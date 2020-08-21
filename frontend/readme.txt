The frontend to display the benchmark results

To download the full dataset, please go to https://drive.google.com/drive/folders/1jlxKftEthXRpoxeeeec2avAgCI51QTwQ?usp=sharing

Download all the csv files from this folder from the link above and put all of them into the same folder(frontend). Do not put the csv files in a Dataset.

Note: Please make sure that you have all the files in the same way we have in the folder. 

new_algorithm.py cannot change the name of it due to that it is the template of the files that can be downloaded for the User. Or you can change the name that is used for download in the uploading.html with the name you desire. 

Currently, the subgraph counting is not working right now. 

When you trying to open the html page, please make sure that you have php being installed. Open the html files through a live server locally. To do this, after installing php, use the following command: 

>php -S 127.0.0.1:8000 

which then you can then open frontier.html at this address: http://127.0.0.1:8000/frontier.html.

Uploads folder:

The download folder is for the ability to allow users to upload their own algorithm for the corresponding algorithm to view their own result. For more details about the upload folder, please take a look at the readme file in the upload folder

The details about the csv files:
The file with "edge" is about the edge DP and the files without it is about node DP

The file with "cdf" is about the cdf graph plotting

The file with "algo" is about the noisy part of the graph

For the way to generate those files above, please take a look at the python code in the uploads folder and that will give you an idea how those files are generated.

The "HistCSV" is the original histogram plotting of the dataset. 

For this file to be generated, please take a look at the uploads truehist.py
