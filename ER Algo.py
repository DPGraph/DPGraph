
# coding: utf-8

# In[210]:


import pandas as pd
import numpy as np
import math


# In[23]:


# define how many nodes we want to subset
num_nodes = 200


# In[234]:


# first we read in a subset of FB

# we only care about the first 200 nodes

fb_data = pd.read_csv("facebook_combined.txt", sep=" ")
fb_sub = fb_data[fb_data["1"] < num_nodes].to_numpy()
fb_flat = fb_sub.flatten()

def edge_density(G, e, k_star):
    # Step 0: we preprocess the graph to get the degree of each vertex
    G_flat = G.flatten()
    deg_array = []
    one_vec = np.ones(len(G_flat))
    for i in range(num_nodes):
        cur_count = one_vec.T @ (G_flat == i)
        deg_array.append(int(cur_count))
    
    # Step 1:
    # calculate p_g, the empirical edge densitiy
    # and d_g, the empirical average degree 
    total_edge = num_nodes*(num_nodes-1)/2
    p_g = len(G)/total_edge
    d_g = (num_nodes-1)*p_g

    # Step 2: 
    # we calcualte beta. Clarify if this is a typo.
    # Note: when e is 0.1, and alpha is 1, sometimes this creates a type error
#     print(e)
#     print(1/k_star**0.5)
    beta = min(e, 1/k_star**0.5)

    # Step 3:
    # we need to find the smallest positive interger k_g
    # such that at most k_g vertices have degree outside of 
    # [d_g - k_star - 3*k_g, d_g + k_star + 3*k_g]
    k_g = 1
    k_g_found = False
    while(not k_g_found):
        cur_count = 0
        lower = d_g - k_star - 3*k_g
        upper = d_g + k_star + 3*k_g
        for i in range(num_nodes):
            if (deg_array[i] < lower or deg_array[i] > upper):
                cur_count+=1
        if (cur_count > k_g):
            k_g+=1
        else:
            k_g_found = True
    
    # Step 4:
    # Now we calculate t_array and wt_array
    # note that each entry in the t_array denotes the 
    # distance between deg(v) and the interval we calculated
    t_array = []
    wt_array = []
    true_lower = d_g - k_star - 3*k_g
    true_upper = d_g + k_star + 3*k_g
    for i in range(num_nodes):
        if deg_array[i] < true_lower:
            cur_dist = true_lower - deg_array[i]
            t_array.append(cur_dist)
        elif deg_array[i] > true_upper:
            cur_dist = deg_array[i] - true_upper
            t_array.append(cur_dist)
        else:
            t_array.append(0)
    for i in range(num_nodes):
        cur_wt = max(0, 1-beta*t_array[i])
        wt_array.append(cur_wt)
    
    # Step 5:
    # in this step we construct a 2D array for wt_edge and val_edge
    wt_edge = []
    val_edge = []
    # Note that wt_edge is 2D array. Its first element has length 199, second 198, and 199th element 1.
    for i in range(num_nodes-1):
        cur_node_array = []
        for j in range(i+1, num_nodes):
            wt_to_append = min(wt_array[i], wt_array[j])
            cur_node_array.append(wt_to_append)
        wt_edge.append(cur_node_array)
    # now we construct val_edge
    G_list = G.tolist()
#     print(G_list)
    for i in range(num_nodes-1):
        cur_node_val = []
        for j in range(i+1, num_nodes):
            x_e = 0
            cur_edge = [i, j]
            if cur_edge in G_list:
                x_e = 1
            # this is the wt of current edge
            wt_e = wt_edge[i][j-i-1]
            cur_wt = wt_e * x_e + (1 - wt_e)  * p_g
            cur_node_val.append(cur_wt)
        val_edge.append(cur_node_val)
    
    # Step 6: we take the unordered sum of all the edges
    f_g = 0
    for i in range(len(val_edge)):
        f_g += sum(val_edge[i])
    
    # Step 7: This step has some challanges: we need to find what c is
    # and we also need to solve a maximization problem
    # At the end of step 7, we should get a value for s
    
    # Steven's comment: discuss whether l is calculated correctly.
    # Also discuss how c should be calculated.
    L = 1/beta - k_g - k_star
    c = 1
    # Note, if our understanding about L is corret, 
    # then the formulate given in the paper actually has a simplied form
    # I don't think that matters too much here
    term_one = c*math.exp(-beta*L)
    term_two = k_g + L + k_star + beta*(k_g+L)*(k_g+L+k_star) + 1/beta
    s = term_one * term_two
    
    # Step 8: Lastly we combine f_g and s to get a return value
    # First we sample z from the t-distribution with 3 degrees of freedom
    z = np.random.standard_t(3)
    res = 2 * (f_g + s * z / e) / (num_nodes * (num_nodes - 1)) 
    return res


# In[221]:


# This is the function we run to estimate the parameter

def ER_estimate(G, e, alpha):
    # Step 1, we calculate p_prime
    # first sample from LAP
    z = np.random.laplace()
    deg_dense = 2*len(G)/num_nodes/(num_nodes-1)
    print("Real degree density is "+str(deg_dense))
    p_prime = deg_dense + 2*z/e/num_nodes
   
    # Step 2
    # In this step we calcualte p_til and k_til
    # I am just going to use natural log since base isn't specified. 
    p_til = p_prime + 4*math.log(1/alpha)/e/num_nodes
    k_til = (p_til * num_nodes * math.log(num_nodes/alpha))**0.5
    
    # Step 3
    p_est = edge_density(G, e, k_til)
    print("Estimated degree density is "+str(p_est))
    return p_est


# In[248]:


# # print([1,2])

# def hi():
#     for i in range(4):
#         for j in range(i+1, 5):
#             cur_edge = [i, j]
#             print(cur_edge)
# [0,2] in fb_sub.tolist()
# # print(fb_sub)
# edge_density(fb_sub, 1, 1)
ER_estimate(fb_sub, 0.1, 0.1)

