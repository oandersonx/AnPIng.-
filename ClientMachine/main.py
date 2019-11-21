import json
import pickle
import socket
from tkinter import scrolledtext
import tkinter.scrolledtext as ScrolledText
from tkinter.ttk import *
import criptografia
from time import gmtime, strftime

from tkinter.filedialog import askopenfilename
from tkinter import *
from docx import Document
import tkinter as tk
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Application:

    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer['bg'] = '#025398'
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer['bg'] = '#025398'
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer['bg'] = '#025398'
        self.terceiroContainer.pack(side='right')

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 100
        self.quartoContainer['bg'] = '#025398'
        self.quartoContainer.pack()


        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 10
        self.quintoContainer['bg'] = '#025398'
        self.quintoContainer.pack(side='right')

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 100
        self.sextoContainer['bg'] = '#025398'
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 10
        self.setimoContainer['bg'] = '#025398'
        self.setimoContainer.pack()


        self.mensagemsegundo = Message(self.segundoContainer, text="", font=self.fontePadrao)
        self.mensagemsegundo["width"] = 200
        self.mensagemsegundo['bg'] = '#025398'
        self.mensagemsegundo.pack()

        self.mensagemterceiro = Message(self.primeiroContainer, text="", font=self.fontePadrao)
        self.mensagemterceiro["width"] = 200
        self.mensagemterceiro['bg'] = '#025398'
        self.mensagemterceiro['fg']='red'
        self.mensagemterceiro.pack()
        self.mensagemterceiro2 = Message(self.primeiroContainer, text="", font=self.fontePadrao)
        self.mensagemterceiro2["width"] = 200
        self.mensagemterceiro2['bg'] = '#025398'
        self.mensagemterceiro2['fg'] = 'yellow'
        self.mensagemterceiro2.pack()

        self.mensagemquinto = Message(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagemquinto["width"] = 200
        self.mensagemquinto['bg'] = '#025398'
        self.mensagemquinto.place(relx=1, x=-2, y=2, anchor=NE)
        self.mensagemquinto.pack()


        self.msgteste = Message(self.quartoContainer, text="", font=self.fontePadrao)
        self.msgteste["width"] = 200
        self.msgteste['bg'] = '#025398'
        self.msgteste.pack()

        self.msg = Message(self.setimoContainer, text="", font=self.fontePadrao)
        self.msg.place(x=90, y=10)
        self.buto = Button(text="Selecionar Arquivo", bg='white', command=self.arquivopc).place(x=250, y=350)

        #self.lb = Label(self.setimoContainer, text="", width=150)
        #self.lb.pack()
        self.texto = Text(self.terceiroContainer, height=25, width=90)
        self.texto.insert(INSERT, '')
        self.texto.pack(side='right')
        #self.ent = Entry(self.segundoContainer, text="")
        #self.ent["width"] = 25

#        self.ent.pack(side=LEFT)

        self.conectar()

    def conectar(self):

        print("Conectando ao Servidor . . .")
        try:
            ip = "192.168.43.187"

            s.connect((ip, 9999))
            print("conect")
            self.mensagemterceiro2["text"] = "Servidor Conectado!"

        except Exception as e:
            print("erro", e)
            self.mensagemterceiro["text"] = "Servidor não Conectado!"
            #self.lb["text"] = "Elves sousa"
            #self.texto.insert(INSERT,'ajsjdsajdjh')

            criptografia.teste()
            #self.v['text'] = "deu certo
            #self.msg["text"]="aaaaaaaaaaaaaaaaaa"
            print("\n>> Impossivel Conectar")
            #self.a= "deu certo"

    def arquivopc(self):

        # Tk().withdraw() # Isto torna oculto a janela principal
        filename = askopenfilename()  # Isto te permite selecionar um arquivo
        document = Document(filename)
        t = ' '
        espaco = '\n  '
        for paragraph in document.paragraphs:
            t = t + espaco + paragraph.text
            #self.mensagemquinto["text"] = paragraph.text


        print("texto: ", t)
        self.texto.insert(INSERT, '\nTEXTO: ')
        self.texto.insert(INSERT, t)
        self.texto.insert(INSERT, '\n\n')

        localtime = strftime("%H:%M:%S", gmtime())
        encript = criptografia.encripta(t, 3)
        desckle = pickle.dumps(encript)  # Cria uma serializacao a partir de do texto encriptografado
        s.send(desckle)  # Envia o texto

        receb = s.recv(1024).decode()  # Recebe os computadores ativos
        print('Recebeu os computadores ativos')

        ''''-----For para mostar os pcs ativos----'''
        num = []
        for i in range(len(receb)):
            try:
                int(receb[i])
                num.append(int(receb[i]))
            except:
                pass
        print("PC ativo: ", num)
        self.texto.insert(INSERT, '\n\nPCs Ativos:')
        self.texto.insert(INSERT, num)
        self.texto.insert(INSERT, '\n\n')

        l = []
        try:
           # print("Entrou no try--------")

            recibido2 = s.recv(4096)
            #print("Recebeuuuuuuuu-------")
            if (recibido2 == None):
                print('Nenhuma palavra processada errada')
                self.texto.insert(INSERT, '\nNenhuma palavra processada errada!')
            else:
                #print('Recebido: ', recibido2)
                #print('Tipo Recebido:', type(recibido2))
                picklebytes = pickle.loads(recibido2)
                palavrasErradas = criptografia.decripta(picklebytes, 3)
                print("Palavras Erradas: ", palavrasErradas)
                self.texto.insert(INSERT, '\nPalavras Erradas: ')
                self.texto.insert(INSERT, palavrasErradas)
                self.texto.insert(INSERT, '\n\n')
                # print("--Aux tipo: ", type(auxiliar))

                for i in range(len(num)):
                    print('Palavras Erradas: pc {}'.format(num[i]), palavrasErradas[i])
                    self.texto.insert(INSERT, '\n\nPalavras Erradas: PC ')
                    self.texto.insert(INSERT, num[i])
                    self.texto.insert(INSERT, '\n')
                    self.texto.insert(INSERT, palavrasErradas[i])





        except E as e:
            print('Erro ao receber as palavras, ', e)



root = Tk()
root.title("Tela Inicial")
root['bg'] = '#025398'
root.geometry("1350x750+0+0")
imagem = tk.PhotoImage(file='show2.png')
w = tk.Label(root, image=imagem, bg='#025398').place(x=180,y=200)


Application(root)
root.mainloop()
s.close()


