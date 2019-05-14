'''
def normalize_query(str):

    str = str.replace('dev', '[ENV]')
    str = str.replace('prod', '[ENV]')
    str =  ' '.join(str.split())
    return str


test_str = 'prod dev end        frkfje, dev ck prod rfvnr'
str = normalize_query(test_str)
print str,

import json

def create_json_obj(liste):
    if len(liste) != 8:
        return 'erreur arg'
    else:
        json.dumps(liste)
        liste = "\n".join(liste)
        liste = json.loads(liste)
        return liste








test_str = 'prod dev end        frkfje, dev ck prod rfvnr'
str = normalize_query(test_str)
print str,



test =  ['fr-imt-isteau-datadesk-dev',
'V_ML_INTERVENTIONS_TO_PREDICT',
'view',
'true',
'SELECT DISTINCT int.ID_EMETTEUR as ID_EMETTEUR, int.CODE_TYPE',
'false',
'00166_ml_data_predictions_france_private',
'Vue des interventions à predire // DG']

json_test = create_json_obj(test)
print json_test

print (type(json_test))



def query_results(query):
        client = bigquery.Client()
        query_job = client.query(query)
        rows = query_job.result()

        for row in rows:
                print(row)


    def test_vue(file, attribute, vue):
        mon_fichier = open(file, 'r')
        contenu = mon_fichier.readline()
        print (contenu)

        if attribute[i] : vue[i] in file:
                print ('vue existante')
        else:   mon_fichier.seek(-1,2)
                mon_fichier.write(attribute +':' + vue .encode())

        return mon_fichier

        def test_vue(file, attribute, vue):
        with open(file, "r") as f:
                for line in f.readlines():
                        if attribute in line:
                                if vue in line:
                                        print('vue existante')
                                else: json.


def test_vue(file, attribute, vue):
        with open(file, "r") as f:        
                mon_fichier = json.load(f)
                for name_value in mon_fichier["tables"]:
                        print name_value [attribute]
'''