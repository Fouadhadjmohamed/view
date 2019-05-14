from google.cloud import bigquery
import json
import os

def normalize_query(query):
    query = query.replace('dev', '[ENV]')
    query = query.replace('prod', '[ENV]')
    query =  ' '.join(query.split())
    return query

def is_query_valid(query):
# Test query into bq
    if ('\n' in query):
        query =  ' '.join(query.split())
    client = bigquery.Client()
    query_job = client.query(query)
    rows = query_job.result()
    res = []
    for row in rows:
            res.append(row)
            break
    return False if not res else True

def get_dict_from_two_lists(keys, values):
        if len(values) != len(keys): 
                return "Error"
        return {keys[i] : values[i] for i in range(len(keys))}
# Quotes -> Double-Quotes partout

def add_view_to_json(json_file, dict_to_add):
        with open(json_file,"ab+") as f:      
                _json = json.load(f)  
                for dict in _json.values():
                        for line in f:
                                (key, val) = line.split()
                                dict[int(key)] = val
                                if dict['name'] == dict_to_add['name']:
                                        f.close()
                                        return 'View already exists in this file'
                                else:  
                                        # _json["tables"].write(json.dumps(dict_to_add, indent=4))                                                
                                        _json.update(dict)
                                        f.close() 
                                        return 'View added'

fp = "00052_lernev2_france_private.json"
query =  ("""
SELECT
  *
FROM
  `fr-imt-isteau-datadesk-dev.00166_ml_data_predictions_france_private.T_INTER_FR_MAPS`
LIMIT
  1000
""")

n_query = normalize_query(query=query)

table_keys = ["project_name", "name", "table_type", "active", "query", "legacySQL", "dataset_name", "description"]
if(is_query_valid(query) == True):
    print("Valid query")
    table_values = ["fr-imt-isteau-datadesk-dev", "V_ML_INTERVENTIONS_TO_PREDICT", "view", "true", normalize_query(query=query), "false", "00166_ml_data_predictions_france_private", "Vue des interventions à predire // DG"]
    view_dict = get_dict_from_two_lists(table_keys, table_values) 
    double_quote = json.dumps(view_dict, indent=4)
    print ("View_dict created")
    print (add_view_to_json(fp, view_dict))
    
else:
    print("Invalid query")

