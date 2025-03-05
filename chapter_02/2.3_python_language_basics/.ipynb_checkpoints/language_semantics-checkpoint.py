import some_module as sm
from some_module import g as gf, PI as pi

# result = sm.f(5)
# pi = sm.PI
"""
result = g(5, PI)

print(PI)
print(result)
"""
result1 = sm.f(pi)
result2 = gf(result1, pi)

print(result1)
print(result2)

# binary operators

a = 10.4
b = 29.6

aa = True
bb = True

# float division
print(a // b)

# Raise s to the b power
print(a ** b)

# and, or and exclusive-or
print(aa & bb)
print(aa | bb)
print(aa ^ bb)