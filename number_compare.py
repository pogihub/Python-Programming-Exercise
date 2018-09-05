print("****************************************************")
print("    Welcome to Number Comparison Program"            )
print("****************************************************")
print("")
input_number = 0
name = input("What is your Name?")
print("Hello",name)
print("")
print("This is program will automatically repeat. To End Program type <<exit>> when asked Enter a Number:")
print("")
number_compare = input("Enter a number to compare:")
while (input_number != "exit"):
  input_number = input("Enter a Number:")
  if (input_number < number_compare):
    print(input_number,"is less than",number_compare)
    print("")
  elif (input_number == number_compare):
    print(input_number,"is equal to",number_compare)
    print("")
  else:
    print(input_number,"is greater than",number_compare)  
    print("")
print("GAME OVER. Thank you for using this Program")\