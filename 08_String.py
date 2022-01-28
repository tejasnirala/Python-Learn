mystr = "My_name_is_Tejas"
print(mystr)
print(len(mystr)) # It gives length of mystr

'''
Neagtive Index ->   -16  -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
--------------------------------------------------------------------------------------------------
Given String is ->   M    y    _    n    a    m    e    _    i    s    _    T    e    j    a    s
--------------------------------------------------------------------------------------------------
Normal Index  ->     0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
'''

# String Slicing
print(mystr[0:5]) # 5th index is excluded
print(mystr[:5]) # It's same as above
print(mystr[0:]) # It gives whole string
print(mystr[:]) # It's same as above (line number - 16)
print(mystr[0:5:2]) # It gives string upto index 5 but having index difference 2
print(mystr[::]) # By default the it will take the value 0:16:1 resepectively
print(mystr[::5590]) # It will give only 'M' because after print 'M' it will jump to index difference 5590

# These two are same (From the above figure -5 is equivalent to 11)
print(mystr[-5:])
print(mystr[11:])

# We use negative number at third colon in order to reverse the string
print(mystr[::-1])
print(mystr[::-2]) # This will reverse the string and print the string with index difference 2

# To print a selected potion of any string in reverse order we give the value of first and second colon in reverse manner
print(mystr[15:10:-1])


