from turtle import *
import math

# calculates nCr
def nCr(n,r):
  if n >= r and r >= 0:
    return math.factorial(n) // (math.factorial(r)*math.factorial(n-r))


# generatesPascal's triangle in the form of a list of lists,
#   where the inner list contains the numbers in each column and
#   the outer list contains each row
def generatePascal(rowMax):
  outerList = [[1]]
  for n in range(2,rowMax+1):
    innerList = []
    for k in range(0,n+1):
      print(n, ", ", k)
      innerList.append(nCr(n,k))
    outerList.append(innerList)
  return outerList


# print the result of generatePascal() - for testing purposes
def testGeneratePascal(rowMax):
  triangle = generatePascal(rowMax)
  for eachRow in triangle:
    print(eachRow)

testGeneratePascal(5)
