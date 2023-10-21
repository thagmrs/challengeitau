import sys
import os
sys.path.insert(0, '../')
import json


class ValidateJSON:
    '''Classe para validação de Json

       validate_keys: valida se o json possui as colunas esperadas e a quantidade correta

       validate_types: valida se os tipos das colunas estão de acordo com o esperado

       validate_events: utiliza o metodo validate_keys para verificar se as chaves estão conforme esperado. Caso não estejam, já finaliza a validação.
                        se as validações das chaves tiverem ok, valida os tipos de cada uma de acordo com o padrão.
    
    '''
    
    def __init__(self, json_data):
        self.json_data = json_data
        self.schema = json.load(open(os.path.dirname(os.getcwd()) +'/exercicio1/schema.json'))

    def validate_keys(self):
        keys_json = sorted(set(self.json_data.keys()))
        try:
            keys_schema = sorted(self.schema['required'])
        except:
            keys_schema = set(self.schema['properties'][key]['properties'].keys())
        if keys_json == keys_schema:
            print('O evento possui as colunas e quantidades esperadas')
            return True
        else:
            print(f'''O evento possui colunas que não são esperadas 
                  colunas do schema: {keys_schema}
                  colunas da entrada: {keys_json}''')
            return False

    def validate_types(self, json_data=None, schema=None):
        if json_data is None:
            json_data = self.json_data
        if schema is None:
            schema = self.schema

        for key in set(schema['properties'].keys()):
            if key in json_data:
                type_event = type(json_data[key]).__name__
                if type_event == 'dict' or type_event == 'object':
                    if 'properties' in schema['properties'][key]:
                            if not self.validate_types(json_data[key], schema['properties'][key]):
                                print('Existem divergencias com os campos dentro da chave: ', key)
                                return False
                elif type_event[:3] != schema['properties'][key]['type'][:3]:
                        print(f'O tipo da chave "{key}" esta divergente do padrao')
                        return False
            else:
                print(f'a chave "{key}" não esta presente no evento enviado')
                return False
        return True

    def validate_events(self):
        if (self.validate_keys()):
            final_validation = self.validate_types()
            print('a validacao dos tipos foi concluida com sucesso!')
        else:
            final_validation = False
        return  final_validation

