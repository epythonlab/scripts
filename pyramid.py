"""Python Challenge
    Print Pyramid Pattern
"""
def pyramid(n):
    for i in range(n):
        # print the first
        # i rows
        for j in range(n-i-1):
            print(" ", end="")
        # Print the asterics for the 
        # current row
        for j in range(2*i+1):
            print("*", end="")
        
        print() # print newline

# call function
pyramid(5)



