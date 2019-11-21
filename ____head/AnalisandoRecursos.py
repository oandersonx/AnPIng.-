import socket

def analisandoRecursos(soc,status):
   try:
        #print('Status: AR', status)
        novostatus = []
      
        
        for h in status:
            if (h != '*'):
                novostatus.append(h)
               
        
        
        msddd = []
        au = 0
       
        for i in novostatus:
            msddd.insert(au, soc[i].recv(1024).decode()) # Recebe o uso da CPU livre
            au += 1
        print('Novo Status:', novostatus)
       
        
        '''----Convertendo a lista msddd para inteiro----'''
        
        cpu_livre = []
        for i in msddd:
            cpu_livre.append(float(i))
            
        
    
        '''----Imprimindo uso da CPU Livre----'''
        print('-------------------------')
       
        print('Uso da CPU Livre')
        aux = 0
        for i in range(len(cpu_livre)):
            print('Nó',novostatus[aux] + 1,':', cpu_livre[i],'%')
            aux +=1
        return cpu_livre
   except Exception as e:
       print('Erro em AnalisandoRecursos', e)
       
   
    
    
    
  