# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).
#
# As we know, the result of
# grows really fast with increasing .
#
# Let's do some calculations on very large integers.
#
# Task
# Read four numbers, , , , and ,
# and print the result of .
# Task
#
# Input Format
# Integers , , , and  are given on four
# separate lines, respectively.



#  SAMPLE İNPUT
# 9
# 29
# 7
# 27

a= int(input())
b= int(input())
c= int(input())
d= int(input())

out1 = a**b
out2 = c**d

print(out1 + out2)