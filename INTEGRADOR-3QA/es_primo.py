def es_primo(num):
    if num <= 1:
        return False
    for i in range (2, int(num ** 0.5) +1):
        if num % i ==0:
            return False
    return True

if es_primo(2):
    print(f"El número es primo.")
else:
    print(f"El número no es primo.")


 
    