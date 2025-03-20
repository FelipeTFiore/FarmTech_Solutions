import csv
import subprocess


caminho_csv = r"C:\Users\Felipe\Desktop\FarmTech_Solutions\dados_culturas.csv"
caminho_rscript = r"C:\Program Files\R\R-4.4.3\bin\x64\Rscript.exe"
caminho_script_r = r"C:\Users\Felipe\Desktop\FarmTech_Solutions\calcular_estatisticas.R"  # Caminho corrigido

# Função para entrada de dados
def entrada_dados(dados):
    print("\n--- Entrada de Dados ---")

    # Loop para validar a cultura
    while True:
        cultura = input("Digite a cultura (café ou milho): ").lower()
        if cultura in ["café", "milho"]:
            break
        else:
            print("Cultura inválida! Digite 'café' ou 'milho'.")

    # Coleta a base e a altura (garantindo que sejam números positivos)
    while True:
        try:
            base = float(input("Digite a base da área plantada (em metros): "))
            if base <= 0:
                print("A base deve ser um número positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número.")

    while True:
        try:
            altura = float(input("Digite a altura da área plantada (em metros): "))
            if altura <= 0:
                print("A altura deve ser um número positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número.")

    # Armazena os dados em um dicionário (ou lista)
    dados.append({
        "cultura": cultura,
        "base": base,
        "altura": altura,
        "insumo": None  # Inicializa o campo de insumo como None
    })

    print("Dados salvos com sucesso!")
    return dados


# Função para saída de dados
def saida_dados(dados):
    print("\n--- Saída de Dados ---")
    if len(dados) == 0:  # Verifica se a lista está vazia
        print("Nenhum dado cadastrado ainda.")
    else:
        print("Dados cadastrados:")
        for i, dado in enumerate(dados, start=1):  # Percorre a lista com índice
            print(f"\nCultura {i}:")
            print(f"  Cultura: {dado['cultura']}")
            print(f"  Base: {dado['base']} metros")
            print(f"  Altura: {dado['altura']} metros")
            if dado['insumo']:  # Exibe os dados de insumo, se existirem
                print(f"  Insumo: {dado['insumo']['produto']}")
                print(f"    Quantidade total: {dado['insumo']['quantidade_mL']} mL")
                print(f"    Quantidade total: {dado['insumo']['quantidade_litros']:.2f} litros")


# Função para atualizar dados
def atualizar_dados(dados):
    print("\n--- Atualizar Dados ---")
    if len(dados) == 0:  # Verifica se a lista está vazia
        print("Nenhum dado cadastrado ainda.")
    else:
        print("Culturas cadastradas:")
        for i, dado in enumerate(dados, start=1):  # Exibe as culturas cadastradas
            print(f"{i}. {dado['cultura']} (Base: {dado['base']} m, Altura: {dado['altura']} m)")

        # Coleta a escolha do usuário
        try:
            indice = int(input("Digite o número da cultura que deseja atualizar: ")) - 1
            if 0 <= indice < len(dados):  # Verifica se o índice é válido
                # Coleta os novos dados
                print(f"\nAtualizando dados para {dados[indice]['cultura']}:")
                nova_base = float(input("Digite a nova base (em metros): "))
                nova_altura = float(input("Digite a nova altura (em metros): "))

                # Atualiza os dados na lista
                dados[indice]['base'] = nova_base
                dados[indice]['altura'] = nova_altura

                print("Dados atualizados com sucesso!")
            else:
                print("Número inválido! Tente novamente.")
        except ValueError:  # Trata erros de entrada (ex.: usuário digita texto em vez de número)
            print("Entrada inválida! Digite um número.")
    return dados


# Função para deletar dados
def deletar_dados(dados):
    print("\n--- Deletar Dados ---")
    if len(dados) == 0:  # Verifica se a lista está vazia
        print("Nenhum dado cadastrado ainda.")
    else:
        print("Culturas cadastradas:")
        for i, dado in enumerate(dados, start=1):  # Exibe as culturas cadastradas
            print(f"{i}. {dado['cultura']} (Base: {dado['base']} m, Altura: {dado['altura']} m)")

        # Coleta a escolha do usuário
        try:
            indice = int(input("Digite o número da cultura que deseja deletar: ")) - 1
            if 0 <= indice < len(dados):  # Verifica se o índice é válido
                # Remove os dados da lista
                cultura_removida = dados.pop(indice)
                print(f"Dados da cultura '{cultura_removida['cultura']}' foram deletados com sucesso!")
            else:
                print("Número inválido! Tente novamente.")
        except ValueError:  # Trata erros de entrada (ex.: usuário digita texto em vez de número)
            print("Entrada inválida! Digite um número.")
    return dados


