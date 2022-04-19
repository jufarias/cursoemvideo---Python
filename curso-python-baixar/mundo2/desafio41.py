from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A sua categoria é: MIRIM.')
elif idade <= 14:
    print('A sua categoria é: INFANTIL.')
elif idade <= 19:
   print('Sua categoria é: JUNIOR.')
elif idade <= 25:
    print('Sua cateforia é: SÊNIOR.')
else:
    print('Sua categoria é: MASTER.')