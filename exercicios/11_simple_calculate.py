c1=int(input("Código do produto 1: "))
q1=int(input("Quantidade de produtos: "))
v1=float(input("Valor do produto 1:"))



c2=int(input("Código do produto 2: "))
q2=int(input("Quantidade de produtos: "))
v2=float(input("Valor do produto 2:"))

r1= q1 * v1
r2= q2 * v2

print(f"O valor a ser pago é {(r1+r2):.2f}")