
print("calculador de imc")
peso = int(input("qual o seu peso em quilos?"))
altura = float(input("qual a sua altura em metros?"))

altura_2 = altura * altura

imc_final = round(peso/altura_2, 2)


print(f"seu IMC é: {imc_final}")


if imc_final <= 18.5:
    print("de acordo com o seu IMC, você esta com baixo peso!")
elif imc_final <= 24.9:
    print("de acordo com o seu IMC, você esta com peso normal!")
elif imc_final <= 29.9:
    print("de acordo com o seu IMC, você esta com exceço de peso!")
elif imc_final <= 34.9:
    print("de acordo com o seu IMC, você esta com obesidade nivel 1!")
elif imc_final <= 39.9:
    print("de acordo com o seu IMC, você esta com obesidade nivel 2!")
else:
    print("de acordo com o seu IMC, você esta com obesidade nivel 3!")
