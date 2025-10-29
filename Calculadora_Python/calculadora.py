operadores = ['*', '/','+','-']

roberto = True
while(roberto):
    sentence = input("Digite a expressão entre dois numeros: ")
    PosOps = 0
    for i, letter in enumerate(sentence):
        if (letter in operadores):
            a = int(sentence[PosOps:i])
            PosOps = i+1
            print(f"achei o operador {letter} na posicão {i}")
            print(f"Oq veio antes do Operador: {a}")
    ultimo = int(sentence[PosOps:])
    print(f"Ultimo numero encontrado: {ultimo}")
    roberto = False
