import numpy as np
import pandas as pd

data = pd.read_csv('data_modified.csv')
data_array = np.array(data)

# Create an array to store which groups have been assigned projects
assigned_g = np.zeros(36)
assigned_g = np.reshape(assigned_g,(36,1))

# Create an array to store which projects have been assigned
assigned_p = np.zeros(48)
assigned_p = np.reshape(assigned_p,(48,1))

counts = []
counts = np.array(counts)
assignments = np.zeros(72)
assignments = np.reshape(assignments,(36,2))
q = 1
for i in range(36):
    assignments[i,0] = q
    q = q + 1

# Creating a temporary assignment where each student/pair gets their 1st choice
t_assignment = np.zeros(72)
t_assignment = np.reshape(t_assignment,(36,2))
choice = np.zeros(36)
choice = np.reshape(choice,(36,1))

for i in range(36):
    t_assignment[i,0] = i+1
    t_assignment[i,1] = data_array[i,0]
    choice[i] = 1
    if i<15:
        assigned_p[data_array[i,0]-1] = assigned_p[data_array[i,0]-1] + 2
    elif i>15:     
        assigned_p[data_array[i,0]-1] = assigned_p[data_array[i,0]-1] + 1

values = []
M = 0 # Number of matchings
count = 0
number = 0
project = 0
while M < 1:  
    for i in range(36):
        if assigned_g[i] != 5:
            if choice[i] == 1:
                z = []
                z = np.isin(values,data_array[i,0])
                values = np.append(values,data_array[i,0]) # Stores assigned projects
                problem_project = data_array[i,0]
            elif choice[i] == 2:
                z = []
                z = np.isin(values,data_array[i,1])
                values = np.append(values,data_array[i,1]) # Stores assigned projects
                problem_project = data_array[i,1]
            elif choice[i] == 3:
                z = []
                z = np.isin(values,data_array[i,2])
                values = np.append(values,data_array[i,2]) # Stores assigned projects 
                problem_project = data_array[i,2]
        if z.any() == True and assigned_p[problem_project-1] > 2:
            x = i
            print(x+1)
            break
    values = []
    if choice[x] == 1:
        t_assignment[x,1] = data_array[x,1] # Identify the project being double assigned and move the student on to their second choice
        choice[x] = 2
        if x>15:
            assigned_p[data_array[x,0]-1] = assigned_p[data_array[x,0]-1] - 1 # Reduce the count of the assigned project by the number of people being moved away
            assigned_p[data_array[x,1]-1] = assigned_p[data_array[x,1]-1] + 1 # Increase the count of the project that the group is being moved to
        elif x<15:
            assigned_p[data_array[x,0]-1] = assigned_p[data_array[x,0]-1] - 2
            assigned_p[data_array[x,1]-1] = assigned_p[data_array[x,1]-1] + 2
           
    elif choice[x] == 2:
        t_assignment[x,1] = data_array[x,2] # Identify the project being double assigned and move the student on to their third choice
        choice[x] = 3
        if x>15:
            assigned_p[data_array[x,1]-1] = assigned_p[data_array[x,1]-1] - 1 # Reduce the count of the assigned project by the number of people being moved away
            assigned_p[data_array[x,2]-1] = assigned_p[data_array[x,2]-1] + 1 # Increase the count of the project that the group is being moved to
        elif x<15:
            assigned_p[data_array[x,1]-1] = assigned_p[data_array[x,1]-1] - 2
            assigned_p[data_array[x,2]-1] = assigned_p[data_array[x,2]-1] + 2
    elif choice[x] == 3: # If the student is already on their third choice, move an earlier student down a choice to make room
        project = data_array[x,2]
        if project == 0 :
            break
        t_assignment[x,1] = data_array[x,2]
        print(project)
        for i in range(36):
            if t_assignment[i,1] == project:
                if choice[i] == 1:
                    t_assignment[i,1] = data_array[i,1]
                    choice[i] = 2
                elif choice[i] == 2:
                    t_assignment[i,1] = data_array[i,2]
                    choice[i] = 3
        
    count = count + 1
    if count > 50:
        M = M + 1
print(t_assignment)
print(assigned_p)
