def chr_remove(recibido, carac):
    
    nova_string = recibido
    for x in carac:
        nova_string = nova_string.replace(x, '')
    
    return nova_string