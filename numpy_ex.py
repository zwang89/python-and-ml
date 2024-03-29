# this is the way py file to excise numpy
import numpy as np

# numpy array

my_list =[1,2,3]
arr = np.array(my_list)
print(arr)

np.arange(0,10)

#create a numpy array

np.array(np.arange(0,10,2))

np.zeros((5,4))

arr = np.linspace(0,50,100)

# identity matrix
np.eye(4)

# random generated by numpy
np.random.rand(5,5)
# normal distribution
np.random.randn(2)

np.random.randint(2,20000,30)

# reshapte the number
arr.argmax()

# numpy indexing
arr = np.arange(0,10)
print(arr)
arr[8]
arr[2:]

arr[0:2] =100
# if array without using .copy() methods, the array will change
arr_2d = np.array([[2,4,3] ,[120,5,6],[2,7,5]])

arr_2d[:,2]

# conditional slicing
arr = np.arange(1,11)
print(arr)

arr[arr>2]

arr[arr<2]

arr_2d = np.arange(50).reshape(5,10)
arr_2d[1:5,4:7]


# numpy operation

arr = np.arange(0, 11)
arr + arr


