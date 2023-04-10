#this is a basic python calculator

#this function multiplies numbers
def mult(num1, num2):
    print(num1 * num2)


#this function adds two numbers
def add(num1, num2):
    print(num1+num2)
    

#this function subtracts two numbers
def subtract(num1, num2):
    print(num1 - num2)


#this function divides two numbers
def divide(num1, num2):
    print(num1/num2)

#this function computes factorial
def factorail(num1):
    if(num1 <0):
        return 0
    elif(num1==0 or num1==1):
        return 1
    else:
        fact = 1
        while(num1>1):
            fact*=num1
            num1 -=1

        print(fact)


#choose operator
operators = ['*','+','/','-','!' '\n']
print('choose any operator from the list \n')
#print("'*' for multiplication, '+' for addition , '!' for factorail, '/' for division and '-' for subtraction \n")

#computation done in proper
#for value in operators:
 #   print(value)
operator = input('enter an operator: ')
num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))
if(operator=='*'):
    mult(num1,num2)
elif(operator == '+'):
    add(num1, num2)
elif(operator =='-'):
    subtract(num1, num2)
elif(operator =='/'):
    divide(num1,num2)
elif(operator == "!"):
    num = int(input("enter number to compute fact: "))
    factorail(num)
else:
    print('no such operator!!!!')
    
    exit
    
    