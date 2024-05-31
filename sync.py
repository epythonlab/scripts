# synchronous example

import time

def hello():
    print("hello")
    time.sleep(5) # delay 5 seconds

def world():
    print("world")
    time.sleep(5) # delay 5 seconds

def main():
    # call the functions
    hello()
    world() # this function is executed after the first
    
if __name__ == "__main__":
    main()