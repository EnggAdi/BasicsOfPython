num1=4
num2=0
for index in range(num2,num1):
    for index1 in range(num2,index+1):
        print("*",end="")
    print("")

for index2 in range(num1, num2,-1):
    for index3 in range(num2,index2-1):
        print("*",end="")
    print("")