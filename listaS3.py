#!/usr/bin/python3

import argparse
import boto3

#Recoleccion de Claves de acceso a AWS
parser = argparse.ArgumentParser()
parser.add_argument("accesskey", type=str, help="ACCESS KEY ID")
parser.add_argument("secretkey", type=str, help="SECRET KEY")
args = parser.parse_args()

#Autenticación con AWS
client = boto3.resource('s3', aws_access_key_id=args.accesskey, aws_secret_access_key=args.secretkey)

#Impresión de datos requeridos
for bucket in client.buckets.all():
  print('Nombre del Bucket: ', bucket.name, 'Fecha de Creación: ', bucket.creation_date, 'Cantidad de Ficheros: ', sum(1 for _ in bucket.objects.all()),'Tamaño de Bucket: ', sum([object.size for object in client.Bucket(bucket.name).objects.all()]))