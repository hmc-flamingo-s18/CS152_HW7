import random

random.seed()

episodesPerLoop = 2
LOOPS = 5

arrows = ["^", ">", "v", "<"]
returns = [9]
policy = [9]
q = [9]
for i in range(9):
    returns[i] = [[], [], [], []]
    policy[i] = [25, 25, 25, 25]
    q[i] = [-9999, -9999, -9999, -9999]

next_states = [[0, 1, 3, 0],
               [1, 2, 4, 0],
               [2, 2, 5, 1],
               [0, 4, 6, 3],
               [1, 5, 7, 3],
               [2, 5, 8, 4],
               [3, 7, 6, 6],
               [4, 8, 7, 6],
               [5, 8, 8, 7]]

for i in range(LOOPS):        
    for j in range(episodesPerLoop):
        s = random.randrange(0, 8)
        intended_a = random.randrange(0, 4)
        r = 0
        rewards = []
        while state != 8:
            actual_a = intended_a
            prob1 = random.randrange(0, 10)
            if  prob1 == 0:
                actual_a = (intended_a + 1) % 4
            elif prob1 == 9:
                actual_a = (intended_a - 1) % 4

            trace = f"(r={r}, s={s}, {arrows[intended_a]}, {arrows[actual_a]}"
            print(trace)
            
            if s == next_states[s][actual_a]:
                r = -10
            else:
                r = -1
            rewards.append((s, intended_a, r))       
            s = next_states[s][a]        
            prob2 = random.randrange(0, 100)
            if prob2 < policy[s][0]:
                a = 0
            elif prob2 < policy[s][0] + policy[s][1]:
                a = 1
            elif prob2 < policy[s][0] + policy[s][1] + policy[s][2]:
                a = 2
            else:
                a = 3
        for index, reward in enumerate(rewards):
            for k in rewards[index:]:
                if q[reward[0]][reward[1]] == -9999:
                    q[reward[0]][reward[1]] = k[2]
                else:
                    q[reward[0]][reward[1]] += k[2]
             
            

            

