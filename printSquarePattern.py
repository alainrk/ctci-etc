'''
Write a program that prints the following pattern

5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''

def getMatrix (n):
  if (n == 1):
    return [[1]]
  sub = getMatrix(n-1)
  for row in sub:
    row.insert(0, n)
    row.append(n)
  sub.insert(0, [n for x in range(n * 2 -1)])
  sub.append([n for x in range(n * 2 -1)])
  return sub

def printSquare(n):
  res = getMatrix(n)
  for row in res:
    print(" ".join(map(lambda x: str(x), row)))

printSquare(5)