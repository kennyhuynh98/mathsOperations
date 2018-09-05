def Derivative():
    termList = list() # For calculating derivative
    termList = list() # For dislpaying first equation.
    userEquation = list()
    derivative = list()
    n = int(input("Input a single variable polynomial power value (eg. 3 - cubic): "))
    for i in range(n + 1):
        if i != n:
            termList.append(int(input("Please enter numeric coefficient of the x^{0} term: ".format(n - i))))
        else:
            termList.append(int(input("Please enter the numeric value of the constant: ")))

    counter = 0
    for i in range(n + 1):
        if termList[i] > 0 & counter == 0:
            userEquation.append("{0}x^{1}".format(termList[i], n - i))
            counter += 1
            continue
        if i < n - 1:
            if termList[i] > 0:
                userEquation.append("+{0}x^{1}".format(termList[i], n - i))
            elif termList[i] < 0:
                userEquation.append("-{0}x^{1}".format(termList[i], n - i))
        elif i == n - 1:
            if termList[i] > 0:
                userEquation.append("+{0}x".format(termList[i]))
            elif termList[i] < 0:
                userEquation.append("-{0}x".format(termList[i]))
        else:
            if termList[i] > 0:
                userEquation.append("+{0}".format(termList[i]))
            elif termList[i] < 0:
                userEquation.append("-{0}".format(termList[i]))


        if i < n:
            if termList[i] > 0 & counter == 0:
                derivative.append("{0}x^{1}".format(termList[i]*(n - i), n - i - 1))
                counter += 1
                continue
            if i < n - 2:
                if termList[i] > 0:
                    derivative.append("+{0}x^{1}".format(termList[i]*(n - i), n - i - 1))
                elif termList[i] < 0:
                    derivative.append("-{0}x^{1}".format(termList[i]*(n - i), n - i - 1))
            elif i == n - 2:
                if termList[i] > 0:
                    derivative.append("+{0}x".format(termList[i]*(n - i)))
                elif termList[i] < 0:
                    derivative.append("-{0}x".format(termList[i]*(n - i)))
            else:
                if termList[i] > 0:
                    derivative.append("+{0}".format(termList[i]*(n - i)))
                elif termList[i] < 0:
                    derivative.append("-{0}".format(termList[i]*(n - i)))

        counter += 1

        
    output = "".join(userEquation)
    outputDeriv = "".join(derivative)
    print("Output: " + output)
    print("Derivative: " + outputDeriv)

Derivative()
