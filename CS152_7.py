import random
import numpy as np

random.seed()

EPISODES = 10

arrows = ["^", ">", "v", "<"]
returns = [[[], [], [], []] for i in range(9)]
policy = [[25, 25, 25, 25] for i in range(9)]
q = [[-9999, -9999, -9999, -9999] for i in range(9)]
next_states = [[0, 1, 3, 0],
               [1, 2, 4, 0],
               [2, 2, 5, 1],
               [0, 4, 6, 3],
               [1, 5, 7, 3],
               [2, 5, 8, 4],
               [3, 7, 6, 6],
               [4, 8, 7, 6],
               [5, 8, 8, 7]]

for i in range(EPISODES):        
    print(f"trace_{i}")
    s = random.randrange(0, 8)
    intended_a = random.randrange(0, 4)
    r = 0
    trace = []
    while s != 8:
        actual_a = intended_a
        prob1 = random.randrange(0, 10)
        if  prob1 == 0:
            actual_a = (intended_a + 1) % 4
        elif prob1 == 9:
            actual_a = (intended_a - 1) % 4

        print(f"(r={r}, s={s}, {arrows[intended_a]}, {arrows[actual_a]})")
        
        if s == next_states[s][actual_a]:
            r = -10
        else:
            r = -1
        trace.append((s, intended_a, r))       
        s = next_states[s][actual_a]        
        prob2 = random.randrange(0, 100)
        if prob2 < policy[s][0]:
            intended_a = 0
        elif prob2 < policy[s][0] + policy[s][1]:
            intended_a = 1
        elif prob2 < policy[s][0] + policy[s][1] + policy[s][2]:
            intended_a = 2
        else:
            intended_a = 3
    for index, line in enumerate(trace):
        for k in trace[index:]:
            if q[line[0]][line[1]] == -9999:
                q[line[0]][line[1]] = k[2]
            else:
                q[line[0]][line[1]] += k[2]
    
    averages = np.array([[0.0, 0.0, 0.0, 0.0] for i in range(9)])
    for m in range(9):
        for n in range(4):
            returns[m][n].append(q[m][n])
            averages[m][n] = sum(returns[m][n]) / len(returns[m][n])

    for l in range(9):
        policy[l] = np.array([0, 0, 0, 0])
        directions = np.argwhere(averages[l] == np.amax(averages[l])).flatten().tolist()
        for q in directions:
            policy[l][q] = 100 / len(directions)
        
print(policy)           
             
            

            

