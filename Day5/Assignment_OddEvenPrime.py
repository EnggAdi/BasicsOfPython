userInput1=int(input("Enter input1"))
userInput2=int(input("Enter input2"))

if type(userInput1) == int and type(userInput2)==int:
    print("Is a number")
else:
    print("Not a number")


#Case1 : Both are Even Numbers
if (userInput1%2 == 0 and userInput2%2 == 0):
    print(userInput1, " and ", userInput2, " are Even Numbers.")
    sumOfNumbers = (userInput1 + userInput2)
    print("Sum of the Two Even Numbers=", sumOfNumbers)
# Case 2:Both are Odd Numbers    
elif (userInput1%2 != 0 and userInput2 != 0):
    print(userInput1, " and ", userInput2, " are Odd Numbers.")
    productOfNumbers = (userInput1 * userInput2)
    print("Product of the Two Odd Numbers=", productOfNumbers)
    
#Case 3: Number 1 is Even and Number 2 is Odd
elif (userInput1%2 == 0 and userInput2 != 0):
    print(userInput1, "is an Even Number and ", userInput2, " is an Odd Number.")

#case 4: Number 1 is Odd and Number 2 is Even
elif (userInput1%2 != 0 and userInput2 == 0):
    print(userInput1, "is an Odd Number and ", userInput2, " is an Even Number.")
    
#If a Number among the two Numbers is prime or not

if (userInput1 > 1):
    for index in range(2, userInput1):
        if(userInput1 % index != 0):
            print(userInput1, "is a Prime Number.")
            break
        else:
            print(userInput1, "is not a Prime Number.")
            break
        
else:
    print(userInput1, "is not a Prime Number.")