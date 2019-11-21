def divideTexto(mensagem, qtd_comp):
    auxiliar = mensagem.split()
    
    n = qtd_comp
    textoQuebrado = []
    len_l = len(auxiliar)
    for i in range(n):
        start = int(i * len_l / n)
        end = int((i + 1) * len_l / n)
        textoQuebrado.append(auxiliar[start:end])
    
    return textoQuebrado



