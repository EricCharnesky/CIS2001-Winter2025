from polynomial import Polynomial

poly2 = Polynomial(2,3) # makes the polynomial 2.00x^3
poly2 = Polynomial(2,3) # makes the polynomial 2.00x^3
poly3 = Polynomial(3,4) # makes the polynomial 3.00x^4
poly1 = poly2 + poly3 # makes poly1 = 3.00x^4 + 2.00x^3
print(poly1) # prints out 3.00x^4 + 2.00x^3
poly3 = poly2*poly1 # sets poly3 to 6.00x^7+4.00x^6
poly4 = poly3.differentiate() # sets poly4 to 42.00x^6+24.00x^5
poly5 = poly1.integrate() # sets poly5 to .60x^5+.50x^4

print(poly3)
print(poly4)
print(poly5)
#
# poly7 = poly1 + poly2
# print(poly7)
# poly9 = Polynomial(5, 7)
# poly11 = poly7 + poly9
# print(poly11)

print(poly4 == poly5)
print(poly2 == Polynomial(2, 3))