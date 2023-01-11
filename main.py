import random
import numpy as np

n=16
seq = []
chars = ['A', 'C', 'G', 'T']

def check(list):
    if(list.count('A')==4 and list.count('G')==4 and list.count('C')==4 and list.count('T')==4):
        print(list)
    else:
        for i in range(n):
            x = random.choice(chars)
            list.append(x)
        check(list)
        
def maxi(a, b, c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    else:
        return c


for i in range(n):
    x = random.choice(chars)
    seq.append(x)  
   
s1 = "ACACACTA"
s2 = "AGCACACA"

match = 5
mismatch = -4

l1 = 8
l2 = 8

matrix = np.zeros((l1+1, l2+1))

for i in range(9):
    matrix[0][i] = 0;
    
for i in range(9):
    matrix[i][0] = 0;
    
max = 0
max_i = max_j = 0

for i in range(1, 9):
    for j in range(1, 9):
        if(s1[j-1]==s2[j-1]):
            matrix[i][j] = matrix[i][j] + match
        else:
            a = matrix[i-1][j] 
            b = matrix[i][j-i] 
            c = matrix[i-1][j]
            matrix[i][j] = maxi
            (a, b, c) + mismatch
        if(matrix[i][j]>max):
            max = matrix[i][j]
            max_i = i
            max_j = j
        
i = max_i
j = max_j

print(matrix)

while(i!= 0 and j!=0):
    if(s1[j-1])==s2[i=1]):
