from spellchecker import SpellChecker



def analisaPalavra(msg):
    
    spell = SpellChecker()
    
    erradas = spell.unknown(msg)
   
    return list(erradas)