# Author: Vikas Vijigiri, Python epCUT, July, 2020
# Enhanced perturbative continuous transformation code(epCUT/pCUT).
# coding:utf-8


#!/usr/bin/env python


################## Load Modules ########################
from __future__ import print_function
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.linalg as la
import sys
import array
import time
import argparse
import scipy.sparse
import scipy.sparse.linalg
########################################################
import itertools
from matplotlib import pyplot as plt
from numba import jit

from random import seed
from random import choice
from random import random
from random import randint
import ast

from scipy.sparse.linalg import eigsh
from scipy.stats import uniform
from scipy.integrate import odeint
from comb import *
from sympy import *
from coef_func import *
from global_var import *
from lattice import lattice
from collections import deque
########################################################

# ******************** input here ***********************
pert_op = [2, 0, -2]
init_glob_var(pert_op)
pert_order = 3
f = {}
lx = 4
ly = 4
Ns = lx*ly
########################################################


def T_op(ls, i):
    for j in range(0, 1):
        ls[bsp[j][i]] = 1 - ls[bsp[j][i]]
    return ls


def check_state(T, ls, i):
    if T == 2 and ls[bsp[0][i]] == 0 and ls[bsp[1][i]] == 0:
        m = 1
    elif T == -2 and ls[bsp[0][i]] == 1 and ls[bsp[1][i]] == 1:
        m = 1
    else:
        m = 0
    return m


def coefficients(lx, ly, Ns, f, pert_order, pert_op):
    new_pert_op = map_gcd(pert_op)
    mp = mapping(pert_op, new_pert_op)

    for i in range(0, len(pert_op)):
        f[bin([new_pert_op[i]])] = 1

    for order in range(2, pert_order+1):
        ls = [p for p in itertools.product(pert_op, repeat=order)]
        fl = open("H_coef_" + str(order) + ".txt", 'w')
    ########################################################
        x = Symbol('x')
        for j in range(0, len(ls)):
            g = 0
            for i in range(1, order):
                s1 = np.sign(M(list(ls[j])[0:i]))
                s2 = np.sign(M(list(ls[j])[i:order]))
                N = M(ls[j])
                m1 = list(ls[j][0:i])
                m2 = list(ls[j][i:order])
                g += (exp((abs(N)-abs(M(m1))-abs(M(m2))) * x)) * \
                    (s1-s2)*f[bin(part_map(m1))]*f[bin(part_map(m2))]
            num = bin(part_map(ls[j]))
            f[num] = integrate(g, (x, 0, x))
            if N == 0:
                fl.write(str([[str(ls[j])], str(limit(f[num], x, oo))]))
                fl.write("\n")
        fl.close()
    #########################################################
    del f, ls
    gs = [0] * Ns
    bpn, bp2s, bsp = lattice(lx, ly)
    #########################################################

    for order in range(2, pert_order+1):
        with open("H_coef_" + str(order) + ".txt", 'r') as f:
            for line in f:
                ls = [int(s) for s in line.strip() if s.isdigit()]
                ns = gs
                for i in range(0, pert_order):
                    for j in range(0, Ns):
                        m = check_state(ls[i], ns, i)
                        ns = T_op(ns, 0)
                print(T_op(gs, 0))
        f.close()


def gs():
    return []
    
def flip(x):
    return 1-x    
###################### Main code here ######################

#print(state(Ns))


G=[];
C=[];
def create(G,Ns):
    for i in range(Ns):
        G.append(i)
        C.append(1);
    return G;
    
G=create(G,Ns)
def annihilate(G,Ns):
    G = deque(G)
    G.popleft()    
    return G;
    
def hopp(G,i):
    n1,n2=NN(i)
    if G[n1]
    neighbour(i)

print(G)


# ******************** DES solver ***********************
