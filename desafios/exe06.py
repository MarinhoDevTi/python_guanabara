from contextlib import nullcontext

def raizq (numq):
    numq = numq ** 0.5
#fim da função                                   


num = int(input("Digite um número: "))
dob = num * 2
tri = num * 3
raizq = num ** 0.5

print("O dobro de {} vale {}.".format(num, dob))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}".format(num, tri, num, raizq))
