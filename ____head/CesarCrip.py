
def encripta(mensagemOuLista, chave):
    
    palavrasEncriptografadas = []
   
    if(type(mensagemOuLista) == list):
       #Lista
        for lista in mensagemOuLista:
            cripto = ''
            for letra in lista:
                if 'A' <= letra <= 'Z':
                    if ord(letra) + chave > ord('Z'):
                        cripto += chr((ord('A') + chave - (ord('Z') + 1 - ord(letra))))
                    else:
                        cripto += chr(ord(letra) + chave)
                elif 'a' <= letra <= 'z':
                    if ord(letra) + chave > ord('z'):
                        cripto += chr((ord('a') + chave - (ord('z') + 1 - ord(letra))))
                    else:
                        cripto += chr(ord(letra) + chave)
                else:
                    cripto += letra
                    
            palavrasEncriptografadas.append(cripto)
       
        return palavrasEncriptografadas
    #letra
    else:
        cripto = ''
        for letra in mensagemOuLista:
            if 'A' <= letra <= 'Z':
                if ord(letra) + chave > ord('Z'):
                    cripto += chr((ord('A') + chave - (ord('Z') + 1 - ord(letra))))
                else:
                    cripto += chr(ord(letra) + chave)
            elif 'a' <= letra <= 'z':
                if ord(letra) + chave > ord('z'):
                    cripto += chr((ord('a') + chave - (ord('z') + 1 - ord(letra))))
                else:
                    cripto += chr(ord(letra) + chave)
            else:
                cripto += letra
                
        
            
    return cripto
        

'''----------------------------------------------------------------------'''


def decripta(mensagemOuLista, chave):
   
    palavrasDescriptografadas = []
    
    if (type(mensagemOuLista) == list):
        for lista in mensagemOuLista:
            cripto = ''
            for letra in lista:
                if 'A' <= letra <= 'Z':
                    if ord(letra) - chave < ord('A'):
                        cripto += chr(ord('Z') - (chave - (ord(letra) + 1 - ord('A'))))
                    else:
                        cripto += chr(ord(letra) - chave)
                elif 'a' <= letra <= 'z':
                    if ord(letra) - chave < ord('a'):
                        cripto += chr(ord('z') - (chave - (ord(letra) + 1 - ord('a'))))
                    else:
                        cripto += chr(ord(letra) - chave)
                else:
                    cripto += letra
            palavrasDescriptografadas.append(cripto)
            
        return palavrasDescriptografadas
    else:
        #letra
        cripto = ''
        for i in mensagemOuLista:
            if 'A' <= i <= 'Z':
                if ord(i) - chave < ord('A'):
                    cripto += chr(ord('Z') - (chave - (ord(i) + 1 - ord('A'))))
                else:
                    cripto += chr(ord(i) - chave)
            elif 'a' <= i <= 'z':
                if ord(i) - chave < ord('a'):
                    cripto += chr(ord('z') - (chave - (ord(i) + 1 - ord('a'))))
                else:
                    cripto += chr(ord(i) - chave)
            else:
                cripto += i
        return cripto

