peso = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual é sua altura: (m) '))
imc = peso / (alt ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO peso normal')
elif imc >= 18.5 and imc <25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
