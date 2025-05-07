""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import functools
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import numpy as np

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    print("number of points: ", n)
    inside_counter = 0
    outside_counter = 0
    inside_points_x = np.empty(n) # Inte en chans att jag sitter och väntar 15 min på att listorna ska gås igenom
    inside_points_y = np.empty(n)
    outside_points_x = np.empty(n)
    outside_points_y = np.empty(n)
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_points_x[inside_counter] = x
            inside_points_y[inside_counter] = y
            inside_counter += 1
        else:
            outside_points_x[outside_counter] = x
            outside_points_y[outside_counter] = y
            outside_counter += 1

    plt.figure()
    plt.scatter(inside_points_x[:inside_counter], inside_points_y[:inside_counter], color="red", s=5)
    plt.scatter(outside_points_x[:outside_counter], outside_points_y[:outside_counter], color="blue", s=5)
    filename = "MA3_assignment_1_n=" + str(n)
    pi = 4 * inside_counter/n
    plt.text(-1, 1.1, f'pi approx for n = {n}, is: {pi}')
    #plt.show()
    #plt.savefig(filename)
    print(pi)
    return pi

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 
    inside_counter = 0
    d_vector = np.empty(d)
    squared = lambda x : x**2
    for i in range(n):
        for i in range(d):
            d_vector[i] = random.uniform(-1, 1)
        if  functools.reduce(lambda x,y : x+y, (map(squared, d_vector))) <= 1:
            inside_counter += 1

    volume = 2**d*inside_counter/n
    return volume

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    volume = np.pi**(d/2) / (m.gamma(d/2+1))
    return volume

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    start = pc()
    
    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(sphere_volume, n, d) for _ in range(np)]
    result = sum([f.result() for f in futures])
    stop = pc()
    print(f'Sphere volume parallel 1 took {stop-start} seconds to complete')
    return result / (d-1)

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    start = pc()
    
    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(sphere_volume, n, d) for _ in range(np)]
    result = sum([f.result() for f in futures])
    stop = pc()
    print(f'Sphere volume parallel 2 took {stop-start} seconds to complete')
    return result / (d-1)
    
    
def main():
    #Ex1
    '''
    dots = [1000, 10000, 100000, 10000000]
    for n in dots:
        approximate_pi(n)
    
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
  
    n = 100000
    d = 11
    
    start = pc()
    sum = 0
    for y in range (10):
        sum += sphere_volume(n,d)
    average_volume = sum/(d-1)
    stop = pc()
    print(f"Ex3:\nAverage Volume = {average_volume}\nRegular loop time = {stop-start}")
    
    sphere_volume_parallel1(n, d, 10)
'''
    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    
    sphere_volume_parallel2(n, d)

    

if __name__ == '__main__':
	main()
