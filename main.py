

# Step 1

def sumTwo(a,b):

   c = a + b

   return c

x = sumTwo(3,5)

print(x)

# Step 2

def getNumber():
  answer = ""  
  symbols = input("Enter a digit: ")
  number = int(symbols)
  while number >= 0:
    answer += symbols
    symbols = input("Enter a digit: ")
    number = int(symbols)
  return answer

print (getNumber())


# Step 3
def sumDigits(x):
    #
    far_right = x % 10 #furthest right digit
    print("Far right: " + str(far_right))
    left_number = x // 10
    print("Left number: " + str(left_number))
    answer = 0
    while left_number > 0: 
      answer += far_right
      print("answer: " + str(answer))
      far_right = left_number % 10 
      left_number = left_number // 10
    answer += far_right
    return answer

print(sumDigits(588))


def sumDigits(x):
  far_right = x%10
  left_nums = x//10
   while left_number > 0:
      answer = far_right + sumDigits(left_nums)
  return answer
print(sumDigits(588))