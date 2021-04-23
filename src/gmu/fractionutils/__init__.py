from .. import getVersion
from ..fractions import Fraction, MixedNumber
from ..errors import FractionAdditionError

def toMixed(fraction):
  numer = fraction.numerator
  denom = fraction.denominator
  return MixedNumber(round(numer / denom), numer - denom * round(numer / denom), denom)
def fromMixed(mixed):
  return Fraction(mixed.numerator + mixed.denominator * mixed.whole, mixed.denominator)

def lcm(numbers):
  iterations = 1
  multiples = []
  for item in numbers:
    multiples.append([])
  while True:
    for x in range(0, len(numbers)):
      item = numbers[x]
      multiples[x].append(item * iterations)
    same = False
    lcm = 0
    for item in multiples[0]:
      isIn = []
      for lst in multiples:
        isIn.append(item in lst)
      if all(isIn):
        same = True
        lcm = item
        break
    if iterations == 1000:
      raise FractionAdditionError("EMERGENCY FAILSAFE ACTIVATED! Addition terminated due to calculations taking over 1000 iterations. This is too keep you from running out of memory, time, and patience.")
      lcm = False
      break
    if same:
      print("\n\n\n\n\nSuccess! The LCM is", lcm, "\nCalculated in", iterations, "iterations.")
      break
    else:
      print("None are the same. Continuing...")
    iterations += 1
  return lcm