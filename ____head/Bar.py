def bar(janela, pgbar):
    import time
    pgbar['value'] = 20
    janela.update_idletasks()
    time.sleep(1)
    
    pgbar = 40
    janela.update_idletasks()
    time.sleep(1)
    
    pgbar['value'] = 50
    janela.update_idletasks()
    time.sleep(1)
    
    pgbar['value'] = 60
    janela.update_idletasks()
    time.sleep(1)
    
    pgbar['value'] = 80
    janela.update_idletasks()
    time.sleep(1)
    pgbar['value'] = 100
   