"""
Break.
    For example, the following code will print 
    the numbers from 1 to 5, 
    but it will break out of the loop if the number is 3:
"""

for i, num in enumerate(range(1,6)):
    if num == 3:
        break
    print(f'{i}. {num}')

# 0. 1
# 1. 2



"""
Continue...
For example, 
the following code will print 
the even numbers from 1 to 10, 

But the if statement checks if the current number is even.
If it is even, the print statement prints the number. 
If it is not even, 
the continue statement skips the current iteration of the loop 
and goes to the next iteration.:
"""
for i, num in enumerate(range(2, 11)):
    if num % 2 == 0:
        print(f'{i}. {num}')
    else:
        break