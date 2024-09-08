import json
def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    while not nome.strip():
        print("Por favor, insira um nome válido para o pet.")
        nome = input("Nome do pet: ")
    
    # Coleta do tipo do pet, garante que o pet seja definido por seu tipo
    print("Selecione o tipo do pet:")
    print("1. Canidéos")
    print("2. Felinos")
    print("3. Aves")
    print("4. Répteis & Anfíbios")


    while True:
        tipo = input("Tipo do pet (digite o número da opção): ")
        if tipo in ["1", "2", "3", "4"]:
            if tipo == "1":
                tipo = "Canidéos"
            elif tipo == "2":
                tipo = "Felinos"
            elif tipo == "3":
                tipo = "Aves"
            elif tipo == "4":
                tipo = "Répteis & Anfíbios"

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
    with open("pet_info.json", "w") as arquivo:
            json.dump(pet_info, arquivo)

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
