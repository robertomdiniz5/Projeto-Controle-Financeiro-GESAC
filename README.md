## General description


*  This project was developed during an internship at the Ministry of Communications of Brazil with the goal of integrating spreadsheets from various sectors associated with GESAC Financial Control. The purpose of this integration was to support WIFI-BRAZIL, an initiative aimed at providing internet connectivity to public schools. 

### Final gol: 

* Pass the data to the PowerBI. To create a model that can integrate  different sectors linked to GESAC Financial Control.

>[PowerBI](https://github.com/s33ding/financial_control_wifi-BR/blob/main/bi_financial.pbix)
![Mardown Logo](https://github.com/s33ding/financial_control_wifi-BR/blob/main/Data_Source/BI.PNG)

### Spreadsheets: 

* Control of Parliamentary Amendments

>[Emendas2021_resumo.xlsx](https://github.com/s33ding/financial_control_wifi-BR/blob/main/Data_Source/Emendas2021_resumo.xlsx)

* Control of Credit Note and Commitment

>[Controle de Empenhos e NC 2022.xlsm](https://github.com/s33ding/financial_control_wifi-BR/blob/main/Data_Source/Controle%20de%20Empenhos%20e%20NC%202022.xlsm)
---
### Challenges:

* Business Understanding: preparation of formal documents for understanding the data based on the initial stages of CRISP-DM management. Data dictionary creation.

* Make recommendations, so that future data could be inserted atomically following database normalizations.

* Advanced data ingestion for reading excel files with different formats.
>[financial_control_wifi-BR.py](https://github.com/s33ding/financial_control_wifi-BR/blob/main/financial_control_wifi-BR.py)

* Create a primary key for the worksheets with the names of Deputies, and Senators to circumvent the inconsistency of the data entered by different professionals from the Ministry of Communications. To then do the modeling of Financial Control within PowerBI.

* Create an algorithm that would make a comparison of entities to fill in the civil name of all Parliamentarians. This filling was done based on a control of all the different parliamentary names given in a dataset with the civil name of each one (Spreadsheet: [Proponentes.xlsx](https://github.com/s33ding/financial_control_wifi-BR/blob/main/Data_Source/Proponentes.xlsx)), a bank created by me from an extraction of the Open Government Data.

__Public Data__
  * [CAMERA](https://dadosabertos.camara.leg.br/)
  * [SENADO](https://www12.senado.leg.br/dados-abertos)
