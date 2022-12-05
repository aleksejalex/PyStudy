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
Hamlet = (True or (not True))  # as 'To be or not to be'


# calling functions, if/else
def shakespeare_says(thought):
    if thought == True:
        return "To be"
    else:  # thought == False
        return "Not to be"


# using functions
print("The answer to Hamlet's question is: " + shakespeare_says(Hamlet))

# lambda functions
# in Python, they are always anonymous: you can call them as var(agrs) (see in printing below),
# but you cannot name them.
x = lambda a, b: a * b
print(x(5, 6))


