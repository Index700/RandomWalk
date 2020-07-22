#!/usr/bin/env python3
#
#
# Copyright (c) 2019, Keita Kitaura
# All rights reserved.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import random

import graph_tools
# ref: https://github.com/h-ohsaki/graph-tools

def RW(g,S,b):
    count = 1
    judge = True    
    while judge:
        for s in S:        
            #エ-ジェントがいるノードの隣接ノードから一つを選択
            neighbors = g.neighbors(s)
            j = random.choice(neighbors)
            #移動したノードが目的ノードなら終了
            if j == int(b):
                judge = False
            #エ-ジェントがいるノードの更新
            S[S.index(s)] = j  
            
        count += 1
        
    return count

def main():
    n = sys.argv[1]
    a = sys.argv[2]
    b = sys.argv[3]
    n_a = sys.argv[4]
    T = sys.argv[5]
    fname = sys.argv[6]

    #S[i-1]: エ-ジェント i がいるノード id
    S = []

    for i in range(0,int(n_a)):
        S.append(int(a))
    
    g = graph_tools.Graph(directed=False)
    for i in range(1,int(n)):
        g.add_vertex(i)

    with open(fname, 'r') as f:
        for line in f:
            edge = []
            i, j, w = map(int, line.split())
            g.add_edge(i,j)

    result = []
    for i in range(int(T)):
            count = RW(g,S,b)
            result.append(count)

    u_ab = sum(result) / int(T)
    # 結果を表示
    print("u_ab: ",u_ab)

    print("degree of b (", b,"):",g.degree(int(b)))
    
if __name__ == "__main__":
    main()
