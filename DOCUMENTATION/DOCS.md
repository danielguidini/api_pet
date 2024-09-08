## Documentação de api_pet.py
### Visão Geral
O script api_pet.py é um programa em Python que coleta e armazena informações sobre um pet. Ele solicita ao usuário que insira o nome, tipo, idade e peso do pet e, em seguida, armazena essas informações em um arquivo JSON.

## Funções

### coletar_informacoes_pet()
Essa função coleta e armazena informações sobre um pet. Ela consiste nas seguintes etapas:

### Coleta do nome do pet: 
Solicita ao usuário que insira o nome do pet, garantindo que um nome válido seja inserido.

### Coleta do tipo do pet: 
Solicita ao usuário que selecione o tipo do pet a partir de uma lista de opções (Canidéos, Felinos, Aves, Répteis & Anfíbios).

### Coleta da idade do pet: 
Solicita ao usuário que insira a idade do pet, garantindo que um número inteiro válido seja inserido.

### Coleta do peso do pet: 
Solicita ao usuário que insira o peso do pet, garantindo que um número flutuante válido seja inserido.

### Exibição das informações do pet: 
Exibe as informações coletadas sobre o pet.

### Armazenamento das informações do pet: 
Armazena as informações coletadas em um dicionário e salva em um arquivo JSON chamado pet_info.json.
## Tratamento de Erros
### O script inclui tratamento de erros para os seguintes cenários:

Entrada inválida para nome, tipo, idade ou peso do pet.

Erro ao salvar as informações do pet no arquivo JSON.

Formato do Arquivo JSON.