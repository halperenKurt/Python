
class calculate():
    def topla(self,number1,number2):
        return number1+number2
    def cıkar(self,number1,number2):
       return number1-number2
    def carp(self,number1,number2):
        return number1*number2
    def bol(self,number1,number2):
        return number1/number2
math = calculate()

print("Operation?")
print("1 : Addition")
print("2 : Extraction")
print("3 : Multiplication")
print("4 : Divide")
option = input("Which operation?")
number1 = int(input("What is the number1?"))
number2 = int(input("What is the number2?"))

if option == '1':
    print("Result = " + str(math.topla(number1,number2)))
elif option == '2':
    print("Result = " + str(math.cıkar(number1,number2)))
elif option == '3':
    print("Result = " + str(math.carp(number1,number2)))
elif option == '4':
    print("Result = " + str(math.bol(number1,number2)))



