
#Viterbi algorithm
import numpy as np
from math import log
import random
random.seed(1003)

def q1():
    TOSS_OUT = open("TOSS_OUT.txt","w")
    CUBES_OUT = open("CUBES_OUT.txt", "w")
    c = random.randint(0,1)
    for i in range(200):
        if c == 0:
            x = random.randint(1,6)
            TOSS_OUT.write(" " + str(x))
            CUBES_OUT.write(" F")
            s = random.randint(1,20)
            if s == 1:
                c = 1
        else:
            x = random.randint(1,10)
            if x > 6:
                x = 6
            TOSS_OUT.write(" " + str(x))
            CUBES_OUT.write(" U")
            s = random.randint(1,10)
            if s == 1:
                c = 0
    
    TOSS_OUT.close()
    CUBES_OUT.close()


def q2():
    TOSS_OUT = open("TOSS_OUT.txt","r")
    X = np.array(list(map(int, TOSS_OUT.readline().split())))
    y = 0
    k = 0
    
    B = np.array([[1/6 , 1/6 , 1/6, 1/6, 1/6, 1/6],[1/10, 1/10, 1/10, 1/ 10, 1/10, 1/2]])
    A = np.array([[0.95, 0.05],[0.1, 0.9]])
    V = np.zeros((2,200))
    P = np.zeros((2,200))
    
    V[0][0] = log(B[0][X[1] - 1] * 0.5)
    V[1][0] = log(B[1][X[1] - 1] * 0.5)
    
    for i in range(199):
        V[0][i + 1] = log(B[0][X[i + 1] - 1]) + max([V[0][i] + log(A[0][0]), V[1][i] + log(A[1][0])])
        V[1][i + 1] = log(B[1][X[i + 1] - 1]) + max([V[0][i] + log(A[0][1]), V[1][i] + log(A[1][1])])
        
        P[0][i + 1] = np.argmax(np.array([V[0][i] + log(A[0][0]), V[1][i] + log(A[1][0])])) 
        P[1][i + 1] = np.argmax(np.array([V[0][i] + log(A[0][1]), V[1][i] + log(A[1][1])]))
    
    out = []
    if np.argmax(np.array([V[0][199] , V[1][199]])) == 0:
        out.append(" F")
        y = 0
    else:
        out.append(" U")
        y = 1
        
    for i in range(199):
        y = P[int(y)][199 - i]
        if y == 0:
            out.append(" F")
        else:
            out.append(" U")
            
    if X[0] == 6:
        out.append(" U")
    else:
        out.append(" F")        
        
    HMM_OUT = open("HMM_OUT.txt","w")    
        
    for i in range(200):
        HMM_OUT.write(out[200 - i])
    
    HMM_OUT.close()
    TOSS_OUT.close()


def q3():
    
    TF = FF = TU = FU = 0 
    
    HMM_OUT = open("HMM_OUT.txt","r")
    CUBES_OUT = open("CUBES_OUT.txt", "r")
    
    HMM = HMM_OUT.readline().split()
    CUBES = CUBES_OUT.readline().split()
    
    for ind, i in enumerate (HMM):
        if i == CUBES[ind]:
            if i == "F":
                TF = TF + 1
            else:
                TU = TU + 1
        else:
            if i == "F":
                FF = FF + 1
            else:
                FU = FU + 1
                
    print("TF:", TF," FF:", FF, " TU:", TU, " FU:", FU)
    print("accuracy:", (TF + TU) / (TF + TU + FF + FU))
            
q1()
q2()
q3()