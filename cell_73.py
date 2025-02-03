#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverse_list(matrix_copy):
    for forward in range(0,len(matrix_copy),1):
        if forward != (len(matrix_copy)//2):
            temp = matrix_copy[forward]
            matrix_copy[forward] = matrix_copy[((len(matrix_copy)-1)-forward)]
            matrix_copy[((len(matrix_copy)-1)-forward)] = temp
        elif forward == len(matrix_copy)//2:
            break
    return(matrix_copy)
n = int(input("integer: "))
matrix = [None] * n
for i in range(0,n,1):
    matrix[i] = [None]*n
k = []
for _ in range(1,(n**2)+1,1):
    k.append(_)
i = 0
for column in range(0,n,1):
    for row in range(0,n,1):
        matrix[row][column] = k[i]
        i+=1
matrix_copy = [None] * n
for column in range(-1,n,2):
    if column != -1:
        for row in range(0,n,1):
            matrix_copy[row] = matrix[row][column]
        matrix_copy = reverse_list(matrix_copy)
        for row in range(0,n,1):
            matrix[row][column] = matrix_copy[row]
for row in range(0,n,1):
        print(matrix[row])

