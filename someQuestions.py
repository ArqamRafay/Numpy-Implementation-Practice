# Question 01
# Write a NumPy program to add, subtract, multiply following two matrics.
#  a = [[-2,  2,  3], 
#       [ 5, -2,  3],
#       [ 9,  2, -2]]

# b = [ [ 1,   2,  -1], 
#       [ 4,  -1,   3],
      # [-1,   2,  -2]]

import numpy as np
import matplotlib.pyplot as plt
import math 

a = [[-2, 2, 3], [ 5, -2, 3], [ 9, 2, -2]]
b = [ [ 1, 2, -1], [ 4, -1, 3], [-1, 2, -2]]
ADD = np.add(a,b)
SUB = np.subtract(a,b)
MUL = np.multiply(a,b)

print("Addition")
print(ADD)
print('Subtraction')
print(SUB)
print('Multiplication')
print(MUL)

# Question 02
# Write a NumPy program to find the min and max of a given matrix.

a = [[-2, 2, 3], [ 5, -2, 3], [ 9, 2, -2]]
b = [ [ 1, 2, -1], [ 4, -1, 3], [-1, 2, -2]]

maxA= np.max(a)
maxB = np.max(b)
minA = np.min(a)
minB = np.min(b)

print('Max value in A matrix: ' + str(maxA))
print('Max value in B matrix: '+str(maxB))
print('Min value in A matrix: '+str(minA))
print('Min value in B matrix: '+str(minB))

# Question 03
# Write a NumPy program to test whether any of the elements of a given array is non-zero.

a = [[-2, 2, 3], [ 5, -2, 3], [ 9, 2, -2]]
b = [ [ 1, 2, -1], [ 4, -1, 3], [-1, 2, -2]]

c = np.any(a)
d = np.any(b)
print(c)
print(d)

# Question 04
# Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.

a = [[-2, 2, 3], [ 5, -2, 3], [ 9, 2, -2]]
b = [ [ 1, 2, -1], [ 4, -1, 3], [-1, 2, -2]]

aa = [[-2, 2, 3], [ 5, -2, 3], [-1, 2, -2]]
bb = [ [-2, 2, 3], [ 5, -2, 3], [-1, 2, -2]]

print(np.allclose(a,b))
print(np.allclose(aa,bb))

# Question 05
# Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.

print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5)

# Question 06
# Write a NumPy program to create an array of all the even integers from 10 to 50.

print(np.arange(10,50,2))

# Question 07
# Write a NumPy program to create a 3x3 identity matrix. Go to the editor
# Click me to see the sample solution

print(np.identity(3))

# Question 08
# Write a NumPy program to compute the x and y coordinates for points on a sine, 
# cosine curve and plot the points using matplotlib Compute the x and y coordinates 

x = np.arange(0, 3*np.pi, 0.2)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)

plt.xlabel('x axis ')
plt.ylabel('y axis ')

plt.title('Sine and Cosine curve')
plt.legend(['Sine', 'Cosine'])

plt.show()

# Question 09
# Write a NumPy program to compute and plot the signmoid, softmax, relu activation functions using matplotlib.



def signmoid():
  # using signmoid formula 
  x = np.linspace(-10, 10, 100)
  z = 1/(1 + np.exp(-x)) 
  
  plt.plot(x, z) 
  plt.title("signmoid Graph")
  plt.xlabel("x-axis") 
  plt.ylabel("y-axis") 
  plt.show() 

def softmaxValue(inputs):
  return np.exp(inputs) / float(sum(np.exp(inputs)))


def graph_Softmax():
  graph_x = range(0, 21)
  graph_y = softmaxValue(graph_x)
  plt.plot(graph_x, graph_y)
  plt.title("Softmax")
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")
  plt.show()

def relu():
   
  z = np.arange(-2, 2, .1)
  zero = np.zeros(len(z))
  y = np.max([zero, z], axis=0)
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(z, y)
  ax.set_ylim([-0.5, 2.0])
  ax.set_xlim([-2.0, 2.0])
  ax.grid(True)
  ax.set_xlabel('x=axis')
  ax.set_title('Relu')
  plt.show()

signmoid()
graph_Softmax()
relu()

# Question 10
# Write a NumPy program to compute the sum of the diagonal element of a given array.

a = [[-2, 2, 3], [ 5, -2, 3], [ 9, 2, -2]]
b = [ [ 1, 2, -1], [ 4, -1, 3], [-1, 2, -2]]

print(np.trace(a))
print(np.trace(b))