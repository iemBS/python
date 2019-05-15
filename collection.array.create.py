zeros creates an array of a specified size containing all zeros:
a = zeros(5) #a=[0 0 0 0 0]
ones similarly creates an array of a certain size containing all ones:
a = ones(5) #a=[1 1 1 1 1]
arange works exactly the same as range, but produces an array instead of a list:
a = arange(10,0,-2) #a = [10 8 6 4 2] And finally, array can be used to convert a list to an array. For instance, when reading from a file, you can create an empty list and take advantage of the append command and lists not having a fixed size. Then once the data is all in the list, you can convert it to an array:
a = [1, 3, 9] #create a list and append it
a.append(3)
a.append(5)
print a
-> [1, 3, 9, 3, 5]
a = array(a)
print a
-> [1 3 9 3 5]
