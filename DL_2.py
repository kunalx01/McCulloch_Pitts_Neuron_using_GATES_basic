## Declaring the libraries and function 

import numpy as np
def linear_threshold_gate(input_val:int , threshold:float) -> int:
    if input_val >= threshold:
        return 1
    else:
        return 0
    
## Taking the input matrix as 0 and 1    

input_matrix = np.array ([
        [0,0],
        [0,1],
        [1,0],
        [1,1] ])
#print(f'input table:\n {input_matrix}')

## $$ FOR AND GATE $$ ##

weights = np.array([1,1])
#print(f'weights:{weights}')

dot_pr = np.dot(input_matrix,weights)
#print(f'dot_product:{dot_pr}')    
 
   
threshold = 2
print(f'The Neuron Activation for AND GATE at Threshold value {threshold}')
for i in range(0,4):
    activation = linear_threshold_gate(dot_pr[i],threshold)
    print(f'Activation: {activation}')   
    
    
    ## $$ FOR OR GATE $$ ##

weights = np.array([1,1])
#print(f'weights:{weights}')

dot_pr = np.dot(input_matrix,weights)
#print(f'dot_product:{dot_pr}')    
 
   
threshold = 1
print(f'The Neuron Activation for OR GATE at Threshold value {threshold}')
for i in range(0,4):
    activation = linear_threshold_gate(dot_pr[i],threshold)
    print(f'Activation: {activation}')   
    
    
    ## $$ FOR NOR GATE $$ ##

weights = np.array([-1,-1])
#print(f'weights:{weights}')

dot_pr = np.dot(input_matrix,weights)
#print(f'dot_product:{dot_pr}')    
 
   
threshold = 0
print(f'The Neuron Activation for NOR GATE at Threshold value {threshold}')
for i in range(0,4):
    activation = linear_threshold_gate(dot_pr[i],threshold)
    print(f'Activation: {activation}')   
