# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Exercise 1
print('')

num = 2
while num <= 10:
    print(num)
    num += 2
print('Goodbye!')

# Exercise 2
print('')

num = 10
print('Hello!')
while num >= 2:
    print(num)
    num -= 2

# Exercise 3
print('')
end = 6

x = 0
while end >= 0:
    x += end
    end -= 1
print(x)

# Exercise 4
print('')

for num in range(2, 12, 2):
    print(num)
print('Goodbye!') 

# Exercise 5
print('')

nums = [10,8,6,4,2]
print('Hello!')
for index in range(len(nums)):
    print(nums[index])
    
# Exercixe 6
print('')
end = 8


x = 0
y = end
for index in range(end):
    x = x + y
    y -=1
print(x)