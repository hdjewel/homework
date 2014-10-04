fruit = ["apple","orange","banana","cherry"]
numlist = [6,7]
newlist = fruit + numlist
zeros = [0] * 4

#This creates a table "fruit" within the second element of zeros (zeros[1]).
zeros[1] = fruit
print("zeros =", zeros)

#This creates a table "numlist" within the third element of the second element of 
#zeros (zeros[1][2]).  In other words a table within a table within table.  To
#access the element with the value of 7, you would code zeros[1][2][1]
zeros[1][2] = numlist
print("zeros =", zeros)

print("zeros =", zeros[1][2][1])

zeros[2] = numlist
print("zeros =", zeros)


#('zeros =', [0, ['apple', 'orange', 'banana', 'cherry'], 0, 0])
#('zeros =', [0, ['apple', 'orange', [6, 7], 'cherry'], 0, 0])
#('zeros =', [0, ['apple', 'orange', 'banana', 'cherry'], [6, 7], 0])