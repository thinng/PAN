import os
import random
import numpy as np
import pandas as pd
import scipy
from scipy.spatial import distance
import networkx as nx
from sklearn import metrics

# get features for adjacency graphs
def get_closeness_centrality(A):
    ret = []
    for e in A:
        g = nx.from_numpy_matrix(e)  
        v =  nx.closeness_centrality(g).values()
        ret += [list(v)]
    return np.array(ret)

# turn continuous graphs to ajacency graphs
def to_adjacency_G(din,TOP):
    NUM_COL = 0
    COLUMNS = []
    ls = []
    for line in open(din):
        if NUM_COL==0:
            COLUMNS = line.strip().split(',')
            NUM_COL = len(COLUMNS)
        else:
            cols = line.strip().split(',')
            e = np.asarray(list(map(float,cols)) ) 
            max_idx = e.argsort()[-TOP:][::-1]
            link = np.zeros(NUM_COL)
            link[max_idx] = 1
            ls += [ link ]
    g = np.array(ls)   
    g = pd.DataFrame(g).astype(int)
    g.columns = COLUMNS
    
    cols = list(g.columns)
    edges = []
    gene_idx = []
    for c in cols:
        subs = c.split('_')
        if len(subs)==2:
            edges += [ (int(subs[0]), int(subs[1]))]
            gene_idx += [int(subs[0]), int(subs[1])]
    gene_idx = list(set(gene_idx))
    NUM_NODE = len(gene_idx)
#     print('Number of nodes:', NUM_NODE)
    gene_idx.sort()
    old_new_idx = {}
    for i in range(NUM_NODE):
        old_new_idx[gene_idx[i]] = i
    g = g.values
    G = []
    edge_count = {}
    for x in g:
        m = np.zeros((NUM_NODE,NUM_NODE))
        p = np.where(x)[0] 
        for e in p:
            l,r = old_new_idx[edges[e][0]], old_new_idx[edges[e][1]]
            m[l][r] = 1
            m[r][l] = 1
        G += [m]  
        try: 
            edge_count[sum(sum(m))] += 1
        except:
            edge_count[sum(sum(m))] = 1
#         try: 
#             edge_count[len(p)] += 1
#         except:
#             edge_count[len(p)] = 1
#     print(edge_count)
    return np.array(G)

# classification evaluation
def evaluate(y_test,y_pred):
    AUC = metrics.roc_auc_score(y_test,y_pred)
    y_pred = [1 if e>=.5 else 0 for e in y_pred]
    F1 = metrics.f1_score(y_test, y_pred)
    Accuracy = metrics.accuracy_score(y_test, y_pred)
    Precision = metrics.precision_score(y_test, y_pred)
    Recall = metrics.recall_score(y_test, y_pred)
    tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
    Specificity = tn / float(tn+fp)
    ret = [F1,Precision,Recall,Specificity,Accuracy,AUC]
    return ret