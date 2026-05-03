# Importa as bibliotecas necessárias
from colorama import Fore, Style, init  # Fore = cores do texto
import random  # Biblioteca para gerar números aleatórios

# Inicializa o colorama (necessário principalmente no Windows)
init(autoreset=True)  # autoreset=True faz a cor voltar ao normal automaticamente

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função responsável por definir a cor com base no nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED      # Nível crítico → vermelho
    elif nivel == 2:
        return Fore.YELLOW   # Nível baixo → amarelo
    elif nivel == 3:
        return Fore.GREEN    # Nível médio → verde
    elif nivel == 4:
        return Fore.CYAN     # Nível alto → ciano
    elif nivel == 5:
        return Fore.BLUE     # Nível muito alto → azul
    else:
        return Fore.WHITE    # Caso inválido → branco padrão

# Função responsável por exibir o status do reservatório
def exibir_status(nivel):
    # Verifica se o nível está dentro do intervalo válido
    if 1 <= nivel <= 5:
        cor = definir_cor(nivel)  # Chama a função que define a cor
        mensagem = niveis[nivel - 1]  # Acessa a lista (ajustando índice)
        print(cor + mensagem)  # Exibe a mensagem com a cor correspondente
    else:
        # Caso o nível seja inválido
        print(Fore.WHITE + "Nível inválido!")

# Gera um nível aleatório entre 1 e 5
nivel_aleatorio = random.randint(1, 5)

# Exibe um título no terminal
print("🔎 Monitoramento do reservatório:\n")

# Chama a função para exibir o status com base no nível gerado
exibir_status(nivel_aleatorio)