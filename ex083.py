'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada esa com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: '))
pilha = []

for símbolo in expressao:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida!')

''' Minha solução 
if '(' in expressao:
    print(expressao.count('('))
if ')' in expressao:
    print(expressao.count(')'))

if expressao.count('(') == expressao.count(')'):
    print('A expressão digitada esta correta!')
else:
    print('A expressão digitada esta errada!')
'''
