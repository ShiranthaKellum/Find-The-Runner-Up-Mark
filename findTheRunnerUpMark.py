
# This program finds the runne-up (the second large mark from a det of marks)
# Explanation is in the readme file

n = int (input ("Number of elements = "))

list = []                                                   # a list of store marks
newlist = []                                                # another list for store same marks

for i in range (n):                                         # get marks
    x = int (input ("Enter element : "))
    list.append (x)

list.sort ()                                                # sort the list

for i in range (n-1):                                       
    if (list [n-1] == list [i]):
        newlist.append (list [i])                           # insert same marks in to newLis

print (list [n-2-len(newlist)])                             # return the runner-up mark


