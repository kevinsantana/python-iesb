'''
2. Converta um número de segundos para horas, minutos e segundos.
'''

segundos = int(input())
print(f"{segundos // 3600}h{(segundos % 3600) // 60}m{((segundos % 3600) % 60)}s")
