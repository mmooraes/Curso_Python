# CORES NO TERMINAL - AULA 11

#Padrão ANSI (escape sequence)
#Tudo em ANSI começa com \ + cod
# \033[style; text; back; m] nesse caso precisa indicar, estilo, cor do texto e codigo de fundo 
# exemplo: \033[0;33;44m]

"""Styles que funcionam bem no Python são: 
0 = none
1 = Negrito
4 = Sublinhado
7 = Negative
"""

""" TEXT que funcionam bem no Python são: 
30 = Branco
31 = Vermelho
32 = verde
33 = Amarelo
34 = Azul
35 = Magenta
36 = Ciano
37 = Cinza
"""

""" BACK que funcionam bem no Python são: 
40 = Branco
41 = Vermelho
42 = verde
43 = Amarelo
44 = Azul
45 = Magenta
46 = Ciano
47 = Cinza
"""

