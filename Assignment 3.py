#!/usr/bin/env python
# coding: utf-8

# # DSW Assignment 3

# ##### Name: Yue (Billy) Liu NetID: yl992

# ## Question 1

# In[1]:


import networkx as nx
import matplotlib as plt
import matplotlib.cm as cm
import operator
from community import community_louvain
G = nx.karate_club_graph()


# ### Part 1A: Make a visualization of the network.

# In[2]:


print("Karate Network")
nx.draw(G, with_labels=True)


# ### Part 1B

# In[3]:


import networkx.algorithms.community as nx_comm
# communities = nx_comm.louvain_communities(G)
communities = community_louvain.best_partition(G)
communities1 = {}
for k, v in communities.items():
     if v not in communities1:
            communities1[v]=1
     communities1[v]+=1
communities1_sorted = dict(sorted(communities1.items(), key=operator.itemgetter(1),reverse=True))
print("Number of communities: {}".format(len(communities1_sorted)))
for c, size in communities1_sorted.items():
    print("Community:{} Size:{}".format(c,size))


# ### Part 1C

# In[4]:


from networkx.algorithms.community.centrality import girvan_newman
communities2 = girvan_newman(G)
print("The two communities are: ")
gn_dict = {}
index = 0
for c in next(communities2):
    gn_dict[index] = len(c)
    index+=1
gn_sorted = dict(sorted(gn_dict.items(), key=operator.itemgetter(1),reverse=True))

for c, size in gn_sorted.items():
    print("Communitiy {}, Size:{}".format(c,size))
    


# In[5]:


for c in next(communities2):
    print(c)


# ### Part 1D

# In[6]:


partition = community_louvain.best_partition(G)

cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
shapes = 'so^>v<dph8'
pos = nx.spring_layout(G)
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_edges(G, pos, alpha=0.5)
print("Visualization of Louvian Groups")
for node, color in partition.items():
    nx.draw_networkx_nodes(G, pos, [node], node_size=100,
                           node_color=[cmap.colors[color]],
                           node_shape=shapes[color])


# ## Question 2

# In[7]:


G2 =nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)
G2 = G2.to_undirected()


# ### Part 2A

# In[8]:


communities = community_louvain.best_partition(G2)
communities3 = {}
for k, v in communities.items():
     if v not in communities3:
            communities3[v]=1
     communities3[v]+=1
communities3_sorted = dict(sorted(communities3.items(), key=operator.itemgetter(1),reverse=True))
print("Number of communities: {}".format(len(communities3_sorted)))


# ### Part 2B

# In[9]:


for c, size in communities3_sorted.items():
    print("Community:{} Size:{}".format(c,size))

