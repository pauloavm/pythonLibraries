import time

tempo_limite = int(input("Digite o tempo limite em segundos: "))

print("Temporizador de Tarefas")
print(f"Você tem {tempo_limite} segundos para completar a tarefa.")

for segundos_restantes in range(tempo_limite, 0, -1):
    print(f"Tempo restante: {segundos_restantes} segundos")
    time.sleep(1)  # Aguardar 1 segundo

print("Tempo esgotado! Tarefa concluída.")
