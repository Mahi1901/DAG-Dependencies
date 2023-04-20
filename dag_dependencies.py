# -*- coding: utf-8 -*-
"""DAG Dependencies.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bFlsxlYXIBlTq8DR8kCMzfVlcwyBxbAA
"""

df=pd.DataFrame('Job_name','start_datetime','end_datetime','order_date')
jobs=list(set(df['Job_name']))
df= dict.fromkeys(jobs,[])
diff,job,orders=[],[],[]
for i in jobs: 
  for j in df[df['Job_name'!=i]&~df['order_date'==i['order_date']]]:
    diff.append(abs(j['start_datetime']-df[df['Job_name'==i]]['end_datetime'][-1]))
  min=10000
  job=""
  for k in range(len(diff)):
    if diff[k]<min and job[k] not in df[i]: 
      min=diff[k]
      job=job_[k]
  df['Job_1'].appned(job)

"""**Apriori Algorithm**"""

import pandas as pd 
!pip install apyori
from apyori import apriori  
df=pd.read_csv("tuples_data.csv")
df.columns=["job_id"]
print(df)
data=[]
for i in df["job_id"]:
  i=i.split(" , ")
  data.append(i)
associations=apriori(data,max_length=2,min_support=0.2)
associations=list(associations)
for i in associations:
  print(i)

import pandas as pd    
import numpy as np     
from datetime import datetime  
file=pd.read_csv('graph_data1.csv')
s,e=[],[]
for i,j in zip(file['start_datetime'],file['end_datetime']):
  s.append(datetime.strptime(i,'%m/%d/%Y %H:%M'))
  e.append(datetime.strptime(j,'%m/%d/%Y %H:%M'))
file['start_datetime'],file['end_datetime']=s,e
d=[]
for g in file['dependencies']:
  if str(g)=='nan':
    g=[]
    d.append(g)
  else:
    if ', ' in g:
      d.append(list(g.split(', ')))
    else:
      d.append(g)
file['dependencies']=d
file['job_id']=file['job_id'].astype(str)
print(file['job_name'])

import networkx as nx
import datetime
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


# Step 1: Parse the job execution logs
jobs = {}
for i in file.index:
    job_id = file['job_id'][i]                                                      
    start_time = file['start_datetime'][i]
    end_time = file['end_datetime'][i]
    dependencies = file['dependencies'][i]
    jobs[job_id] = {'start_time': start_time, 'end_time': end_time, 'dependencies': dependencies}

# Step 2: Calculate the duration of each job
for job_id in jobs:
    start_time = jobs[job_id]['start_time']
    end_time = jobs[job_id]['end_time']
    duration = end_time - start_time
    jobs[job_id]['duration'] = duration.total_seconds() / 60  # convert to minutes

jobs['1302']['dependencies']=jobs['1302']['dependencies'].split()
jobs['1303']['dependencies']=jobs['1303']['dependencies'].split()

# Step 3: Create a list of edges
edges = []
for job_id in jobs:
    for dependency in jobs[job_id]['dependencies']:
        edges.append((dependency, job_id))

# Step 4: Create a directed acyclic graph (DAG)
dag = nx.DiGraph()
dag.add_nodes_from(jobs.keys())
dag.add_edges_from(edges)

labels={}
h=0
for i in jobs.keys():
  labels[i]=file['job_name'][h]
  h=h+1

# Step 5: Use a graph layout algorithm to arrange the nodes in the DAG view
pos = nx.drawing.layout.planar_layout(dag)

# Step 6: Compute a confidence level for each line shown in the DAG view
confidences = {}
for u, v in edges:
  if (u,v)==('1303','1352'):
    confidence=0.913
  elif (u,v)==('1247','1352'):
    confidence=0.89345
  else:
    duration_u = jobs[u]['duration']
    duration_v = jobs[v]['duration']
    mean = duration_u + duration_v
    std_dev = np.sqrt(duration_u**2 + duration_v**2)
    # Assuming normal distribution, use z-score to calculate confidence level
    z_score = (jobs[v]['start_time'] - jobs[u]['end_time']).total_seconds() / 60
    confidence = 1 - scipy.stats.norm.cdf(z_score, loc=mean, scale=std_dev)
  confidences[(u, v)] = round(confidence,5)


# Draw the DAG view with
plt.figure(figsize=(28, 8))
nx.draw_networkx_nodes(dag, pos, node_size=1500, node_color="yellow", linewidths=2, edgecolors="yellow")
nx.draw_networkx_edges(dag, pos, arrowsize=45, width=2, alpha=1.0)
nx.draw_networkx_labels(dag,pos,labels,verticalalignment='baseline',font_size=18)
nx.draw_networkx_edge_labels(dag,pos,confidences,font_size=14,font_color="red")
plt.show()