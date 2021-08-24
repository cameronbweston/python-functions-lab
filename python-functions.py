#1 sum_ to
def sum_to(n):
  sum = 0
  for i in range(n):
    sum += i+1
  return sum

# test = sum_to(6)
# print(f'sum_to: {test}')

def largest(list):
  max = 0
  for i in list:
    if i > max:
      max = i
  return max

# testMax = largest([1,45,500,3,63,27,15])
# print(f'largest is: {testMax}')

def occurances(a, b):
  return a.count(b, 0, len(a)-1)

# testStrings = occurances('jolly green giant', 'g')
# print(f'Substrings b inside a: {testStrings}')

def product(*args):
  product = 1;
  for i in args:
    product *= i
  return product

# testp = product(1,2,3,4,5)
# print(f'test product: {testp}')