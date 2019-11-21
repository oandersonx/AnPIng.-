
from math import floor


def balanceamento(soc, status,cpu_livre, textoQuebrado):
   
    qtd_palavras = []
    for i in range(len(cpu_livre)): #cpu_livre é uma lista contendo o uso do cpu Livre de cada nó
        
        tam = len(textoQuebrado[i])
        #print('Tamanho texto quebrado pc {}'.format(i+1), tam)
        a = cpu_livre[i]/100
        b =  a * tam
        fl = floor(b)
        qtd_palavras.append(fl)
        print('-------------------------------------')
       
  
        
    print('Limite(s):', qtd_palavras)

   

   

    '''----- Envio aos Nodes ----'''

    novostatus = []
    for h in status:
        if (h != '*'):
            novostatus.append(h)

    aux = 0
    '''---For para enviar os limites aos Nodes---'''
    for i in novostatus:
        soc[i].send(str(qtd_palavras[aux]).encode())
        print('Envio limite ao Nó {} '.format(i + 1))
        aux += 1
        
        
    
  
    
    return qtd_palavras