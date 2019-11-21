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


class Aplicacao:
   def __init__(self, master=None):
      self.fontePadrao = ("Arial", "12")
      self.unicoContainer = Frame(master)
      self.unicoContainer['bg'] = '#025398'
      self.unicoContainer["pady"] = 10
      self.unicoContainer.pack(side='right')
      self.unicoContainer(bg='orange')

      
      
      self.msg = Message(self.unicoContainer, text='', font=self.fontePadrao)
      self.msg['widht'] = 200
      self.msg['bg'] = 'green'
      self.msg['fb'] = 'red'
      self.msg.pack()
      
      self.Inicializar()
   
   def Inicializar(self):
      
   
      # Bind works to head conections. use " " to hear any IP conection in that port.
      so.bind(("", 9999))
   
      # Accept just 1 conection in the socket
      so.listen(1)
   
      # Instantiate object sc. s.accept  return 2 values, IP and Port from new conection
      sco, addri = so.accept()
   
      while True:
      
         try:
            # Receiving client messages. Method recv receive data and 1024 is the amount of bytes
            recebido = sco.recv(4096)
            self.msg['text'] = 'Deu certooooooooooo'
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
         
            msg = EnviarMensagem.enviarMensagem(noCarc, sco)
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


   

janela = Tk()
janela.title('Janela Principal')
janela['bg'] = '#025398'
janela.geometry('1350x750+0+0')
imagem = tk.PhotoImage(file='show2.png')
w = tk.Label(janela, image=imagem, bg='#025398').place(x=440, y=5)
l = tk.Label(janela, text='Esperando texto.. ', bg='white')
l.place(x=570, y=150)




pgbar = Progressbar(janela, orient=HORIZONTAL, length=100)
pgbar.place(x=600, y=190)
pgbar.start()

Aplicacao(janela)
janela.mainloop()
so.close()