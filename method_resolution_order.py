# MRO => Method Resolution Order
# Used by python to search for the right method to use in classes having multi-inheritance

# Old MRO algorithm (DLR, Deep first, from left to right ): used in old python classes i.e not inheriting from object
# Old MRO algorithm (C3 Algorithm) : used in new python classes i.e inheriting from object
class A:
    def whoami(self):
        print("I am A")


class B:
    def whoami(self):
        print("I am B")


class C(A, B):  # MRO of C will be C --> A ---> B
    pass


class D(B, A):  # MRO of D will be D --> B ---> A
    pass


# class E(C, D):  # MRO can't be decided because both parent class(C-> A,B  D->B,A) have different MRO
#     pass


c = C()
c.whoami()

d = D()
d.whoami()


# e = E()
# e.whoami()


class F(A):
    def whoami(self):
        print("I am in F")


class G(A):
    def whoami(self):
        print("I am in G")


class H(F, G):
    def whoami(self):
        print("I am G")


class I(G, F):
    pass


# https://www.youtube.com/watch?v=cuonAMJjHow

h = H()
h.whoami()

i = I()
i.whoami()

print(I.__mro__)
print(H.__mro__)


# super with multiple Inheritance
class Base:
    def basem(self):
        print("Inside base")


class DerivedBase1(Base):
    def basem(self):
        super().basem()


class DerivedBase2(Base):
    def basem(self):
        print("Inside Derive base 2")


class Derive(DerivedBase1, DerivedBase2):
    def basem(self):
        super().basem()


print(Derive.__mro__)
derive = Derive()
derive.basem()