# Função para cálculo de manejo de insumos
def calcular_insumos(dados):
    print("\n--- Cálculo de Manejo de Insumos ---")
    if len(dados) == 0:  # Verifica se a lista está vazia
        print("Nenhum dado cadastrado ainda.")
    else:
        print("Culturas cadastradas:")
        for i, dado in enumerate(dados, start=1):  # Exibe as culturas cadastradas
            print(f"{i}. {dado['cultura']} (Base: {dado['base']} m, Altura: {dado['altura']} m)")

        # Coleta a escolha do usuário
        try:
            indice = int(input("Digite o número da cultura que deseja calcular o insumo: ")) - 1
            if 0 <= indice < len(dados):  # Verifica se o índice é válido
                # Coleta os dados do insumo
                produto = input("Digite o nome do produto (ex.: fosfato): ")
                quantidade_por_metro = float(input("Digite a quantidade necessária por metro (em mL): "))
                numero_ruas = int(input("Digite o número de ruas da lavoura: "))

                # Calcula a quantidade total de insumo em mL
                base = dados[indice]['base']
                quantidade_total_mL = quantidade_por_metro * base * numero_ruas

                # Converte mL para litros
                quantidade_total_litros = quantidade_total_mL / 1000

                # Armazena os dados do insumo no dicionário da cultura
                dados[indice]['insumo'] = {
                    "produto": produto,
                    "quantidade_mL": quantidade_total_mL,
                    "quantidade_litros": quantidade_total_litros
                }

                # Exibe o resultado
                print(f"\nQuantidade total de {produto} necessária para {dados[indice]['cultura']}:")
                print(f"  {quantidade_total_mL} mL")
                print(f"  {quantidade_total_litros:.2f} litros")  # Exibe com 2 casas decimais
            else:
                print("Número inválido! Tente novamente.")
        except ValueError:  # Trata erros de entrada (ex.: usuário digita texto em vez de número)
            print("Entrada inválida! Digite um número.")
    return dados


# Função para exibir a área calculada
def exibir_area_calculada(dados):
    print("\n--- Área Calculada ---")
    if len(dados) == 0:  # Verifica se a lista está vazia
        print("Nenhum dado cadastrado ainda.")
    else:
        print("Áreas calculadas:")
        for i, dado in enumerate(dados, start=1):  # Percorre a lista com índice
            area = dado['base'] * dado['altura']
            print(f"\nCultura {i}: {dado['cultura']}")
            print(f"  Área: {area:.2f} metros quadrados")


# Função para salvar dados em CSV
def salvar_dados_csv(dados, nome_arquivo="C:/Users/Felipe/Desktop/FarmTech_Solutions/dados_culturas.csv"):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:  # Adicionado encoding="utf-8"
        writer = csv.DictWriter(arquivo, fieldnames=["cultura", "base", "altura"])
        writer.writeheader()
        for dado in dados:
            writer.writerow({
                "cultura": dado["cultura"],
                "base": dado["base"],
                "altura": dado["altura"]
            })
    print(f"Dados salvos no arquivo {nome_arquivo}")


# Função para calcular estatísticas em R
def calcular_estatisticas_r():
    try:
        # Executa o script R
        resultado = subprocess.run(
            [caminho_rscript, caminho_script_r],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8"  # Força a codificação UTF-8
        )
        print(resultado.stdout)  # Exibe a saída do R
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o script R:")
        print(e.stderr)  # Exibe a mensagem de erro do R


# Menu principal
dados = []  # Lista para armazenar os dados

while True:
    print("\n--- Menu ---")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Calcular insumos")
    print("6. Exibir área calculada")
    print("7. Calcular estatísticas (R)")
    print("8. Sair")

    # Captura a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # Trata a opção escolhida
    if opcao == "1":
        dados = entrada_dados(dados)
    elif opcao == "2":
        saida_dados(dados)
    elif opcao == "3":
        dados = atualizar_dados(dados)
    elif opcao == "4":
        dados = deletar_dados(dados)
    elif opcao == "5":
        calcular_insumos(dados)
    elif opcao == "6":
        exibir_area_calculada(dados)
    elif opcao == "7":
        salvar_dados_csv(dados)
        calcular_estatisticas_r()
    elif opcao == "8":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")