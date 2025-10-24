"""DESAFIO 021 - AULA 08
FAÇA UM PROGRAMA EM PY QUE ABRA E REPRODUZA UM AUDIO DE ARQUIVO EM MP3
"""

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(r"C:\Users\Matheus Moraes\Downloads\ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
