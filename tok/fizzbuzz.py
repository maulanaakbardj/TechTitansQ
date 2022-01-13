# input = 15
def fizzBuzz(n):
    # Write your code here
    for i in range (1, n+1) :
        string = ""
        if i % 3 == 0:
            string = string + "Fizz"
        if i % 5 == 0:
            string = string + "Buzz"
        if i % 5 != 0 and i % 3 != 0:
            string = string + str(i)
        print(string)
