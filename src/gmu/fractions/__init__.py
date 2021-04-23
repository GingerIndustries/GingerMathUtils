from ..errors import FractionAdditionError

class Fraction():
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def __iter__(self):
    return [self.numerator, self.denominator].__iter__()
  def __str__(self):
    return (str(self.numerator) + "/" + str(self.denominator))
  def _lcmcalc(self, numbers): #duplicated to prevent circular import
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
        break
      else:
        pass
      iterations += 1
    return lcm
  def _calc(self, other, mode):
    numer1 = self.numerator
    numer2 = other.numerator
    denom1 = self.denominator
    denom2 = other.denominator
    lcm = self._lcmcalc([denom1, denom2])
    multi1 = lcm / other.denominator
    multi2 = lcm / self.denominator
    numer1 *= multi2
    numer2 *= multi1
    denom1 = denom2 = lcm
    if mode == "a":
      numer = numer1 + numer2
    elif mode == "s":
      numer = numer1 - numer2
    return round(numer), denom1

  def _simp(self, numer, denom):
    #uwu
    counter = 10
    lowest = [numer, denom]
    while True:
      counter = 10
      answers = []
      while counter != 0:
        bcm = (lowest[1] / counter)
        tcm = (lowest[0] / counter)
        if int(round(bcm)) == bcm and int(round(tcm)) == tcm:
          answers.append([tcm, bcm])
        counter -= 1
      if answers[0] != lowest:
        for item in answers:
          if item[1] < lowest[1]:
            lowest = item
      else:
        return round(lowest[0]), round(lowest[1])
  
  def __add__(self, other):
    return Fraction(*self._calc(other, "a"))
  def __sub__(self, other):
    return Fraction(*self._calc(other, "s"))
  def __invert__(self):
    return Fraction(*self._simp(self.numerator, self.denominator))

class MixedNumber():
  def __init__(self, whole, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
    self.whole = whole
  
  #again, circular imports :(
  def _toMixed(self, fraction):
    numer = fraction.numerator
    denom = fraction.denominator
    return MixedNumber(round(numer / denom), numer - denom * round(numer / denom), denom)
  def _fromMixed(self, mixed):
    return Fraction(mixed.numerator + mixed.denominator * mixed.whole, mixed.denominator)

  def __str__(self):
    return (str(self.whole) + " " + str(self.numerator) + "/" + str(self.denominator))
  def __iter__(self):
    return [self.whole, self.numerator, self.denominator].__iter__()
  def __add__(self, other):
    return self._toMixed(self._fromMixed(self) + self._fromMixed(other))
  def __sub__(self, other):
    return self._toMixed(self._fromMixed(self) - self._fromMixed(other))
  