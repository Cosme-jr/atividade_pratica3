"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
temp = float(input("Digite a temperatura a ser convertida: "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

if unidade_origem == "C":
    if unidade_destino == "F":
        temp_convertida = (temp * 9/5) + 32
    elif unidade_destino == "K":
        temp_convertida = temp + 273.15
    else:
        temp_convertida = temp
elif unidade_origem == "F":
    if unidade_destino == "C":
        temp_convertida = (temp - 32) * 5/9
    elif unidade_destino == "K":
        temp_convertida = (temp - 32) * 5/9 + 273.15
    else:
        temp_convertida = temp
elif unidade_origem == "K":
    if unidade_destino == "C":
        temp_convertida = temp - 273.15
    elif unidade_destino == "F":
        temp_convertida = (temp - 273.15) * 9/5 + 32
    else:
        temp_convertida = temp
else:
    print("Unidade de origem inválida.")
    temp_convertida = None

if temp_convertida is not None:
    print(f"A temperatura convertida é {temp_convertida:.2f}°{unidade_destino}.")