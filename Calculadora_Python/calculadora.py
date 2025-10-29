class Calculadora:
    def __init__(self):
        self.partial_numbers = list()
        self.operators_sequence = list()
        self.resultado = 0

    def calcular(self, sentence):
        self._pre_processamento(sentence)
        self._processamento()

    def _pre_processamento(self, sentence):
        """
            Pré-Processamento
        """
        operadores = ['*', '/','+','-']
        roberto = True
        self.partial_numbers = []
        self.operators_sequence = []
        while(roberto):
            PosOps = 0
            for i, letter in enumerate(sentence):
                if (letter in operadores):
                    a = int(sentence[PosOps:i])
                    self.partial_numbers.append(a)
                    PosOps = i+1
                    self.operators_sequence.append(letter)
                    #print(f"achei o operador {letter} na posicão {i}")
                    #print(f"Oq veio antes do Operador: {a}")
            ultimo = int(sentence[PosOps:])
            self.partial_numbers.append(ultimo)
            #print(f"Ultimo numero encontrado: {ultimo}")
            roberto = False
        print(self.partial_numbers)
        print(self.operators_sequence)

    def _calculo_basico(self, operador):
        operators_index = self.operators_sequence.index(operador)
        if operador == '*':
            resultado = self.partial_numbers[operators_index] * self.partial_numbers[operators_index+1]
        elif operador == '/':
            resultado = self.partial_numbers[operators_index] / self.partial_numbers[operators_index+1]
        elif operador == '-':
            resultado = self.partial_numbers[operators_index] - self.partial_numbers[operators_index+1]
        elif operador == '+':
            resultado = self.partial_numbers[operators_index] + self.partial_numbers[operators_index+1]
        self.partial_numbers.pop(operators_index)
        self.partial_numbers.pop(operators_index)
        self.partial_numbers.insert(operators_index, resultado)
        self.operators_sequence.remove(operador)

    def _processamento(self):
        while(len(self.operators_sequence) != 0):
            if '*' in self.operators_sequence or '/' in self.operators_sequence:
                if '/' in self.operators_sequence:
                    self._calculo_basico('/')
                else:
                    self._calculo_basico('*')
            elif '+' in self.operators_sequence:
                self._calculo_basico('+')
            elif '-' in self.operators_sequence:
                self._calculo_basico('-')
        self.resultado = self.partial_numbers[0]

Calc = Calculadora()
Calc.calcular("12+56*42+43/6-70")
print(Calc.resultado)

# [12, 56, 42, 43]
# ['+', '*', '+']
# 3

12+56*42+43/6-70

