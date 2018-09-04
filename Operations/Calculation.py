import BasicOperations

class Calculation():

    quit = False

    while quit != True:
        print("Operation select:")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n")
        print("Press 'q' to quit.\n")
        operation = input("Please select an operation: ")

        result = 0
        average = 0

        if operation == '1':
            result, average = BasicOperations.Addition()
            print("\nAddition result: %d\nAverage: %.2f\n" % (result, average))
        elif operation == '2':
            result = BasicOperations.Subtraction()
            print("\nSubtraction result: %d\n" % (result))
        elif operation == '3':
            result = BasicOperations.Multiplication()
            print("\nMultiplication result: %d\n" % (result))
        elif operation == '4':
            result = BasicOperations.Division()
            print("\nDivision result: %.2f\n" % (result))
        elif operation == '5':
            result = BasicOperations.Exponentiation()
            print("\nExponentiation result: %d\n" % result)
        elif operation == 'q':
            print("\nTerminating process...")
            quit = True