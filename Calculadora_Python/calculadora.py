
#------------------------
#   Pré-Processamento
#------------------------
operadores = ['*', '/','+','-']
roberto = True
partial_numbers = []
operators_sequence = []
sentence = input("Digite a expressão entre dois numeros: ")
while(roberto):
    PosOps = 0
    for i, letter in enumerate(sentence):
        if (letter in operadores):
            a = int(sentence[PosOps:i])
            partial_numbers.append(a)
            PosOps = i+1
            operators_sequence.append(letter)
            #print(f"achei o operador {letter} na posicão {i}")
            #print(f"Oq veio antes do Operador: {a}")
    ultimo = int(sentence[PosOps:])
    partial_numbers.append(ultimo)
    #print(f"Ultimo numero encontrado: {ultimo}")
    roberto = False
print(partial_numbers)
print(operators_sequence)

#------------------------
#      Processamento
#------------------------


while(len(operators_sequence) != 0):
    if '*' in operators_sequence:
        operators_index = operators_sequence.index('*')
        resultado = partial_numbers[operators_index] * partial_numbers[operators_index+1]
        partial_numbers.pop(operators_index)
        partial_numbers.pop(operators_index)
        partial_numbers.insert(operators_index, resultado)
        operators_sequence.remove('*')
    elif '+' in operators_sequence:
        operators_index = operators_sequence.index('+')
        resultado = partial_numbers[operators_index] + partial_numbers[operators_index+1]
        partial_numbers.pop(operators_index)
        partial_numbers.pop(operators_index)
        partial_numbers.insert(operators_index, resultado)
        operators_sequence.remove('+')
    elif '-' in operators_sequence:
        operators_index = operators_sequence.index('-')
        resultado = partial_numbers[operators_index] - partial_numbers[operators_index+1]
        partial_numbers.pop(operators_index)
        partial_numbers.pop(operators_index)
        partial_numbers.insert(operators_index, resultado)
        operators_sequence.remove('-')

print(partial_numbers)
print(operators_sequence)

# [12, 56, 42, 43]
# ['+', '*', '+']
# 3

12+56*42+43*6-70

