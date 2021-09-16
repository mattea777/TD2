# -*- coding: utf-8 -*-

# Q1

def poly_mult(P,Q):
    res = [0] * (len(P) + len(Q))
    for i in range(len(P)):
        for j in range(len(Q)):
            res[i + j] += P[i] * Q[j]
    return res
            
            

def cost_mult(n):
    if n==1:
        return 1
    return 2 * (n**2) - 2*n + 1

# Q2

def poly_add(P,Q):
    
    out = [0] * max(len(P), len(Q))
    for i in range(min(len(P), len(Q))):
        sum1 = P[-i-1] + Q[-i-1]
        out[-i-1] += sum1 % 10
        if sum1 >= 10:
            out[-i-2] = 1
    return out
        

         
def neg(P):
    for i in P:
        i = -i
    return P
   
def shift(P,k):
   P += [0] * k
   return P
  
# Q3  
  
def poly_kara_mult(P,Q):
    pass
    
def cost_poly_kara_mult(n):
    pass

# Q4 

def cost_poly_tc3_mult(n):
    pass

# Q5 hybrid
   
def poly_switch_mult(d,P,Q):
    pass

def cost_switch_mult(d,n):
    pass

   
