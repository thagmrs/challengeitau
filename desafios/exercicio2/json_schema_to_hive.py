import json
import os

_ATHENA_CLIENT = None

def create_hive_table_with_athena(query):
    '''
    Função necessária para criação da tabela HIVE na AWS
    :param query: Script SQL de Create Table (str)
    :return: None
    '''
    
    print(f"Query: {query}")
    _ATHENA_CLIENT.start_query_execution(
        QueryString=query,
        ResultConfiguration={
            'OutputLocation': f's3://iti-query-results/'
        }
    )

def handler():
    '''
    #  Função principal
    Aqui você deve começar a implementar o seu código
    Você pode criar funções/classes à vontade
    Utilize a função create_hive_table_with_athena para te auxiliar
        na criação da tabela HIVE, não é necessário alterá-la
    '''
    database = 'db_teste'
    table_name = 'table_teste'
    query = f"""
    CREATE EXTERNAL TABLE IF NOT EXISTS {database}.{table_name} (
        eid string,
        documentNumber string,
        name string,
        age integer,
        address struct<
            street:string
            number:integer
            mailAddress:boolean>
    )
    ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
    """

    create_hive_table_with_athena(query)

