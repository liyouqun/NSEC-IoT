import enum

class A(enum.Enum):
    AA = 1
    AB = 2
    AC = 3
    class a(enum.Enum):
        a = 1
        b = 2

class B(enum.Enum):
    BA = 1
    BB = 2
    BC = 3

print(A.AA)
print(repr(A.AA))
print(type(A.AA))
print(B.BA)

print(A.AA == B.BA)

print(A.a)
print(A.a.b)
