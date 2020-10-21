import pyttsx3
engine = pyttsx3.init()
from spellchecker import SpellChecker

spell = SpellChecker()
engine.setProperty('rate', 100)

def correct(word):
    print("input: " + word)
    corrected = spell.correction(word)  #removes , and capitalization
    print(corrected)
    return corrected

def say(text):
    engine.say(text)
    engine.runAndWait()
    
def saySentence(text):
    sentence = ""
    for i in range(0,len(text)):
        #sentence += correct(text[i]) + " "
        sentence += text[i] + " "  
    print(sentence)
    say(sentence)
    
    
#saySentence(["pnnciples", "design.", "As", "you", "study", "design", "pattems", "our", "unde", "of"])
