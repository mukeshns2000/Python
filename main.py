# Python code to demonstrate naive method
# to compute factorial
n = 5
fact = 5
 
for i in range(1, n+1):
    fact = fact * i
 
print("The factorial of 5 is : ", end="")
print(fact)