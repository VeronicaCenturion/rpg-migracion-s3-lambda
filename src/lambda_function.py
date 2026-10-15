import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Solo procesar archivos de pf-migrados/
    if not key.startswith('pf-migrados/'):
        return

    # Leer archivo sucio
    obj = s3.get_object(Bucket=bucket, Key=key)
    texto = obj['Body'].read().decode('utf-8')

    # Limpieza: minúsculas y un solo espacio
    texto = texto.lower()
    texto = ' '.join(texto.split())

    # Guardar en limpio/
    nombre = key.split('/')[-1]
    s3.put_object(
        Bucket=bucket,
        Key=f'limpio/{nombre}',
        Body=texto.encode('utf-8')
    )

    print(f"Archivo limpiado: limpio/{nombre}")
    return f'OK: limpio/{nombre}'