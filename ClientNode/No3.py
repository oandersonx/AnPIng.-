import socket, AnalisaPalavra
import json
import psutil



# usando a conexão socket
st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# recebendo a conexão ip nessa porta.
st.bind(("", 1488))

# aceitando apenas uma conexão no scket
st.listen(1)

# retornando dois valores, o ip e a porta para uma nova conexão.
sct, addrt = st.accept()
print("Entrou")


while True:
    try:
        # Recebendo mensagens do cliente. O método recv recebe dados e 1024 é a quantidade de bytes

        a = 'Computador Ativo'
        sct.send(a.encode())
        
        cpu_livre = psutil.cpu_times_percent().idle
        sct.send(str(cpu_livre).encode())
        
        threshold = sct.recv(1024).decode()
        
        
        print('Threshold:',threshold)
       
        '--- Convertendo threshold para inteiro----'
        threshold = int(threshold)
       
        print(type(threshold))
        '''---Recebendo lista de palavras a serem analisadas-----'''
        mensagem = sct.recv(1024).decode()
        print('MENSAGEM RECEBIDA...', mensagem)
        lista = mensagem.split()
        print('Lista:', lista)
        print('Palavras capturadas no texto: ', lista[:threshold])
        print('Quantidade de palavras: ', len(lista[:threshold]))
        print('Tipo Lista Threshold:', type(lista[:threshold]))
        palavrasCorretas = AnalisaPalavra.analisaPalavra(lista[:threshold])
        print('Tipo de palavras corretas:', type(palavrasCorretas))
        j = ','.join(palavrasCorretas).replace(',', ' ')
        
        if(j == None):
            print('Lista de Palavras Erradas:', 0)
        else:
            print('Lista de Palavras Erradas:', j)
            
        sct.sendall(j.encode())#retornando a mensagem pro servidor(head)
        print('Enviou ao HeadNode')
        break

    except Exception as e:
        print("Ocorreu un error ", e)
        break

sct.close()
st.close()
print('Enrerrou')