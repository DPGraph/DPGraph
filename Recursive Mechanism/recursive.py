import pandas as pd
import numpy as np
import scipy.optimize
from tqdm import tqdm

def H_linprog(df,n, q, k):
    # assume all ids are arranged as
    # 0, 1, ..., n-1
    m = len(df)
    A_ub = np.zeros([2*(m+n), m+n])
    b_ub = np.zeros(2*(m+n))
    A_eq = np.zeros([1, m+n])
    A_eq[0, m:] = 1
    b_eq = np.ones(1) * k
    for i, (idx, row) in enumerate(df.iterrows()):
        people_list = row.to_numpy()
        l = len(people_list)
        # t >= x_i1 + x_i2 + x_i3 - 2
        A_ub[i*2, m+people_list] = 1
        A_ub[i*2, i] = -1
        b_ub[i*2] = l - 1
        # t >= 0
        A_ub[i*2+1, i] = -1
        b_ub[i*2+1] = 0
    for i in range(n):
        # x_i <= 1
        A_ub[(m+i)*2, m+i] = 1
        b_ub[(m+i)*2] = 1
        # -x_i  <= 0
        A_ub[(m+i)*2+1, m+i] = -1
        b_ub[(m+i)*2+1] = 0
    c = np.zeros(m+n)
    c[:m] = q
    res = scipy.optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)
    return res


def G_linprog(df, n, q, k):
    # assume all ids are arranged as
    # 0, 1, ..., n-1
    m = len(df)
    A_ub = np.zeros([2*(m+n)+n, m+n+1])
    A_ub[2*(m+n):, -1] = -1
    b_ub = np.zeros(2*(m+n)+n)
    A_eq = np.zeros([1, m+n+1])
    A_eq[0, m:-1] = 1
    b_eq = np.ones(1) * k
    for i, (idx, row) in enumerate(df.iterrows()):
        people_list = row.to_numpy()
        l = len(people_list)
        # t >= x_i1 + x_i2 + x_i3 - 2
        A_ub[i*2, m+people_list] = 1
        A_ub[i*2, i] = -1
        b_ub[i*2] = l - 1
        # t >= 0
        A_ub[i*2+1, i] = -1
        b_ub[i*2+1] = 0
        # update sensitivity
        for pid in people_list:
            A_ub[2*(m+n)+pid, i] = q
    for i in range(n):
        # x_i <= 1
        A_ub[(m+i)*2, m+i] = 1
        b_ub[(m+i)*2] = 1
        # -x_i  <= 0
        A_ub[(m+i)*2+1, m+i] = -1
        b_ub[(m+i)*2+1] = 0
    
    c = np.zeros(m+n+1)
    c[-1] = 1
    res = scipy.optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)
    return res

def recursive(n, edges, query, eps1, eps2, theta, beta, mu, logging=False):
    '''
    @n: n is the total number of nodes. We assume their indices are 
    0, 1, ..., n-1
    @edges: edges is a dataframe with columns ['f', 't'].
    It is unlabeled, and edge is from small index to high index.
    @query: 'triangle', '2-star' and so on
    @epsilon: epsilon
    @theta: theta
    @beta: beta
    @mu: mu
    '''
    
    # The efficiency of this algorithm can be further 
    # improved by section 5.3
    
    # 1. Get the output as a dataframe
    if query == 'triangle':
        e1 = edges.copy().rename(columns={'f': 'a', 't': 'b'})
        e2 = edges.copy().rename(columns={'f': 'b', 't': 'c'})
        e3 = edges.copy().rename(columns={'f': 'a', 't': 'c'})
        triangles = e1.join(e2.set_index('b'), on='b', how='inner').join(e3.set_index(['a', 'c']), on=['a', 'c'], how='inner')
        
        df = triangles
        q  = 1
    elif query == '2-star':
        pass
    
    # P.S. Get the local sensivity for the logging purpose
    # Local Sensitivity of query
    values, counts = np.unique(df.to_numpy(), return_counts=True)
    if logging:
        display(f'local sensitivity is {np.max(counts)}')
    
    # 2. Compute the H and G sequence
    H, G = [], []
    if logging:
        ranges = tqdm(range(n+1))
    else:
        ranges = range(n+1)
    for i in ranges:
        Hi = H_linprog(df, n, q, i)['fun']
        Gi = G_linprog(df, n, q, i)['fun'] * 2
        H.append(Hi)
        G.append(Gi)
        
    # 3. Compute delta
    exp_series = np.exp(np.arange(n+1)*beta) * theta
    inversed_G = G[::-1]
    delta = np.min(exp_series[exp_series >= inversed_G])
    if logging:
        display(f'delta is {delta}')
    
    # 4. Compute delta_hat
    Y1 = np.random.laplace(scale=beta/eps1)
    delta_hat = np.exp(mu + Y1) * delta
    
    # 5. Compute X
    X = np.min(H + (n-np.arange(n+1))*delta_hat)
    if logging:
        display(f'X is {X}')
    
    # 6. Compute X_hat
    Y2 = np.random.laplace(scale=delta_hat/eps2)
    X_hat = X + Y2
    
    return {'noisy': X_hat, 'truth': len(df) * q}