
import socket, EnviarMensagem, CesarCrip

import RemoveCarac, pickle

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt







#l = tk.Label(janela, text='Aguardando Conexão... ', bg='white')
#l.place(x=600, y=250)
#plt.figure(figsize=(3,3))
#plt.pie(x=valores, labels=dados, autopct='%1.1f%%', explode=ex) #Grafico de Pizza
# #bt = tk.Button(janela, text = 'Abrir Conexão', command=tt, bg='white')
#bt.place(x=629,y=180)




# Intantianre object s to work with sockets
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import socket
import pickle
import CesarCrip
import EnviarMensagem
import RemoveCarac
import threading

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind works to head conections. use " " to hear any IP conection in that port.
so.bind(("", 9999))


def Inicializar():
    # Accept just 1 conection in the socket
    so.listen(1)
    l = tk.Label(janela, text='Aguardando conexao... ', bg='white')
    l.place(x=570, y=150)
    
    # Instantiate object sc. s.accept  return 2 values, IP and Port from new conection
    sco, addri = so.accept()
    l.destroy()
    pgbar.destroy()
    
    while True:
        
        try:
            # Receiving client messages. Method recv receive data and 1024 is the amount of bytes
            recebido = sco.recv(4096)
            
            descplic = pickle.loads(recebido)
            mensagem = CesarCrip.decripta(descplic, 3)
            
            # print('Texto Recebido: ', descplic)
            print('Texto Recebido Desriptografado: ', mensagem)
            print('---------------------')
            
            arquivo = open('RECEBIDO.txt', 'w')
            arquivo.write(mensagem)
            arquivo.close()
            print("Quantidade de palavras, ", len(mensagem.split()))
            
            noCarc = RemoveCarac.chr_remove(mensagem, "$%_,?.!#&#+")
            
            msg = EnviarMensagem.enviarMensagem(noCarc, sco, janela)
            print('Msg:', msg)
            
            '''---Envio de volta ao ClientMachine---'''
            encript = CesarCrip.encripta(msg, 3)
            print('encrpt:', encript)
            
            palavrasErradas = pickle.dumps(encript)
            
            print('Pickle:', palavrasErradas)
            print('Tipo Pickle:', type(palavrasErradas))
            
            sco.send(palavrasErradas)
            
            print('Enviado ao clienteMachine...\n')
            
            break
        
        except Exception as e:
            print('ERRO\n', e)
            break
    sco.close()  # Conexao IP e o Socket


janela = tk.Tk()
janela.title('Janela Principal')
janela['bg'] = '#025398'
janela.geometry('1350x750+0+0')
imagem = tk.PhotoImage(file='show2.png')
w = tk.Label(janela, image=imagem, bg='#025398').place(x=440, y=5)

pgbar = Progressbar(janela, orient=HORIZONTAL, length=100)
pgbar.place(x=590, y=170)
pgbar.start()

bt = tk.Button(command=Inicializar, text='Inicializar')
bt.place(x=610, y=210)

janela.mainloop()
so.close()






