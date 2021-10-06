#Callista Dominique with Nadhiva
#fist option
n = 100

def this_is_result():
  result = formula1 - formula2
  print("b - a : " + str(result))

# 1^2 + 2^2 + 3^2....+ n^2
formula1 = ((2*n**3) + (3*n**2) + (n)) / 6 
# (1+2+3....)^2
formula2 = ((n**4) + (2*n**3) + (n**2)) / 4 

print("a : " + str(formula1))
print("b : " + str(formula2))
this_is_result()

#second option
a =int( input("Enter a Number: "))
# enter the number that we want to calculate

x = ((2*a**3) + (3*a**2) + (a)) / 6 
#x is x=(a^2+b^2+.....+z^2)
y = ((a**4) + (2*a**3) + (a**2)) / 4 
#y is y=(a+b+......+z)^2
print("x : " + str(x))
print("y : " + str(y))

b = x - y
print("x - y : " + str(b))

