#!python3
# Projeto 5 - Decida por mim
# Faça uma pergunta para o programa e le terá que dar uma resposta 

import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso! ',
            'Não sei, você que sabe ',
            'Não faça isso! ',
            'Acho que tá na hora certa!'
        ]
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()*