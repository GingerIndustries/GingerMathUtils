import sys
sys.path.append("src/")
import gmu.fractionutils
import gmu.fractions

fraction = gmu.fractions.Fraction(14, 6)
print(fraction)
print(gmu.fractionutils.toMixed(fraction))
print(fraction - gmu.fractions.Fraction(1, 12))
simp = gmu.fractions.Fraction(10, 20)
print(~simp)

print(gmu.fractions.MixedNumber(2, 1, 2) + gmu.fractions.MixedNumber(2, 1, 2))
print(list(fraction))