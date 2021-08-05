# The goal of this program is to practice Python constructs

def sumTwo(a,b):

   c = a + b

   return c

x = sumTwo(3,5)

print(x)

#how to comment

def getNumber():
   
   #symbols = input("Enter a digit: ")
  number = 0  #int
  answer = ""  #string
  symbols = input("Enter a digit: ")
  while number >= 0:
    answer += symbols
    symbols = input("Enter a digit: ")
    number = int(symbols)
  return answer

print (getNumber())



  
