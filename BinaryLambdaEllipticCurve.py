from BinaryModularArithmetic import BinaryModularArithmetic

class BinaryLambdaEllipticCurve:

    def __init__(self, a, b, n, polynomial):
        self.a = a
        self.b = b
        self.n = n
        self.modularArithmetic = BinaryModularArithmetic(n, polynomial)

    def findPoint(self, xFrom): 
        xFound = -1
        yFound = -1 
        limit = self.modularArithmetic.getPrimitive() - 1
        for x in range(xFrom, limit):
            for y in range(1, limit): 
                print(x, y)
                ySquare = self.modularArithmetic.square(y) 
                xSquare = self.modularArithmetic.square(x) 
                xCube = self.modularArithmetic.multiply(xSquare, x) 
                xy = self.modularArithmetic.multiply(x, y) 
                axSquare = self.modularArithmetic.multiply(self.a, xSquare) 
                left = self.modularArithmetic.add(ySquare, xy) 
                right = self.modularArithmetic.add(xCube, axSquare) 
                right = self.modularArithmetic.add(right, self.b) 
                if (left == right): 
                    yFound = y 
                    break 
            if (yFound):
                xFound = x
                break
        return xFound, yFound 

    def multiplyProjectivePoint(self, k, Xp, Lp, Zp):
        # TODO: Duzeltilecek (soldan sağa olacak şekilde değiştirlecek) (multiplyProjectivePoint2)
        Xq, Lq, Zq = 0, 0, 0
        while (k):
            Xp, Lp, Zp = self.doubleProjectivePoint(Xp, Lp, Zp)
            if (k & 1):
                Xq, Lq, Zq = self.addProjectivePoint(Xq, Lq, Zq, Xp, Lp, Zp)
            k >>= 1    
        return Xq, Lq, Zq

    def multiplyProjectivePoint2(self, k, Xp, Lp, Zp):
        found = 0
        mask = 1 << (self.n - 1)
        Xq, Lq, Zq = 0, 0, 0
        for i in range(k.bit_length() - 1, 0):
            if (found):
                Xq, Lq, Zq = self.doubleProjectivePoint(Xq, Lq, Zq)
            if (k & mask):
                if (found):
                    Xq, Lq, Zq = self.addProjectivePoint(Xq, Lq, Zq, Xp, Lp, Zp)
                else:
                    Xq, Lq, Zq = Xp, Lp, Zp
                found = 1
            k = k << 1   
        return Xq, Lq, Zq
        
    def toProjectivePoint(self, x, y):
        X = x
        L = self.modularArithmetic.divide(y, x)
        L = self.modularArithmetic.add(x, L)
        Z = 1
        return X, L, Z

    def toAffinePoint(self, X, L, Z):
        x = self.modularArithmetic.divide(X, Z)
        y = self.modularArithmetic.divide(L, Z)
        y = self.modularArithmetic.subtract(y, x)
        y = self.modularArithmetic.multiply(y, x)
        return x, y

    def doubleProjectivePoint(self, Xp, Lp, Zp):
        XpZp = self.modularArithmetic.multiply(Xp, Zp)
        XpZpXpZp = self.modularArithmetic.square(XpZp)
        LpLp = self.modularArithmetic.square(Lp)
        LpZp = self.modularArithmetic.multiply(Lp, Zp)
        ZpZp = self.modularArithmetic.square(Zp)
        aZpZp = self.modularArithmetic.multiply(self.a, ZpZp)
        T = self.modularArithmetic.add(LpLp, LpZp)
        T = self.modularArithmetic.add(T, aZpZp)
        TLpZp = self.modularArithmetic.multiply(T, LpZp)
        X2p = self.modularArithmetic.square(T)
        Z2p = self.modularArithmetic.multiply(T, ZpZp)
        L2p = self.modularArithmetic.add(XpZpXpZp, X2p)
        L2p = self.modularArithmetic.add(L2p, TLpZp)
        L2p = self.modularArithmetic.add(L2p, Z2p)
        return X2p, L2p, Z2p

    def addProjectivePoint(self, Xp, Lp, Zp, Xq, Lq, Zq):
        # TODO: İki point birbirine eşitse double yapılacak
        LpZq = self.modularArithmetic.multiply(Lp, Zq)
        LqZp = self.modularArithmetic.multiply(Lq, Zp)
        XpZq = self.modularArithmetic.multiply(Xp, Zq)
        XqZp = self.modularArithmetic.multiply(Xq, Zp)
        A = self.modularArithmetic.add(LpZq, LqZp)
        B = self.modularArithmetic.add(XpZq, XqZp)
        B = self.modularArithmetic.square(B)
        AB = self.modularArithmetic.multiply(A, B)
        ABZq = self.modularArithmetic.multiply(AB, Zq)
        Xpq = self.modularArithmetic.multiply(A, XpZq)
        Xpq = self.modularArithmetic.multiply(Xpq, XqZp)
        Xpq = self.modularArithmetic.multiply(Xpq, A)
        Lpq0 = self.modularArithmetic.multiply(A, XqZp)
        Lpq0 = self.modularArithmetic.add(Lpq0, B)
        Lpq0 = self.modularArithmetic.square(Lpq0)
        Lpq1 = self.modularArithmetic.add(Lp, Zp)
        Lpq1 = self.modularArithmetic.multiply(ABZq, Lpq1)
        Lpq = self.modularArithmetic.add(Lpq0, Lpq1)
        Zpq = self.modularArithmetic.multiply(ABZq, Zp)
        return Xpq, Lpq, Zpq
