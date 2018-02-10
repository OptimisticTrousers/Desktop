import math

while True:
    number = int(input("Enter number to find squareroot: "))
    result = math.sqrt(number)
    print("The square root of " + str(number) + "is: " + str(result))
    user_input=("Do you want to contiune: ")
    if(user_input=="no"):
        break
      
end=input("")
