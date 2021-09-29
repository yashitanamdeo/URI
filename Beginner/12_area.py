A,B,C = map(float,input().split())
triangle = 0.5 * A * C
circle = 3.14159 * (C**2)
trapezium = ((A+B)/2) * C
square = B**2
rectangle = A*B

print("TRIANGULO:",format(triangle,".3f"))
print("CIRCULO:",format(circle,".3f"))
print("TRAPEZIO:",format(trapezium,".3f"))
print("QUADRADO:",format(square,".3f"))
print("RETANGULO:",format(rectangle,".3f"))