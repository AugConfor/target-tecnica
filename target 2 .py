num1=0
num2=1
num_Desejado = input("Digite um número:")
num_Next = num2
while int(num_Desejado) > num_Next:
    num1, num2 = num2, num_Next
    num_Next = num1 + num2
if int(num_Desejado) == num_Next:
    print("Pertence a sequência.")
else:
    print("Não pertence.")
