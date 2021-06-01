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

def distribui_carta(baralho, participante):

    carta = baralho.pop()
    participante.append(carta)
    return carta

def total(mao):

    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
            '9': 9, '1': 10, 'J': 10, 'K': 10, 'Q': 10, 'A': 11 }

    resultado = 0
    ases = 0

    for carta in mao:
        resultado += valores[carta[0]]
        if carta[0] == 'A':
            ases += 1

    while resultado > 21 and ases > 0:
        resultado -= 10
        ases -= 1

    return resultado

def compara_maos(casa, jogador):

    total_casa, total_jogador = total(casa), total(jogador)

    if total_casa > total_jogador:
        print("Você perdeu!")
    elif total_casa < total_jogador:
        print("Você venceu!")
    elif total_casa == 21 and 2 == len(casa) < len(jogador):
        print("Você perdeu.")
    elif total_jogador == 21 and 2 == len(jogador) < len(casa):
        print("Você venceu!")
    else:
        print("Empatou")