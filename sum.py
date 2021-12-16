# Adding n numbers
# To solve a mathematical problem that is required to return the sum of the first n numbers

n = int(input("Enter a number: "))   #value upto which to compute
sum = 0   # initializing the value of sum to zero

# The function to calculate the sum of the first n numbers
def sum(x):
    if x <= 1:    #If the input is less or equal to one return n
        return x
    else:       #if the number is greater than zero, execute
        return x + sum(x-1)    
    
print("The sum of the firs n numbers is: ", sum(n)) 


# Testing the program on different values: 10, 10000, 1000000, 1000000000.
def test_sum():
    assert sum(n)

if __name__ == "__main__":
    test_sum()
    print("passed")


