import sys

try :
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")
    firstNumber = float(first)
    secondNumber = float(second)
    result = firstNumber / secondNumber
    print(first+" / "+second+" = "+str(result))
except ZeroDivisionError:
        print("The Answer is Infinity")
except :
        error = sys.exc_info()[0]
        print(error)