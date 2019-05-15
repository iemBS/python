Multi-dimensional lists: Because Python arrays are actually lists, you are allowed to have jagged arrays. Multi-dimensional lists are just lists of lists:
a=[[0,1,2],[3,4,5]]
print a[1]
-> [3, 4, 5]
s = ["Lee", "Walsh", "Roberson"]
s2 = ["Williams", "Redick", "Ewing", "Dockery"]
s3 = [s, s2]
print s3[1][2]
-> Ewing
