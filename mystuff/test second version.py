fruit = ["apple","orange","banana","cherry"]
numlist = [6,7]
newlist = fruit + numlist
zeros = [0] * 4

zeros[1] = fruit
print("zeros =", zeros)

#zeros[1][2] = numlist
zeros[2] = numlist
print("zeros =", zeros)


#('zeros =', [0, ['apple', 'orange', 'banana', 'cherry'], 0, 0])
#('zeros =', [0, ['apple', 'orange', [6, 7], 'cherry'], 0, 0])