![Mardown Logo](https://www.gov.br/mcom/pt-br/acesso-a-informacao/acoes-e-programas/wi-fi-brasil/wi-fi-brasil-1/@@collective.cover.banner/c5b4edcd-e164-4632-ad98-d37765684777/@@images/90c578cf-47c6-4bec-9773-44afc3c4c2db.png)

## General description

* Project made by me to integrate spreadsheets from different sectors linked to GESAC Financial Control (WIFI-BRAZIL that aims to bring the connection to public schools). To then pass the data to the PowerBI.

### Spreadsheets: 

* Control of Controle das emendas Parlamentares (Parliamentary Amendments), Control of Credit Note and Commitment.

Challenges:

- Business Understanding: preparation of formal documents for understanding the data based on the initial stages of CRISP-DM management. Data dictionary creation.

-Advanced data ingestion for reading excel files with different formats.

-Create a primary key for the worksheets with the names of Deputies, and Senators to circumvent the inconsistency of the data entered by different professionals from the Ministry of Communications. To then do the modeling of Financial Control within PowerBI.

-Create an algorithm that would make a comparison of entities to fill in the civil name of all Parliamentarians. This filling was done based on a control of all the different parliamentary names given in a dataset with the civil name of each one (Spreadsheet: Proponents), a bank created by me from an extraction of the Open Government Data.

-Make recommendations, so that future data could be inserted atomically following database normalizations.

----------------------------------------------------------------------------
Projeto feito por mim para integrar planilhas de diferentes setores ligadas ao Controle Financeiro GESAC (WIFI-BRASIL que visa levar conexão às escolas públicas). Para depois serem passados para o PowerBI.

Planilhas: Controle de Emendas Parlamentares, Controle de Nota de Crédito e Empenho.

Desafios: 

-Entendimento do Negócio: elaboração dos documentos formais de entendimento dos dados com base nas etapas iniciais de gestão do CRISP-DM. Criação do dicionário de dados.

-Ingestão avançada de dados para leitura de arquivos excel com diferentes formatações.

-Criar uma chave primária para as planilhas com os nome cívil dos Deputados, Senadores  de maneira a driblar a inconssistência dos dados inseridos por diferentes profissionais do Ministério das Comunicaçoẽs. Para depois fazer a modelagem do Controle Financeiro dentro do PowerBI.

-Criar um  algoritmo que fizesse uma comparação das entidades de maneira a preencher o nome cívil de todos os Parlamentares. Esse preenchimento era feito com base num controle de todos os diferentes nomes dados parlamentares num dataset com o nome cívil de cada um(Planilha:Proponentes), banco esse criado por mim a partir de uma extração dos Dados Abertos do Governo. 

-Fazer recomendações, para que dados futuros fossem inseridos de forma atômicas seguindo normalizações de banco de dados.
