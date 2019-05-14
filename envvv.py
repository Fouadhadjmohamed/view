from google.cloud import bigquery

client = bigquery.Client()
query = ("SELECT * FROM 'fr-imt-isteau-datadesk-dev.00049_contrat_france.V_ACTIVITE_V1' LIMIT 1000")
query_job = client.query(query)

'''
for row in query_job:  # API request - fetches results
    # Row values can be accessed by field name or index
    assert row[0] == row.Type == row["Type"]
    print(row)'''