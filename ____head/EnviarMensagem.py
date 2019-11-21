import socket
import json
from typing import List

import DivideTexto, AnalisandoRecursos, Balanceamento

import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *


def enviarMensagem(mensagem, sco, janela):
   
    soc = []
    '''---- Criando sockets-----'''
    
    for i in range(3):
        soc.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
   
    
    '''--- Atribuindo PORTAS-----'''
    p = [5005, 1482, 1488]
    ip = ['192.168.43.19', '192.168.43.174', '192.168.43.187']
    status = []
    at = []
    inat = []
    
    while True:
        
        try:
            
            for i in range(3):
                try:
                    soc[i].connect((ip[i], p[i]))
                    print('Conectou com o pc {}'.format(i + 1))
                    recebido = soc[i].recv(1024).decode()
                    
                    if (recebido == 'Computador Ativo'):
                        status.append(i)
                except Exception as e:
                    print('O computador {} nao conectou'.format(i + 1))
                    status.append('*')
            
            '''---------Imprimindo qtd e quais máquinas estão ativas e inativas---------'''
            print('\n-------------------\n')
            print('Status: ', status)
            for i in range(len(status)):
                if (status[i] == '*'):
                    inat.append(i)
                else:
                    at.append(i)
            
            '''---- Somando mais 1 para printar---- [0,1] -> [1,2]'''
            sat = []
            for i in at:
                sat.append(i + 1)
            
            sinat = []
            for i in inat:
                sinat.append(i + 1)
            
            
            if (sat == []):
                print('Quantidade de computadores ativos: ', len(at), '| Nenhum Computador Ativo')
            else:
                print('Quantidade de computadores ativos: ', len(at), '| Computadores Ativos: ', sat)
                
            print('-------------')
            
            if (sinat == []):
                print('Quantidade de computadores inativos: ', len(inat),  '| Todos estao Ativos')
            else:
                print('Quantidade de computadores inativos: ', len(inat),'| Computadores inativos: ', sinat)

           
            ''''-----Enviando ao ClientMachine a quantidade de computadores Ativos-----'''
            lSat = json.dumps(sat)
            sco.send(lSat.encode())
            
            qtdAt = tk.Label(janela, text='Quantidade de computadores ativos:')
            qtdAt.place(x=160,y=180)
            
            
            x = 350
            for i in sat:
                st = str(i)
                qtdAt = tk.Label(janela, text=st, bg='orange')
                qtdAt.place(x=x, y=180)
                x = x+15

            qtdIn = tk.Label(janela, text='Quantidade de computadores inativos:')
            qtdIn.place(x=160, y=210)

            x = 350
            for i in sinat:
                st = str(i)
                qtdIn = tk.Label(janela, text=st, bg='orange')
                qtdIn.place(x=x, y=210)
                x = x + 15














        except Exception as e:
            print('Erro EnviarMensagemTry1', e)
        
        try:
            
            textoQuebrado = DivideTexto.divideTexto(mensagem, len(at))
            
            print('\n-------------------\n')
            
            print('Pre-divisoes de palavras: ')
            for i in range(len(at)):
                print('Nó {}'.format(at[i] + 1), '-', len(textoQuebrado[i]), 'palavras')
                #print('Quantidade de palavras analisadas No {}:'.format(at[i] + 1), len(textoQuebrado[i]),'palavras')
                #print('Node {} analisará: '.format(at[i] + 1), textoQuebrado[i])

                
            '''------ Analisando recursos dos computadores ativos---------'''
            cpu_livre = AnalisandoRecursos.analisandoRecursos(soc,status)
           
            limite = Balanceamento.balanceamento(soc, status, cpu_livre,textoQuebrado)
            
            
            
            print('Tamanho textoQuebrado: ', len(textoQuebrado[0]))
            
            '''---Imprimindo Grafico---'''
            
            
            dados = []
            valores = []

            sat = []
            for i in at:
                sat.append(i + 1)
                
            for i in range(len(sat)):
                var = str(sat[i])
                dados.append(var)
                
            stextoQuebrado = 0
            for i in range(len(at)):
                stextoQuebrado = len(textoQuebrado[i]) + stextoQuebrado
            for i in limite:
                valores.append((i * 100)/stextoQuebrado)

            plt.figure(figsize=(3, 3))

            plt.pie(x=valores, labels=dados, autopct='%1.1f%%')  # Grafico de Pizza
            plt.savefig('deucerto.png', format='png')

            im = tk.PhotoImage(file='deucerto.png')
            w = tk.Label(janela, image=im, bg='#025398').place(x=440, y=300)
            
            
            
            
            
            
          
            
            
            
            
            
            
            
            
            '''----- Enviando o texto aos Nodes ----'''

           
            aux = 0
            print('\n-------------------------\n')
            for i in status:
                if (i != '*'):
                    j = ','.join(textoQuebrado[aux]).replace(',', ' ')
                    soc[i].send(j.encode())
                    print('Texto enviado ao Node{} '.format(i + 1))
                    aux += 1
                else:
                    continue
            
            '''----- Recebe as palavras erradas do Node --- '''
            
            
            copia_status = []
            for h in status:
                if (h != '*'):
                    copia_status.append(h)

            listaDePalavrasErradas = []
            
            print('Copia Status', copia_status)
            au = 0
            for i in copia_status:
                listaDePalavrasErradas.insert(au, soc[i].recv(1024).decode())
                au += 1
            
            '''------Imprimindo palavras erradas-----'''
            
            
            aux = 0
            for i in listaDePalavrasErradas:
                print('\n')
                print('NÓ', copia_status[aux] + 1,' - Palavras Erradas: ','\n  ', i)
                aux+=1
                
            print('---------------------------')
            for i in range(3):
                soc[i].close()
            return listaDePalavrasErradas
            
        
        except Exception as e:
            print("Erro em EnviarMensagem", e)
        break
        
        
        
    
    
    
   