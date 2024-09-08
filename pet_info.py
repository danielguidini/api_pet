import json

def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    while True:
        nome = input("Nome do pet: ")
        if nome.strip():
            break
        else:
            print("Por favor, insira um nome válido para o pet.")

    # Coleta do tipo do pet, garante que o pet seja definido por seu tipo
    print("Selecione o tipo do pet:")
    print("1. Canidéos")
    print("2. Felinos")
    print("3. Aves")
    print("4. Répteis & Anfíbios")

    tipo_options = {
        "1": "Canidéos",
        "2": "Felinos",
        "3": "Aves",
        "4": "Répteis & Anfíbios"
    }

    while True:
        tipo = input("Tipo do pet (digite o número da opção): ")
        if tipo in tipo_options:
            tipo = tipo_options[tipo]
            break
        else:
            print("Por favor, insira um número válido para o tipo do pet.")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")
    print(f"Tipo: {tipo}")

    # Armazenar as informações do pet em um dicionário
    pet_info = {
        "nome": nome,
        "tipo": tipo,
        "idade": idade,
        "peso": peso
    }

    # Salvar as informações do pet em um arquivo
    try:
        with open("pet_info.json", "w") as arquivo:
            json.dump(pet_info, arquivo)
    except Exception as e:
        print(f"Erro ao salvar as informações do pet: {e}")

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()