
import functools

from BinaryModularArithmetic import BinaryModularArithmetic
from BinaryLambdaEllipticCurve import BinaryLambdaEllipticCurve

## q^127 over x^127+x^63+1
m = 127
polynomail = [127, 63, 0]
testBinaryModularArithmetic = False

if (testBinaryModularArithmetic):
    bma = BinaryModularArithmetic(m, polynomail)
    print(bma.multiply(102851, 52772))
    print(bma.multiply(52772, 102851))
    print(bma.multiply(5516292, bma.inverse(5516292)))
    print(bma.multiply(5457623469874, bma.inverse(5457623469874)))
    print(bma.divide(bma.multiply(4863215, 5516292), 4863215))

bec = BinaryLambdaEllipticCurve(1, 1, m, polynomail)
x, y = bec.findPoint(1)

Xp, Lp, Zp = bec.toProjectivePoint(0, 1)
print(Xp, Lp, Zp)
x, y = bec.toAffinePoint(Xp, Lp, Zp)
print(x, y)
X2p, L2p, Z2p = bec.multiplyProjectivePoint2(400, Xp, Lp, Zp)
X3p, L3p, Z3p = bec.multiplyProjectivePoint2(517, Xp, Lp, Zp)
print(bec.multiplyProjectivePoint2(517, X2p, L2p, Z2p))
print(bec.multiplyProjectivePoint2(400, X3p, L3p, Z3p))
