#alpha async ECA
import random 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

powers_of_two= np.array([[4], [2] ,[1]])

def step(x, rule_binary):

    x_shift_right = np.roll(x, 1)   # circular shift to right
    x_shift_left = np.roll(x, -1)  # circular shift to left
    y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)  
    z = np.sum(powers_of_two * y, axis=0).astype(np.int8)  

    return rule_binary[7-z]

def cellular_automaton(rule_number, size, steps,
                       init_cond='random', impulse_pos='center', alpha=0.5):


    assert 0 <= rule_number <= 255
    assert init_cond in ['random', 'impulse']
    assert impulse_pos in ['left', 'center', 'right']
   
    rule_bin_str=np.binary_repr(rule_number,width=8)
    rule_binary=np.array([int(i) for i in rule_bin_str],dtype=np.int8)
    print(rule_binary)
    x=np.zeros((steps, size), dtype=np.int8)

    if init_cond == 'random':
           x[0, :] = np.array(np.random.rand(size) < alpha, dtype=np.int8)
          # print((x[0, :].tolist())[1])
    elif init_cond == 'impulse':
            if impulse_pos == 'left':
                x[0, 0] = 1
            elif impulse_pos == 'right':
                x[0 , size -1] = 1
                
            else:
                x[0, size//2] = 1

    for i in range(steps-1):
        for j in range(size):
            rando = random.random()
            if rando < alpha :
                 x[i + 1, : ] = step(x[i, : ], rule_binary)
            else :
               # print(x)
                continue

         #   print(x)
        
    return x


    
    


rule_no = 30
size = 5
steps = 10
init_cond = 'random'
impulse_pos = 'left'
alpha = 0.8

y = cellular_automaton(rule_no, size, steps, init_cond, impulse_pos ,alpha)

fig = plt.figure(figsize=(10, 10))

ax = plt.axes()
#ax.set_axis_off()

ax.imshow(y, interpolation='none',cmap='RdPu')
#plt.show()
#plt.savefig('elementary_cellular_automaton12.png', dpi=300, bbox_inches='tight')



