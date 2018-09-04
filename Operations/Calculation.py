import BasicOperations
class Calculation():

    numList = list()
    quit = False
    while quit != True:
        print("Operation select:")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation")
        operation = int(input("Please select an operation: "))

    
        num  = int(input("Enter amount of numbers to evaluate: "))

        for x in range(num):
            numToAdd = int(input("Enter a number(#" + str(x) + "): "))
            numList.append(numToAdd)

        if operation == 1:
            print(BasicOperations.Addition(numList))