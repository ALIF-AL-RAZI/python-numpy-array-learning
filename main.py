import numpy as np

# arr= np.array([1,2,3,4,5,6])
#
# print(arr)
#
# print(type(arr))
#
# print(np.__version__)


# arr0D = np.array(56)
# arr1D = np.array([1,2,3,6,7,8,4])
# arr2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print('\n\n',arr0D)
# print('\n\n',arr1D)
# print('\n\n',arr2D)
#print('\n\n',arr3D)

#--------------------------array indexing----------------------


# print(arr1D[1])
#
# print(arr2D[2,1])
#
# print(arr2D[2,-2])  # negetaive index. count from last
#
# print(arr3D[0,1,2])




#----------------------array slicing-------------------------



# print(arr1D[1:5]) #    np.array([1,2,3,6,7,8,4])      outcome[2 3 6 7]
#
# print(arr1D[2:]) #outcome [3 6 7 8 4]
#
# print(arr1D[:4])  #[1 2 3 6]
#
# print((arr1D[-3:-1]))  #Slice from the index 3 from the end to index 1 from the end. outcome [7 8]
#
# print(arr2D[1:3,1:3])
#
#
#
# #step slice
# print(arr1D[1:4:3])




#---------------data type ----------
# arr = np.array([1, 25, 3, 4], dtype='S')
# arrw = np.array([1,5,7,3,6,4], dtype='c')
# print(arrw)
#
# print(arr)
#
#
# print(arr.dtype)
#
#
# arr = np.array([1, 0, 3])
#
# newarr = arr.astype(bool)
#
#
#
#
# print(newarr)
# print(newarr.dtype)



#---------copy vs veiw--------

#
# arr = np.array([1,5,8,3,6,2,4,6])
#
# x = arr.copy()
#
# arr[6]=67  #original change
#
# print(arr)  #[ 1  5  8  3  6  2 67  6]  #original change
# print(x)   #[1 5 8 3 6 2 4 6]


# arrView = np.array([3,6,3,6,8,2,6,8,9,3,8,4,7])
# view = arrView.view()
# arrView[6] = 456  #both change
#
# print(arrView)  #[  3   6   3   6   8   2 456   8   9   3   8   4   7]   #both change
# print(view)    #[  3   6   3   6   8   2 456   8   9   3   8   4   7]
#
#
#
# arrView1 = np.array([3,6,3,6,8,2,6,8,9,3,8,4,7])
# view1 = arrView.view()
# view1[6] = 478   #original no change
#
# print(arrView1)  #[3 6 3 6 8 2 6 8 9 3 8 4 7]  #original no change
# print(view1)    #[  3   6   3   6   8   2 456   8   9   3   8   4   7]




# arr = np.array([1, 2, 3, 4, 5])
#
# x = arr.copy()
# y = arr.view()
#
# print(x.base)  #show None if the array owns the data.
# print(y.base)   #show original array




#------------array shape -------

#
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# print(arr.shape) # show (2,4) 2 rows 4 columns
#
# print(arr3D.shape)


#--------------array reshape-------------- 1d to 2d, 2d to 1d, 2d to 3d ,.......



# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newArr = arr.reshape(2,3,2)
#
# print(newArr)






#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newArr = arr.reshape(3,3)
#
# print(newArr)  #show error as 8 elements

#print(arr.reshape(2, 4).base)    #[1 2 3 4 5 6 7 8]





# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# newarr = arr.reshape(-1)
#
# print(newarr)    # [1 2 3 4 5 6]







#------------------------------Iterating Arrays-------------------------------




# arr = np.array([1,2,3,4,5,6,7])
#
# for x in arr:
#     print(x)



#arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# for x in arr2:
#     for y in x:
#         print(y)




# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr3:
#   print('\n',x)   #print 2 different 2d array






#arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr3:
#   for y in x:
#     for z in y:
#       print(z)






#arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr2):                #same as x y z iteration
#     print(x)






# arr = np.array([1, 2, 3])
#
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):    #changing datatype.. cap S is for string
#     print(x)






# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
#
# for x in np.nditer(arr[:, ::2]):   #skipping 1 element   ,,,, 3 for skipping 3 elements
#     print(x)





# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# for id, x in np.ndenumerate(arr):                    #enumerate for printing both position of element and elements
#   print(id, x)



#---------------------------------Joining NumPy Arrays-----------------------------



# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
#
# arr = np.concatenate((arr1,arr2))    #[1 2 3 4 5 6]
#
# print(arr)





#joining 2d array


# arr1 = np.array([[1, 2], [3, 4]])
#
# arr2 = np.array([[5, 6], [7, 8]])
#
# arr = np.concatenate((arr2,arr1), axis=1)   #axis= 1 is 2d array
#
# print(arr)




#Joining Arrays Using Stack Functions


# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.stack((arr1, arr2), axis=1)            # [[1 4]
#                                                 #  [2 5]
# print(arr)                                      #  [3 6]]





#Stacking Along Rows (hstack)

# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.hstack((arr1, arr2))    #[1 2 3 4 5 6]
#
# print(arr)






#Stacking Along column (vstack)

# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.vstack((arr1, arr2))     #  [[1 2 3]
#                                   #   [4 5 6]]
# print(arr)



#Stacking Along Height (depth)


# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.dstack((arr1, arr2))     #  [[[1 4]
#                                   #   [2 5]
# print(arr)                        #   [3 6]]]




#------------------------Splitting NumPy Arrays--------------------


# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr,3)   #Split the array in 3 parts
#
# print(newarr)              #[array([1, 2]), array([3, 4]), array([5, 6])]
#
# print(newarr[0])  #[1 2]
# print(newarr[1])  #[3 4]
# print(newarr[2])  #[5 6]





# Split the 2-D array into three 2-D arrays


# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
#
# newarr = np.array_split(arr, 3)            #        [array([[1, 2],
#                                            #                 [3, 4]]), array([[5, 6],
# print(newarr)                              #                                  [7, 8]]), array([[ 9, 10],
                                             #                                                   [11, 12]])]





#----------------search(where)-------------

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 4 )
# print(x)  #print indexes
#
# y= np.where(arr%2 == 0)   # print even element indexes
#
# print(y)
#
#
# z= np.where(arr%2 == 1)   # print odd element indexes
#
# print(z)






#------------------------------------sort---------------------------

# arr = np.array([3, 2, 0, 1])
#
# print(np.sort(arr))    #[0 1 2 3]
#
#
#
# arr = np.array(['banana', 'cherry', 'apple'])
#
# print(np.sort(arr))   #['apple' 'banana' 'cherry']
#
#
#
# arr = np.array([True, False, True])
#
# print(np.sort(arr))     #[False  True  True]
#
#
#
#
# #Sorting a 2-D Array
#
# arr = np.array([[3, 2, 4], [5, 0, 1]])
#
# print(np.sort(arr))     #[[2 3 4]
#                          #[0 1 5]]











#-------------------------------------NumPy Filter Array---------------------------------




# arr = np.array([41, 42, 43, 44])
#
# x = [True , False, False, True]
#
# newarr = arr[x]
#
# print(newarr)        #[41 44]




# arr = np.array([41, 42, 43,44])
#
# filter_arr =[]
#
# for element in arr:
#     if element > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
#
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)