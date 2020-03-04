'''
6. Mostre a data e hora atual
'''

from datetime import datetime

agora = datetime.now()
print(f'{agora.strftime("%d/%m/%Y %H:%M:%S")}')
