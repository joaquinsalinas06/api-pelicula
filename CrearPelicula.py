import boto3
import uuid
import os

def lambda_handler(event, context):
    try:
        # Entrada (json)
        print({"tipo": "INFO", "log_datos": event})
        tenant_id = event['body']['tenant_id']
        pelicula_datos = event['body']['pelicula_datos']
        nombre_tabla = os.environ["TABLE_NAME"]
        # Proceso
        uuidv4 = str(uuid.uuid4())
        pelicula = {
            'tenant_id': tenant_id,
            'uuid': uuidv4,
            'pelicula_datos': pelicula_datos
        }
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(nombre_tabla)
        response = table.put_item(Item=pelicula)
        # Salida (json)
        print({"tipo": "INFO", "log_datos": pelicula})
        return {
            'statusCode': 200,
            'pelicula': pelicula,
            'response': response
        }
    except Exception as e:
        print({"tipo": "ERROR", "log_datos": {"error": str(e)}})
        return {
            'statusCode': 500,
            'error': str(e)
        }
