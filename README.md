# Migración y Limpieza Serverless con S3 y Lambda

Proyecto de la materia RPG - FP-UNA 2026
Alumno: Verónica Centurión

## Objetivo
Crear un pipeline automático que al subir un archivo TXT sucio a S3, lo limpie (minúsculas y sin espacios dobles) y lo guarde en otra carpeta.

## Arquitectura
S3 (pf-migrados/) -> Evento S3 -> Lambda (limpiadorTXT) -> S3 (limpio/)

## Tecnologías
- AWS S3
- AWS Lambda (Python 3.12 + boto3)
- AWS IAM (permisos S3WriteAccess)
- AWS CloudWatch

## Funcionamiento
1. Se sube `Archivo1.txt` con MAYÚSCULAS y espacios dobles a `pf-migrados/`
2. S3 dispara la Lambda automáticamente
3. La Lambda lee, convierte a minúsculas y quita espacios con `' '.join(texto.split())`
4. Guarda el resultado en `limpio/`

## Problema resuelto hoy
Error `AccessDenied` al escribir en S3. Se solucionó creando política IAM con `s3:PutObject` en `arn:aws:s3:::rpg-migracion-vcenturion-2026/limpio/*`.

## Costo
< 0.01 USD - 100% dentro del Free Tier. Crédito restante: 112.34 USD.