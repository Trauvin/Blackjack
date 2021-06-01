import random

def mistura_baralho():
    
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2', '3', '4', '5', '6', '7', '8' '9', '10', 'J', 'K', 'Q', 'A'}
    baralho = []

    # cria um baraalho de 52 cartas 9*4(número e naipes) + 4*4 (cartas especiais e naipes)
    for naipe in naipes:
        for valor in valores:
            baralho.append(valor + ' ' + naipe)

    # mistura o baralho
    random.shuffle(baralho)

    return baralho
    