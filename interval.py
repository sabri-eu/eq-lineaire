from sympy.abc import x,y
from sympy import solveset,S,Interval
from sympy.simplify.simplify import *
import numpy as np
from math import *


question = input("Type =")
if question == "1":
  z = input("x =")
  if z == "pi":
    z = pi
  if z == "sqrt()":
    num = int(input("quel nombre"))
    z = sqrt(num)
  if z == "sqrt()pi":
    v = int(input("ton sqrt"))
    z = sqrt(y)*pi
    z == sqrt(y)
  one = int(z)
  print(one)
elif question == "2":
  z = input("x =")
  if z == "sqrt()pi":
    num = int(input(sqrt))
    z = sqrt(num)*pi
  if z == "sqrt()":
    num = int(input("sqrt"))
    z = sqrt(num)
  if z == "nsqrt()":
    num = int(input("nb"))
    sqr = int(input("sqrt"))
    z = num*sqrt(sqr)
  if z == "nsqrt()pi":
        num = int(input("nb"))
        sqr = int(input("sqrt"))
        z = num*sqrt(sqr)*pi
  v = int(input("y ="))
  if v == "pi":
    num = int("ton nombre")
    v = num*pi
  two = z/v
  print(two)
print("Membre de droit")
a = int(input("Premier chiffre"))
b = int(input("Second chiffre"))
c = int(input("Troiseme chiffre"))
d = int(input("Quatrieme chiffre"))
a1 = a*x+b
b1 = c*x+d
signe = input("Quelle signe ?")
if signe == ">=":
  if question == "2":
    res = a1/b1 - z/v
  if question == "1":
    eq = a1/b1 - z
if signe == "<=":
  if question == "2":
    res = -a1/b1 + z/v
  if question == "1":
    res = -a1/b1 + z

print("# Calcul de Alpha")
if question == "2":
  alpha = z/v
if question == "1":
  alpha = z
print(alpha)

print("#Calcul de A")
result = a - c * alpha
print("A =", result)
print("#Calcul de B")
resulta = b - d * alpha
print("B =", resulta)

print("#Calcul de l'interval")
res = solveset(res >= 0, domain=S.Reals)
print(res)