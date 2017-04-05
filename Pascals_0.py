from turtle import *
import math

def nCr(n,r):
  return math.factorial(n) // (math.factorial(r)*math.factorial(r-n))

def generatePascal(rowMax):
  for n in range(rowMax):
    i = n
    for k in range(i):
      print(str(nCr(n,k)))
