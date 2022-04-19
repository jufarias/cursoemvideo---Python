nome = str(input('Qual é o seu nome? '))
if nome == 'Juliana':
    print('Que nome bonito!')
elif nome == 'vini' or 'Maria' or 'Malu':
    print('Seu nome é tão normal no Brasil.')
else:
    print('Seu nome é tão comum.')
print('Tenha um bom dia, {}!'.format(nome))