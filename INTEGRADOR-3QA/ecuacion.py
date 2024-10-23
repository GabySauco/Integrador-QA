import math

def ecuacion_cuadratica (a,b,c):
    discriminante = b**2 - 4*a*c

    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    return raiz1, raiz2

#ejemplo
print(ecuacion_cuadratica(1, 5, 6))
