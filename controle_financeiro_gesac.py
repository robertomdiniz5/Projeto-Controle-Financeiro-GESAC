import pandas as pd
import numpy as np 
import regex as re
from datetime import datetime
from time import time
from time import sleep
from math import ceil
from datetime import timedelta
import unicodedata  
import os
from IPython.display import clear_output

#%%
#df_folders
lst_folders_and_files = [
    ('FINANCEIRO','\GESAC\GESAC_2017\ADMPP'),
    ('SISGESAC',None)
    ]

folder = [folder for (project,folder) in lst_folders_and_files]
project = [project for (project,folder) in lst_folders_and_files]
df_folder = pd.DataFrame({'project':project,'folder':folder});df_folder
#%%
def get_sheets_names(file):
    """
    This function gets the names of the sheets inside the excel file

    Args: The file which you want extract the name of the sheet inside of it.

    Returns: The sheets names 
    """
    excel = pd.ExcelFile(file)
    return excel.sheet_names  #see all sheet names

def strip_accents(string_input):
    """
    This function remove the accent of string so it can be more ease to make comparison 
    between between different strings, useful information

    ARGS: 
        string(str): The string that you wanna transform, it can be a value in a row or head column.
    RETURNS:
        string_cleaned(str): The sheet's name that will be used to create the DataFrame
    """
    string_input = str(string_input)
    string_cleaned = ''.join(c for c in unicodedata.normalize('NFD', string_input)if unicodedata.category(c) != 'Mn')
    return string_cleaned

def transform_column_name(column_name):
    """
    This function removes the accent on the string so it can be easier to make comparisons
     between different values of the same type,  and find useful information.

    ARGS: 
        column_name(str): the column_name
    RETURNS:
        name_cleaned(str): The column_name after transformed.
    """
    name_cleaned = strip_accents(str(column_name).strip('[]()').lower().replace(' ','_'))
    return name_cleaned

def rename_cl_df(df):
    """
    This function gets the DataFrame and renames its columns using the transform_column_name()

    ARGS:
        df(pandas.core.frame.DataFrame): The DataFrame that you will rename the columns
    RETURN:
        df(pandas.core.frame.DataFrame): The same DataFrame that you entered in the function but transformed.
    """

    #This list comprehension gets the name of the DataFrame and make a list
    old_cln = [cln for cln in df.columns.values]

    #This list comprehension gets the name of the DataFrame and make a list with theses names transformed by the transform_column_name()
    new_cln = [transform_column_name(cln) for cln in df.columns.values]

    #This dictionary(dct) is made with the lists:old_cln and new_cln. So that the columns in the DataFrame can be renamed comparing key and value inside ofthe dictionary.   
    dct = dict(zip(old_cln, new_cln))

    #this function is a method in Pandas to rename columns, in this case we are using the dictionary above to say what are values to replace.  
    df.rename(columns=dct,inplace=True)

    #This method is appending the new column names  to a list so that it can be insert into the data dictionary(df_sheet)
    lst_df_clns.append(new_cln)

    return df

def regexing(value, list_input):
    """
        This function gets the string and replace its value to other value referenced in the lst_re(list) 
    ARGS:
        value(str): value that will be replaced 
        list_input(list): list with the old values and new values in a tuple format.
    RETURN:
    """
    #Looping through the list to replace the values. Inside of each tuple there is a value on the first index to be replaced by a value of the second index.  
    for string in list_input:
        value = re.sub(string[0],string[1],value)
    return value


def filter_key(x):
    return (x==lst_pr[0])|(x==lst_pr[1])|(x==lst_pr[2])|(x==lst_pr[3])|(x==lst_pr[4])

def writing_in_df_prop():
    prop_name = df_nk['proponente'][i]
    input_regex = input('REGEX: ')
    name_regex = r''+input_regex
    return prop_name, name_regex

#lamb_str(anonymous function): This function make the string value upper case and and apply strip_accents() to the value.
lamb_str = lambda x:strip_accents(x).upper()

"""lamb_regex(anonymous function): This function apply the the regexing() to the string value. The regexing function is reposible 
for cleaning the data by replacing specifc values using the lst_re"""
lamb_regex = lambda x:regexing(x, lst_regex)

#lamb_strip(anonymous function): This function remove unecessay space by applying the strip method on the string.
lamb_strip = lambda x: str(x).strip()
#entering  in the folder to get the data
%cd Data_Source

#listing all the files on the Data_Source folder
files = os.listdir()

#filtering the xlsx or xls format on the directory
lst_excel_files = [x for x in files if x.split('.')[-1]=='xlsx' or  x.split('.')[-1]=='xls' or x.split('.')[-1]=='xlsm']

#putting all the sheets names inside of a list using a list comprehension that loops through list of excel files(lst_excel files)
sheets_names = [get_sheets_names(excel) for excel in lst_excel_files]

