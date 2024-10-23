"""Gera o mapa do labirinto com emojis de blocos coloridos"""
import emoji
a=	emoji.emojize(':orange_square:')
b=emoji.emojize(':white_large_square:')
Saída=emoji.emojize(':red_square:')
Chegada =emoji.emojize(":green_square:")

l1=Saída+b+a*8
l2=a+ b+a+6*b+a
l3=a+ 3*b+a*4+b+a
l4=a+b+a*2+3*b+a+b+a
l5=a+b+a*2+b+3*a+b+a
l6=a+2*b+a+b*5+a
l7=2*a+b+a+b+2*a+b+2*a
l8=a+2*b+a+b+2*a+b+2*a
l9=a+b+a+4*b+3*a
l10=a+2*b+3*a+2*b+2*a
l11=a*7+2*b+Chegada
labirinto=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]

