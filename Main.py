from BinaryModularArithmetic import BinaryModularArithmetic
from BinaryLambdaEllipticCurve import BinaryLambdaEllipticCurve

## q^127 over x^127+x^63+1

bma = BinaryModularArithmetic(127, 170141183460469231740910675752738881537)
print(bma.multiply(102851, 52772))
print(bma.multiply(52772, 102851))
print(bma.multiply(5516292, bma.inverse(5516292)))
print(bma.multiply(2, bma.multiply(2, 2)))

bec = BinaryLambdaEllipticCurve(1, 1, 127, 170141183460469231740910675752738881537)
Xp, Lp, Zp = bec.toProjectivePoint(10, 20)
x, y = bec.toAffinePoint(Xp, Lp, Zp)
X2p, L2p, Z2p = bec.multiplyProjectivePoint(400, Xp, Lp, Zp)
X3p, L3p, Z3p = bec.multiplyProjectivePoint(517, Xp, Lp, Zp)

print(bec.multiplyProjectivePoint(517, X2p, L2p, Z2p))
print(bec.multiplyProjectivePoint(400, X3p, L3p, Z3p))