"""
Zipping the lists together for presenting and executing more code, with a list source(lst_source). 
The list source is for unifying sources in a unique list
"""
lst_source = list(zip(lst_excel_files, sheets_names))

#building a data frame with information about the excel files
df_excel= pd.DataFrame(lst_source, columns=['excel_file','sheets'])

#living the diretory of the Data_Source to ensure that the code will be not brake if it executed in the incorrect order.
%cd ..

#looping through the list_source to make a summary of the data that will be ingested on the Pandas DataFrame
print('')
for source in lst_source: 
    excel = source[0]
    sheet = source[1]
    print(f'EXCEL: {excel} >>> SHEETS: {sheet}')
#%%
#entering in the Data_Source directory to get data to be ingested into the DataFrame
%cd Data_Source

"""
Creating a list manually with the information presented about the sheets on the Data_Source Directory.
The First index of these tuples referer to the name that we will give to the DataFrame the second one refers to the sheet that the DataFrame will use.

EXAMPLE:
df_nm =[
(dataframe1_name, sheet_name1),
....
(dataframe8_name, sheet_name8)
]

the df_nm will be used to create the data dictionary inside of a Pandas DataFrame
"""
df_nm =[
('df_cg', 'ControleGeral2022'),
('df_sn', 'SintéticoGeral2022'), 
('df_pr', 'Sheet1'),
('df_states', 'estados'),
('df_emp', 'proponentes'),
('df_emb', 'bancadas'),
] 

#df_sheets -> This DataFrame was created do organize da data dictionary, it also will useful to some operation through the code
df_sheet = pd.DataFrame(df_nm, columns = ['df_name', 'sheet_name'])

#Creating a column to put the information that indicate from which excel file the DataFrames and sheets come from.
df_sheet['excel_file']= ''

"""Creating a loop to fill the rows in the df_sheets DataFrame with information about the excel source """

for i1, sheets in enumerate(df_excel['sheets']):
    for i2, sheet in enumerate(df_sheet['sheet_name']):
        if sheet in sheets:
            df_sheet['excel_file'][i2] = df_excel['excel_file'][i1]

#living the diretory of the Data_Source to ensure that the code will be not brake if it executed in the incorrect order.
%cd ..
#%%

#entering in the Data_Source directory to get and ingest the data into the DataFrame
%cd Data_Source

df_cg = pd.read_excel('Controle de Empenhos e NC 2022.xlsm', sheet_name='ControleGeral2022',
usecols='c:x', skiprows=14)

df_sn = pd.read_excel('Controle de Empenhos e NC 2022.xlsm',sheet_name='SintéticoNC2022',
usecols='f:n', skiprows=3)

df_emp = pd.read_excel('Emendas2021_resumo.xlsx', sheet_name="proponentes",
usecols='a:q', skiprows=3)

df_emb = pd.read_excel('Emendas2021_resumo.xlsx', sheet_name="bancadas",
usecols='a:m', skiprows=3)

df_pr = pd.read_excel('Proponentes.xlsx',
usecols='d:l')

df_states = pd.read_excel('estados.xlsx')

#living the diretory of the Data_Source to ensure that the code will be not brake if it executed in the incorrect order.
%cd ..

#%%
#creating a list with all DataFrame names from the data dictionary
dfs = [ x for x in df_sheet['df_name']]

#creating a command to transform the list with the name of the DataFrame to a list with real Dataframes inside of it
cmd = str(dfs).replace("'","")
#executing the cmd(str) into a real command using the exec() method
exec('dfs = {}'.format(cmd))

#lst_df_clns(list): Creating an empty list that will be filled using the the rename_cl_df(). This list will be be part of the data dictionary.  
lst_df_clns = []

#Looping through all the DataFrames to rename the columns using the rename_cl_df()
for df in dfs:
    rename_cl_df(df)

#df_sheet['columns']: Creating a column in the df_sheet(Dataframe) with information about all the columns of each sheet
df_sheet['columns'] = lst_df_clns 
df_sheet

#%%

#creating a list with all DataFrame names from the data dictionary
dfs = [ x for x in df_sheet['df_name']]

#creating a command to transform the list with the name of the DataFrame to a list with real Dataframes inside of it
cmd = str(dfs).replace("'","")
#executing the cmd(str) into a real command using the exec() method
exec('dfs = {}'.format(cmd))

#lst_df_clns(list): Creating an empty list that will be filled using the the rename_cl_df(). This list will be be part of the data dictionary.  
lst_df_clns = []

#Looping through all the DataFrames to rename the columns using the rename_cl_df()
for df in dfs:
    rename_cl_df(df)

#df_sheet['columns']: Creating a column in the df_sheet(Dataframe) with information about all the columns of each sheet
df_sheet['columns'] = lst_df_clns 
df_sheet

#%%
#creating a list of DataFrame with Proponentes
dfs = (df_cg, df_sn, df_emp)

#criando as colunas das primary_keys nos 3 dataframes
for df in dfs:
    df['prop_pk1'] = ''
    df['prop_pk2'] = ''

