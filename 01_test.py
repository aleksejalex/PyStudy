"""
01 - test file

Just to test if the project and the GitHub are set up correctly.


"""

from studyLib import *

# print a concatenation of strings, access library through shortcut
print("pi is >> " + str(np.pi))

# for loop, TicToc usage
tic()
for i in range(600):
    print("i = " + str(i))

toc()

# booleans
shakespeare = (True or (not True))  # as 'To be or not to be'
print("The Hamlet's question has simple answer: " + str(shakespeare))



