class A:
    def z(self):
        return self
    
    def y (self, t):
        return len(t)

a = A
y = a.z
print(y(a))
aa = a()
print(aa)