pk2 = []
for index, prop in enumerate(df_pr['prop_pk1']):
    if df_pr['orgao'][index] == "senado":
        pk2.append('SEN. ' + prop)
    elif  df_pr['orgao'][index] == "camara":
        pk2.append('DEP. ' + prop)
    else: 
        pk2.append(prop)#fazendo o loop sobre a lista acima para aplicar as funções que normalizam a coluna com as chaves dos proponentes

    df['prop_pk1'] = ''
    df['prop_pk2'] = ''
    #%%
    
#filling NaN values with 0
df_cg.fillna(0,inplace=True)
df_sn.fillna(0,inplace=True)
df_emp.valor.fillna(0,inplace=True)

lst_df = [df_cg, df_sn, df_emp]
#fazendo o loop sobre a lista acima para aplicar as funções que normalizam a coluna com as chaves dos proponentes
for df in lst_df:
    df['proponente'] = df['proponente'].apply(lamb_str)
    df['proponente'] = df['proponente'].apply(lamb_regex)
    df['proponente'] = df['proponente'].apply(lamb_strip)

lst_pr = (df_pr['prop_pk1'], df_pr['prop_1'],df_pr['prop_2'], df_pr['prop_3'],df_pr['prop_4'])

for df in lst_df:
    lst_prop_pk1 = []
    lst_prop_pk2 = []
    for index,value in enumerate(df.proponente):
        filt_finding_key =  filter_key(df.proponente.iloc[index])
        result1 = str(df_pr.loc[filt_finding_key].prop_pk1.values).strip("[']")
        result2 = str(df_pr.loc[filt_finding_key].prop_pk2.values).strip("[']")
        lst_prop_pk1.append(result1)
        lst_prop_pk2.append(result2)
    df['prop_pk1'] = lst_prop_pk1
    df['prop_pk2'] = lst_prop_pk2
    
#%%

#list of dfs that has proponentes names to found
dfs  = [[df_cg,'df_cg'], [df_sn,'df_sn'],[df_emp,'df_emp']]; 

lst_prop_no_key= []; lst = []

for df in dfs:
    for index, value in enumerate(df[0].loc[df[0].prop_pk1==''].proponente.values):
        if value not in lst:
            prop_name =  df[0].loc[df[0].prop_pk1==''].proponente.values[index]
            prop_source = df[1]
            lst_prop_no_key.append((prop_name, prop_source))
            lst.append(value)
        else:pass

print('DF COM OS PROPONENTES QUE NÃO APRESENTARAM CORRESPONDÊNCIA COM A COLUNA DO NOME CIVIL:')
proponentes_without_key = pd.DataFrame()
proponentes_without_key['proponente'] = [proponente for proponente, source in lst_prop_no_key]
proponentes_without_key['source'] = [source for proponente, source in lst_prop_no_key]
proponentes_without_key
#%%
%rm -r PowerBI_Dataset
%mkdir PowerBI_Dataset
%mkdir PowerBI_Dataset/csv/
%mkdir PowerBI_Dataset/xlsx/

%rm -r Data_Dictionary
%mkdir Data_Dictionary
%mkdir Data_Dictionary/csv/
%mkdir Data_Dictionary/xlsx/
%mkdir Data_Dictionary/csv/Columns/
%mkdir Data_Dictionary/xlsx/Columns/

path = 'PowerBI_Dataset'
for i, df  in enumerate(df_sheet['df_name']):
       exec(f'df = {df}')
       exec(f"{df_sheet['df_name'][i]}.to_csv('{path}/csv/{df_sheet['sheet_name'][i]}.csv')")
       exec(f"{df_sheet['df_name'][i]}.to_excel('{path}/xlsx/{df_sheet['sheet_name'][i]}.xlsx')")

path = 'Data_Dictionary'
for df in ('df_sheet', 'df_excel', 'df_folder'):
    exec(f"{df}.to_csv('{path}/csv/{df}.csv')")
    exec(f"{df}.to_excel('{path}/xlsx/{df}.xlsx')")

path2 = 'Columns'
for i, df  in enumerate(df_sheet['df_name']):
       exec(f'df = {df}')
       lst_cl = []
       for cl in df.columns: lst_cl.append(cl)
       dct = {'columns':lst_cl}
       exec(f"{df_sheet['df_name'][i]}_columns = pd.DataFrame(dct)")
       exec(f"{df_sheet['df_name'][i]}_columns['descricao'] = '' ")
       exec(f"{df_sheet['df_name'][i]}_columns.to_csv('{path}/csv/{path2}/{df_sheet['sheet_name'][i]}_columns.csv')")
       exec(f"{df_sheet['df_name'][i]}_columns.to_excel('{path}/xlsx/{path2}/{df_sheet['sheet_name'][i]}_columns.xlsx')")

%rm -r trash
%mkdir trash
proponentes_without_key.to_excel('trash/proponetes_without_key.xlsx')
