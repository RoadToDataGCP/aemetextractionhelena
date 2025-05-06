import datetime as dt
from google.cloud import storage

def subirabucket(archivo, nombrecarpeta):
    today_date = dt.datetime.now().strftime("%Y-%m-%d")
    destination_blob_name = f"{nombrecarpeta}/{today_date}/{archivo.split('/')[-1]}"

    storage_client = storage.Client()
    bucket = storage_client.bucket('aemetextractionhelena')
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(archivo)

    print(f"Archivo subido a gs://{'aemetextractionhelena'}/{destination_blob_name}")