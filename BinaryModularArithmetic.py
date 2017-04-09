class BinaryModularArithmetic:

    def __init__(self, m, primitive):
        self.m = m
        self.limit = 1 << m
        self.primitive = primitive

    def degree(self, a):
        return a.bit_length()

    def reduce(self, a):
        c = a
        if (c & self.limit):
            c = c ^ self.primitive
        return c

    def add(self, a, b):
        c = a ^ b
        return c
    
    def subtract(self, a, b):
        c = self.add(a, b)
        return c

    def square(self, a):
        c = self.multiply(a, a)
        return c

    def multiply(self, a, b):
        mask = self.limit - 1
        c = 0
        while (b):
            if (b & 1):
                c = c ^ a
            a = a << 1
            a = self.reduce(a)
            b = b >> 1
        c = self.reduce(c)
        return c

    def multiply2(self, a, b):
        c = 0
        mask = 1 << (self.limit - 1)
        for i in range(b.bit_length() - 1, 0):
            c = c << 1
            c = self.reduce(c)
            if (b & mask):
                c = c ^ a
            b = b << 1
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
