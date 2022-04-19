casa = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
ano = int(input('Quantos anos de financiamento? '))
parcelas = casa / (ano*12)
minimo = sal * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos,\nas parcelas serão de R${:.2f}'.format(casa,ano,parcelas))
if parcelas <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO! ')