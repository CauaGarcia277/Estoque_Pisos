# Estoque De Pisos
Sistema para estoque de pisos com CRUD simples, utilizando a linguaguem Python e banco de dados MySQL, é um projeto academico pessoal para estudo e treinamento. O sistema consiste em gerenciar um estoque de pisos e suas especificações, será possivel saber quantos pisos tem no estoque e quais foram vendidos em respectivos dias, dashboards utilizando PowerBI para melhor vizualização dos dados, utilização de IA regressiva para previsão simples de quais dias o estoque pode acabar

# Estoque_v1
O Estoque_v1 foi implementado um CRUD simples em Python (Insert, Delete, Select e Rename), definindo o banco de dados e pequenas regras para o funcionamento do esqueleto do projeto

    Estrutura
        A estrutura foi separa em:

    -crud.py: O CRUD do projeto
    -db.py: Conexão com o banco de dados
    -func.py: Definições de funções básicas para o funcionamento da versão_v1
    -main.py: Ainda robusta, mas o inicial para a vizualização


    Erros encontrados
        Durante a codificação aprendi que a data no banco de dados é em uma formatação diferente, para resolver:
    
    -def data no func.py, onde o usuario digita o padrão DD/MM/AAAA, e a função usando a biblioteca datetime faz a transcrição para AAAA/MM/DD para ser aceito no banco de dados

    Melhorias feitas
        Validação de input e dados em geral

    
    Melhorias futuras
        Para o Estoque_v2 terá uma separação correta em cada setor do CRUD, visando deixar o código mais claro
        e de facil manutenção. Melhoria no código do banco de dados, pois o banco de dados foi criado
        manualmente e agora com estudos recentes da faculdade será reformulado por código para melhor
        entendimento. Terá a validação de ID, chaves primárias e secundarias.


