import numpy as np
from scipy import sparse
import matplotlib as plt
import math

def buildMatrixA(N:int):
    A=sparse.lil_matrix((N-1,N-1))
    A.setdiag(2)
    for i in range(N-2):
        A[i,i+1]=-1
        A[i+1,i]=-1
    return A

def buildMatrixB(N:int):
    B=sparse.lil_matrix((N-1,N-1))
    B.setdiag(-1)
    for i in range(N-2):
        B[i,i+1]=1
    return B

def buildMatrixC(N:int):
    C=sparse.lil_matrix((N-1,N-1))
    C.setdiag(1)
    for i in range(N-2):
        C[i+1,i]=-1
    return C

def buildVectorF(N:int):
    F=np.ones(N-1, np.int8)
    return F


def firstEquation(N:int,eps:float):
    dx=1/N
    sumMatrix=((eps/dx**2)*buildMatrixA(N))+(1/abs(dx)*buildMatrixB(N))
    return sparse.linalg.spsolve(sumMatrix,buildVectorF(N))

def secondEquation(N:int,eps:float):
    dx=1/N
    sumMatrix=((eps/dx**2)*buildMatrixA(N))+(1/abs(dx)*buildMatrixC(N))
    return sparse.linalg.spsolve(sumMatrix,buildVectorF(N))

def given_solution(x:float, eps:float):
    return x - 1 + (np.exp((x-1)/eps) - 1 ) / ((np.exp((-1)/eps )) - 1)


def calcError (N:int, eps:float, calculatedPoints):
    dx=1/N
    uHat=[]
    for i in (range(N+1)):
        uHat.append(given_solution(i*dx,eps))
    sum=0
    for i in (range(N+1)):
        sum+=dx*(uHat[i]-calculatedPoints[i])**2
    return math.sqrt(sum)

print(calcError(1000,0.5,secondEquation(1000,0.5)))