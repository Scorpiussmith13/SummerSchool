#Reversibility Test

import numpy as np
import matplotlib.pyplot as plt
import csv


header_alpha = ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8' ,'0.9']
with open('result.csv', 'w', encoding='UTF8', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(header_alpha)
    
    powers_of_two= np.array([[4], [2] ,[1]])

    def step(x, rule_binary):
        x_shift_right = np.roll(x, 1)   # circular shift to right
        x_shift_left = np.roll(x, -1)  # circular shift to left
        y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)  
        z = np.sum(powers_of_two * y, axis=0).astype(np.int8)  

        return rule_binary[7-z]





    def cellular_automaton(rule_number, size, steps,dict1,
                           init_cond='random', impulse_pos='center', alpha=0.5,):


        assert 0 <= rule_number <= 255
        assert init_cond in ['random', 'impulse']
        assert impulse_pos in ['left', 'center', 'right']
        flag = False
       
        rule_bin_str=np.binary_repr(rule_number,width=8)
        rule_binary=np.array([int(i) for i in rule_bin_str],dtype=np.int8)
       # print(rule_binary)
        x=np.zeros((steps, size), dtype=np.int8)

        if init_cond == 'random':
               x[0, :] = np.array(np.random.rand(size) < alpha, dtype=np.int8)
               list1 = x[0, :].tolist()
               
               num = 0
               for i in list1:
                   num = (num*10) + i
                   
               dict1[num]=1
            #   print(x)
            
        elif init_cond == 'impulse':
                if impulse_pos == 'left':
                    x[0, 0] = 1
                elif impulse_pos == 'right':
                    x[0 , size -1] = 1
                    
                else:
                    x[0, size//2] = 1

        for i in range(steps-1):
                  rando = np.random.random(1)[0]
                  if rando < alpha :
                         x[i + 1, : ] = step(x[i, : ], rule_binary)
                         list1 = x[i + 1, :].tolist()
                         num = 0 
                         for i in list1:
                                num=(num*10)+i
                                
                         if num in dict1:
                             flag = True
                             continue    


                         else:
                              dict1[num]=1
                              flag = False

                         
                  else :
                 #       print(x)
                        continue


        if flag is True: #if a configaration is found to repeat
           list2.append("Reversible")

        else:
           list2.append("Non")

        
        return x,list2


    #rule_no = 30
    size = 4
    steps = 500  
    init_cond = 'random'
    impulse_pos = 'left'
    #alpha = 0.4
    
    for rule_no in range(256):
        list2=list()
        for alpha in np.arange(10,100,10):
            dict1=dict()
            y,list2 = cellular_automaton(rule_no, size, steps, dict1 ,init_cond, impulse_pos ,alpha//100)
           
            #writer.writerow(list2)

        writer.writerow(list2)
            



















"""
fig = plt.figure(figsize=(10, 10))

ax = plt.axes()
#ax.set_axis_off()

#ax.imshow(y, interpolation='none',cmap='RdPu')
#plt.show()
#plt.savefig('elementary_cellular_automaton12.png', dpi=300, bbox_inches='tight')
"""


