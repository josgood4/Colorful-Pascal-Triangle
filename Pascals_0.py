from turtle import *
import math

COLOR_LIST = ['white', 'black', 'yellow', 'green', 'orange', 'blue', \
              'violet', 'brown', 'pink', 'grey']
BLOCK_WIDTH = 2 # width of INNER blocks in the triangle - MUST BE >= 4
HEIGHT = BLOCK_WIDTH//2 # its best if the BLOCK_WIDTH:HEIGHT ratio is ~2

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
  t.speed(0)
  t.pu()
  t.lt(90)
  t.fd(HEIGHT*rowMax//2)
  t.rt(90)
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
    ##print("l=0")
    for stOffset in range(HEIGHT-1, -1, -1):
      t.color(COLOR_LIST[row[0]])
      t.pu()
      t.fd(stOffset)
      t.pd()
      t.fd(BLOCK_WIDTH-stOffset*2)
      t.pu()
      t.fd(stOffset)
      # reset 
      t.bk(BLOCK_WIDTH)
      t.rt(90)
      t.fd(1)
      t.lt(90)    
  else:
    for stOffset in range(HEIGHT-1, -1, -1):
      t.fd(stOffset)
      t.pd()
      for i in range(0,len(row)):
        t.color(COLOR_LIST[row[i]])
        
        # this case handles the center block when l is even
        if i == (l-1)/2:
          t.fd(BLOCK_WIDTH-stOffset*2)
          
        # this case handles the center 2 blocks when l is odd
        elif (l%2 == 0) and ((i == (l-1)//2) or (i == (l-1)//2+1)):
          t.fd(BLOCK_WIDTH - stOffset)
          
        # this is all other cases
        else:
          t.fd(BLOCK_WIDTH)         
      t.pu()
      t.fd(stOffset)
          
      t.bk(BLOCK_WIDTH*l)
      t.rt(90)
      t.fd(1)
      t.lt(90)
  t.bk(BLOCK_WIDTH//2)

testGeneratePascal(10, 64)
