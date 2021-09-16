#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


#Q6
def mult_matrix(A,B):
    pass


#Q7
def cost_mult_matrix(n):
    pass

#Functions split, merge, add_matrix and sub_matrix are given
def split(A):
    A=np.array(A)
    row, col = A.shape
    row2, col2 = row//2, col//2
    return A[:row2, :col2].tolist(), A[:row2, col2:].tolist(), A[row2:, :col2].tolist(), A[row2:, col2:].tolist()

def merge(a,b,c,d):
    return np.vstack((np.hstack((a, b)), np.hstack((c, d)))).tolist()

#Computes the matrix A+B
def add_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
    return C

#Computes the matrix A-B
def sub_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
    return C

#Q8
def strassen(A,B):
    pass

#Q9
def cost_strassen(n):
    pass


#Q10
def convert_01(A):
    pass

#Q11
def transitive_closure(A):
    pass






