import os
import numpy as np
import pandas as pd

cwd = os.getcwd()

data = pd.read_csv('data2.csv')
data_array = np.array(data)

# Create an array to store which groups have been assigned projects
assigned_g = np.zeros(36)
assigned_g = np.reshape(assigned_g,(36,1))

# Create an array to store which projects have been assigned
assigned_p = np.zeros(48)
assigned_p = np.reshape(assigned_p,(48,1))

points = 0
# Go through every student/pair and, if their first choice is not assigned, give it to them 

print ('\n First choices:')
for i in range(36):
    if assigned_g[i] == 0:
        first = data_array[i,0]
        if assigned_p[first-1] == 0:
            if i<16:
                print (i+1, first) # Groups 1-15 are already paired up so store 2
                assigned_g[i] = 2
                assigned_p[first-1] = 2
                points = points + 2
            else:
                print (i+1, first) # Can pair up people 16-36 so store 1
                assigned_g[i] = 1
                assigned_p[first-1] = 1
                points = points + 1

# Run this again but allowing us to pair unpaired people.
for i in range(17,36):
    if assigned_g[i] == 0:
        first = data_array[i,0]
        if assigned_p[first-1] == 1:
            print (i+1, first)
            assigned_g[i] = 2
            assigned_p[first-1] = 2
            points = points + 1

# Same for second choice
print ('\n Second choices:')
for i in range(36):
    if assigned_g[i] == 0:
        second = data_array[i,1]
        if assigned_p[second-1] == 0:
            if i<16:
                print (i+1, second)
                assigned_g[i] = 2
                assigned_p[second-1] = 2
                points = points + 4
            else:
                print (i+1, second)
                assigned_g[i] = 1
                assigned_p[second-1] = 1
                points = points + 2

# Same for third choice
print ('\n Third choices:')
for i in range(36):
    if assigned_g[i] == 0:
        third = data_array[i,2]
        if assigned_p[third-1] == 0:
            if i<16:
                print (i+1, third)
                assigned_g[i] = 2
                assigned_p[third-1] = 2
                points = points + 6
            else:
                print (i+1, third)
                assigned_g[i] = 1
                assigned_p[third-1] = 1
                points = points + 3
            
print('Point total =',points)

# Upon grouping we are only left with 8 and 12 requiring manual allocation.