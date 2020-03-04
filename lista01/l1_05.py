'''
5. Liste todos os arquivos no diretório informado
'''

import os


diretorio = input()
for _, _, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        print(arquivo)
