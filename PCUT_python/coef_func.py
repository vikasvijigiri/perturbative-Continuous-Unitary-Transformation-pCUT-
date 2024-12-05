from global_var import *


def init_glob_var(pert_op):
    global len_pert_op
    len_pert_op=len(pert_op)


def M(ls):
    return sum(ls)
    
def bin(ls):
    num = 0

    for b in range(0,len(ls)):
        num += ((len_pert_op**b) * (ls[b]+1))
    return num-1    
  
  # algorithm to find H.C.F. of two number
def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x
    
def map_gcd(ls):
    max_pert=max(ls)
    X=[x+max_pert for x in ls]  
    num1 = X[0]
    num2 = X[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, len(X)):
        gcd = find_gcd(gcd, X[i])
    X=[int(x/gcd) for x in X] 
    return X 
    
     
######################################################## 


def mapping(pert_op,new_pert_op):
    global mp
    mp = {}
    for i in range(0,len(pert_op)):
        mp[pert_op[i]]=new_pert_op[i]
    return mp  

def part_map(ls):
    X=[mp[x] for x in ls]
    return X 
