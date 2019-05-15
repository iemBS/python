

Initializing a 2D list

While this can be done safely to initialize a list:

lst = [0] * 3

The same trick won’t work for a 2D list (list of lists):

>>> lst_2d = [[0] * 3] * 3
>>> lst_2d
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> lst_2d[0][0] = 5
>>> lst_2d
[[5, 0, 0], [5, 0, 0], [5, 0, 0]]

The operator * duplicates its operands, and duplicated lists constructed with [] point to the same list. The correct way to do this is:

>>> lst_2d = [[0] * 3 for i in xrange(3)]
>>> lst_2d
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> lst_2d[0][0] = 5
>>> lst_2d
[[5, 0, 0], [0, 0, 0], [0, 0, 0]]

