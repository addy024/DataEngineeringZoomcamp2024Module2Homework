import pyarrow as pa 
import pyarrow.parquet as pq 
import os 


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/arcane-timer-411710-5ba45c45dfce.json"
bucket_name = 'mage-zoomcamp-aditya-phulallwar'
project_id = 'arcane-timer-411710'
table_name = 'nyc_green_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table, 
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )



