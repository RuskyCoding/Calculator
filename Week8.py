import math

print("Welcome to Calculator!")
print(" ")
#This 'def' outlines how the calculations are performed. If an invalid function is chosen the user is prompted to choose again.
def calculate(num1,num2,operation):
  if operation == '+':
    calculation_result = num1+num2
  elif operation == '-':
    calculation_result = num1-num2  
  elif operation == '*':
    calculation_result = num1*num2  
  elif operation == '/':
    calculation_result = num1/num2
  elif operation == '**': 
    calculation_result = num1**num2
  elif operation == '%': 
    calculation_result = num1%num2
  else:
    print ("You need to use a valid function. Please try again.")
  return calculation_result
#while True statement to allow the calculator to repeat at the request of the user.
while True:
  num1 = float(input('Please enter your first number:'))
  while True:
#Outline the operation to be chosen by the user, repeating if they choose and invalid value (add, sub, mult, div or remainder)
     operation = input("What function would you like to perform? Add (+), Sub (-), Mult (*), Div (/), Pow (**) or Mod (%): ")
     if operation == '+':
      break
     elif operation == '-':
      break
     elif operation == '*':
      break
     elif operation == '/':
      break
#Added Power operation to calculate num1 to the power of num2 and print result.
     elif operation == '**':
      break
#Added Modulo operation to calculate remainder from division of num1 and num2.
     elif operation == '%':
      break
     else:
      print ("You need to use a valid function. Please try again.")
#Second figure input by the user, with a while True to prevent the user using 0 as a value, preventing the 'divide 0' error.
  while True:
    num2 = float(input('What is your second number:'))
    if num2 != 0:
      break
    else:
      print('0 is not a valid option. Please try again...')
  calculation_result=calculate(num1,num2,operation)
  print("Your sum of ",num1,operation,num2,"=",calculation_result)
#Closing of the while True from line 20. Allows the loop of the calculator or exit the program based on user input.
  next_calculation = (input("Please type 'exit' to leave, else press any key to continue: "))
#If the user types 'exit', the below is printed and the calculator ends. 
  if next_calculation == "exit":
    print("Thank you for using the Calculator... Goodbye.")
    break
  else:
    next_calculation != "exit"
    print("Starting another calculation...")   
