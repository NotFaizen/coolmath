import math, requests,os

base = os.getenv("api_url")
key = os.getenv("api_key")
Sum = sum
def iseven(num:int)->bool:
  """
  Check if {num} is even or not\n
  @params\n
    \tnum {int} The number to check for even\n
  @return\n
    \tis_even {bool} True if {num} is even and False if not\n
  @example\n
   \>>> coolmath.is_even(20)\n
    \tTrue
  \>>> coolmath.is_even(31)\n
    \tFalse

  """
  if num % 2 == 0: 
    return True 
  else: 
    return False

def isodd(num:int)->bool:
  """
  Check if num is odd or not\n
  @params\n
    num {int} The number to check for odd\n
  @return\n
    is_odd {bool} True if {num} is odd and False if not\n
  @example\n
    \>>> coolmath.is_odd(69)\n
      \tTrue\n
    \>>> coolmath.is_odd(420)\n
      \tFalse
  """
  return True if (num % 2) != 0 else False 

def sum(*nums)->float:
  """
  Returns the sum of all the numbers passed in {nums}\n
  @params\n
    \tnums {float_tuple} The numbers to add\n
  @return\n
    \tsum {float} The sum of {nums}\n
  @example\n
    \>>> coolmath.sum(2,2)\n
      \t4\n
    \>>> coolmath.sum(2.65,1.25)\n
      \t3.9\n
    \>>> coolmath.sum(1,2,3)\n
      \t6
  """
  total=0
  for num in nums:
    total+=num
  return total

def sub(*nums)->float:
  """
  Returns the subtraction of all the numbers passed in {nums}\n
  @params\n
    \tnums {float_tuple} The numbers to subtract\n
  @return\n
    \tsub {float} The subtraction of {nums}\n
  @example\n
    \>>> coolmath.sub(2,2)\n
      \t1.4\n
    \>>> coolmath.sub(2.65,1.25)\n
      \t3.9\n
    \>>> coolmath.sub(1,2,3)\n
      \t-4
  """
  total=0
  for num in nums:
    total-=num
  return total

def multi(*nums): #multiply two numbers
  """
  Returns the multiplication of all the numbers passed in {nums}\n
  @params\n
    \tnums {float_tuple} The numbers to multiply\n
  @return\n
    \tmulti {float} The multiplication of {nums}\n
  @example\n
    \>>> coolmath.multi(2,2)\n
      \t4\n
    \>>> coolmath.multi(2.65,1.25)\n
      \t3.3125\n
    \>>> coolmath.multi(1,2,3)\n
      \t6
  """
  total=1
  for num in nums:
    total*=num
  return total

def divide(*nums):
  """
  Returns the division of all the numbers passed in {nums}\n
  @params\n
    \tnums {float_tuple} The numbers to divide\n
  @return\n
    \tdivide {float} The division of {nums}\n
  @example\n
    \>>> coolmath.divide(2,2)\n
      \t1\n
    \>>> coolmath.divide(1,2)\n
      \t0.5\n
    \>>> coolmath.divide(1,2,3)\n
      \t6
  """
  total=1
  for num in nums:
    total = 1/total/num
  return total


def modulo(x:int,y:int)->int:
  """
  Returns the remainder of the division between {x} and {y}\n
  @params\n
    \tx {int} The number to divide by {y}\n
    \ty {int} The number diving with {x}\n
  @return\n
    \tmodulo {int} The remainder of the division between {x} and {y}\n
  @example\n
    \>>> coolmath.modulo(2,2)\n
      \t0\n
    \>>> coolmath.modulo(1,2)\n
      \t1\n
  """
  return x % y
def sqr(num: float): #find the square power of a number
  """
  Returns the square power of {num}\n
  @params\n
    \tnum {float} The number to raise by 2\n
  @return\n
    \tsqr {float} The square power of {num}\n
  @example\n
    \>>> coolmath.modulo(2,2)\n
      \t0\n
    \>>> coolmath.divide(1,2)\n
      \t1\n
  """
  return num*num

def isprime(num): # check if `num` is prime or not
    '''Returns True if number is prime, and False if not'''
    if num < 2: 
         return False;
    if num % 2 == 0:             
         return num == 2  # return False
    k = 3
    while k*k <= num:
         if num % k == 0:
             return False
         k += 2
    return True

def pow(num1,num2):
  '''This will return num1 to the power num2.
  
  For example coolmath.pow(2,3) would return 8'''
  return num1 ** num2

def average(*nums):
  return Sum(nums)/len(nums)

def sqrt(num:int):
  return num**1/2

def roots(a:float,b:float,c:float):
  pos = (-b+(math.sqrt((b**2) - 4*a*c)))/2*a
  neg = (-b - (math.sqrt((b**2) - 4*a*c))) / 2*a
  return tuple((pos,neg))

def isNaN(num:float):
  res = requests.get(f"{base}&num={num}")
  data = res.json()
  return bool(data["isNaN"])
