import json


def read_creds_file(file_path='creds.json'):
    ''' Generic method to read a creds file 
        found in the root directory of the project
    '''
    data = None
    if file_path:
        try:
            with open(file_path) as json_file:
                data = json.load(json_file)
                return data
        except Exception as e:
            print(e)
    return {}
