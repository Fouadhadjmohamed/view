from google.cloud import bigquery
from google.cloud.bigquery import Dataset
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials 

# credentials to list project
credentials = GoogleCredentials.get_application_default()
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

# list project
request = service.projects().list()
response = request.execute()

# Main loop for project
for project in response.get('projects', []):
    client = bigquery.Client(project['projectId']) # Start the client in the right project

    # list dataset
    datasets = list(client.list_datasets())
    if datasets: # If there is some BQ dataset
        print('Datasets in project {}:'.format(project['name']))
        # Second loop to list the tables in the dataset
        for dataset in datasets: 
            print(' - {}'.format(dataset.dataset_id))
            get_size = client.query("select table_id, size_bytes as size from "+dataset.dataset_id+".__TABLES__") # This query retrieve all the tables in the dataset and the size in bytes. It can be modified to get more fields.
            tables = get_size.result() # Get the result
            # Third loop to list the tables and print the result
            for table in tables:
                print('\t{} size: {}'.format(table.table_id,table.size))
                