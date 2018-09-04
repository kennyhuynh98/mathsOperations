def Addition():
    numList = list()
    result = 0
    average = 0
    counter = 0
    userInput = ""
    while userInput != " ":
        userInput = input("(Input whitespace if you want to continue) Enter a number(#{0}): ".format(counter + 1))
        if userInput is not " ":
            numList.append(int(userInput))
            counter += 1

    for x in numList:
        result += x
    average = result/counter
    return result, average

def Subtraction():
    userInput = int(input("Enter the first number: "))
    userInput2 = int(input("Enter the second number: "))
    result = 0
    result = userInput - userInput2
    return result

def Multiplication():
    numList = list()
    result = 1
    counter = 0
    userInput = ""
    while userInput != " ":
        userInput = input("(Input whitespace if you want to continue) Enter a number(#{0}): ".format(counter + 1))
        if userInput is not " ":
            numList.append(int(userInput))
            counter += 1

    for x in numList:
        result *= x
    return result

def Division():
    userInput = int(input("Enter the first number: "))
    userInput2 = int(input("Enter the second number: "))
    result = 0
    result = userInput/userInput2
    return result

def Exponentiation():
    userInput = int(input("Enter the base number: "))
    userInput2 = int(input("Enter the exponent: "))
    result = 0
    result = userInput ** userInput2
    return result