'''
Given a random N, write a code to print all
positive number less than N in which all adjacent
digits differ by 1.
'''

def differByOne (arr):
  for i in range(len(arr) - 1):
    if abs(arr[i] - arr[i + 1]) != 1:
      return False
  return True

def adjacent (n):
  res = []
  for x in range(n):
    arr = [int(i) for i in str(x)]
    if (differByOne(arr)):
      res.append(x)
  print("Result for", n, "=", res)
  return res

def test ():
  test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101]
  if adjacent(105) != test:
    print("Error on", test)
    return False
  test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101, 121, 123]
  if adjacent(135) != test:
    print("Error on", test)
    return False
  test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  if adjacent(10) != test:
    print("Error on", test)
    return False
  test = [0, 1, 2, 3, 4]
  if adjacent(5) != test:
    print("Error on", test)
    return False
  test = []
  if adjacent(0) != test:
    print("Error on", test)
    return False
  return True

print(test())

# print(differByOne([1, 0, 5]))
# print(differByOne([1, 0, 1]))
# print(differByOne([9, 8]))
# print(differByOne([9, 9]))
# print(differByOne([1]))