from turtle import *
import math

COLOR_LIST = ['red', 'blue', 'green', 'yellow', 'purple', \
              'black', 'green4', 'blue4', 'DeepSkyBlue', 'violet']

# calculates nCr
def nCr(n,r):
  if n >= r and r >= 0:
    return math.factorial(n) // (math.factorial(r)*math.factorial(n-r))


# generatesPascal's triangle in the form of a list of lists,
#   where the inner list contains the numbers in each column and
#   the outer list contains each row
def genModPascal(mod, rowMax):
  outerList = []
  for n in range(0,rowMax+1):
    innerList = []
    for k in range(0,n+1):
      ##print(n, ", ", k)
      innerList.append(nCr(n,k) % mod)
    outerList.append(innerList)
  return outerList


# print the result of generatePascal() - for testing purposes
def testGeneratePascal(mod, rowMax):
  triangle = genModPascal(mod, rowMax)
  t = Turtle()
  t.ht()
  for eachRow in triangle:
    ##print(eachRow)
    drawRow(t, eachRow)
    

# draws the given row with the turtle
# @param t - a turtle object
# @param row - a list to draw 
# note: position the turtle in the upper left corner of the desired row, facing east
#       the turtle ends just below the lower left corner, facing the same way
def drawRow(t, row):
  l = len(row)
  if l == 1:
    print("l=0")
    for stOffset in (1,0):
      t.color(COLOR_LIST[row[0]])
      t.pu()
      t.fd(stOffset)
      t.pd()
      t.fd(4-stOffset*2)
      t.pu()
      t.fd(stOffset)
      # reset 
      t.bk(4)
      t.rt(90)
      t.fd(1)
      t.lt(90)
    
  else:
    for stOffset in (2,1,0):
      for i in range(len(row)):
        t.color(COLOR_LIST[row[i]])
        if i==0:
          t.pu()
          t.fd(stOffset)
          t.pd()
          t.fd(5-stOffset)
        elif i < len(row)-1:
          t.fd(4)
        else:
          t.fd(5-stOffset)
          t.pu()
          t.fd(stOffset)
      t.bk(10 + (l-2)*4)
      t.rt(90)
      t.fd(1)
      t.lt(90)
  t.bk(2)

testGeneratePascal(2, 16)
