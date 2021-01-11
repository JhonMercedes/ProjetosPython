#!python3
# Simulador de Dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado(Frame):
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 2
        self.mensagem = 'Voce gostaria de gerar um valor para o Dado ? '
        # Layout 
        self.layout = [
            [sg.Text('Jogar Dado ? ')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        
    
    def Iniciar(self):
        # Criar Janela 
        self.janela = sg.Window('Simulador De Dado',layout=self.layout)
        # Ler os valores da tela 
        self.eventos, self.valores = self.janela.Read()

        # Fazer alguma ação com os valores
       
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else: 
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')    

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
