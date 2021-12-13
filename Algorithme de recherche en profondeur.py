#!/usr/bin/env python
# coding: utf-8

# In[16]:


def dfs(G,s) :
    couleur=dict()
    for v in G :couleur[v]='blanc'
    P=dict()
    P[s]=None
    couleur[s]='gris'
    Q=[s]
    while Q :
        u=Q[-1]
        R=[y for y in G[u] if couleur[y]=='blanc']
        if R :
            v=R[0]
            couleur[v]='gris'
            P[v]=u
            Q.append(v)
        else :
            Q.pop()
            couleur[u]='noir'
    return P
G=dict()
G['1']=['4','8']
G['2']=['7','6','3']
G['3']=['2','5','8']
G['4']=['6','1']
G['5']=['3']
G['6']=['7','8','4','2']
G['7']=['2','6']
G['8']=['6','3','1']


print(dfs(G,'3'))


# In[ ]:




