first = input("Enter the first number: ")
second = input("Enter the second number: ")

firstNumber = float(first)
secondNumber = float(second)
try :
     result = firstNumber / secondNumber
     print(first+" / "+second+" = "+str(result))
except ZeroDivisionError:
        print("The Answer is Infinity")