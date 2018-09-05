#Program excercise of function return

#September 5, 2018


#Start of Function

def add(x,y):
    return  x + y     


def multiply(x,y):
    return  x * y  


def div(x,y):
    return  x / y  

#End of Function
      
      
  

print("Welcome to Pogi's Calculator")

print("")

x = input("Enter First Number: ")

y = input("Enter Second Number: ")

x = int(x)
y = int(y)
print("")


print("****************************")

sum = add(x,y)

print("SUM:",sum)

multi = multiply(x,y)

print("MULTIPLY:",multi)

divr = div(x,y)

print("DIVIDE:",divr)

print("****************************")