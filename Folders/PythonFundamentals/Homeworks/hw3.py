# Palindrom function
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
palindrome=input('Enter a string :')
print(isPalindrome(palindrome)) 
# Nombre premier
def prime(number):
   
    if number > 1:
       for i in range(2, number):
                if (number % i) == 0:
                            return False
                else:
                            return True
num = int(input("enter a number and we will tell  u if it is a prime :"))
print(prime(num))
# check if a number is in a given range
def isinrange(n,l,p):
  if n in range(l,p):
    print(str(n)+" is in range of ("+str(l)+","+str(p)+")")
  else :
    print("it is not")
a=int(input("enter 3 strings : "))
b=int(input(""))
c=int(input(""))
isinrange(a,b,c)
# calculate the factorial of a number
# Calculate the factorial of a number
def facto(n):
  factorial=1
  if n == 0:
    return 1
  elif n==1:
    return 1
  else : 
    for i in range(1,n + 1):
       factorial = factorial*i
    return factorial
numb=int(input("enter a number to calculate it's facotiral : "))
facto(numb)
# reverse a string
def reversed_string(text):
     result = ""
     index = len(text) - 1
     while index >= 0:
         result += text[index]
         index -= 1
     return result

txt=input("enter a string")
reversed_string(txt)
# sum elements of a list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((5,6,3,4)))
# max of 3 elements
def max(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c :
    return b
  else :
    return c
max(2,5,6)