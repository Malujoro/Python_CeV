kg = float(input('Qual seu peso? (kg): '))
m = float(input('Digite sua altura? (m): '))
imc = kg / m**2
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPRESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
