import functools

class BinaryModularArithmetic:

    def __init__(self, m, polynomial):
        self.m = m
        self.limit = 1 << m
        self.primitive = self.findPrimitive(m, polynomial)

    def getPrimitive(self):
        return self.primitive

    def findPrimitive(self, m, polynomial):
        binaryPolynomial = [0] * (m + 1)
        for index in polynomial:
            binaryPolynomial[index] = 1
        binaryPolynomial.reverse()
        temp = map(lambda a, b: a << b, binaryPolynomial, range(len(binaryPolynomial) - 1, -1, -1))
        return functools.reduce(lambda a, b: a | b, temp)

    def degree(self, a):
        return a.bit_length()

    def reduce(self, a):
        c = a
        if (c & self.limit):
            c = c ^ self.primitive
        return c

    def add(self, a, b):
        c = a + b
        return self.reduce(c)
    
    def subtract(self, a, b):
        c = self.add(a, b)
        return c

    def square(self, a):
        c = self.multiply(a, a)
        return c

    def multiply(self, a, b):
        c = 0
        while (b):
            if (b & 1):
                c = c ^ a
            a = a << 1
            a = self.reduce(a)
            b = b >> 1
        c = self.reduce(c)
        return c

    def divide(self, a, b):
        inverseOfB = self.inverse(b)
        c = self.multiply(a, inverseOfB)
        return c

    def inverse(self, x):
        u1 = 0
        u3 = self.primitive
        v1 = 1
        v3 = x
        while (v3):
            t1 = u1
            t3 = u3
            q = self.degree(u3) - self.degree(v3)
            if (q >= 0):
                t1 = t1 ^ (v1 << q)
                t3 = t3 ^ (v3 << q)
            u1 = v1
            u3 = v3
            v1 = t1
            v3 = t3
        u1 = self.reduce(u1)
        return u1
