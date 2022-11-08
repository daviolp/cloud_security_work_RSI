from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import dynamodb
import buckets
import logging

app = FastAPI()


@app.get("/")
def read_root():
    return 'Grupo 03: Davi Oliveira, Lucélia Lima, Lorena Medeiros e Nathália Cavalcante.'

@app.get("/criardynamo")
def criar_dynamo():
    dynamodb.criando_tabela()

@app.get("/deletardynamo")
def deletar_dynamo():
    dynamodb.deletando_tabela()

@app.get("/writedynamo/")
async def write_dynamo(nome: Union[str, None] = 'Davi', linkedin: Union[str, None] = 'linkedin.com/in/davi-oliveira-lopes'):
    dynamodb.escrevendo(nome, linkedin)

@app.get("/readdynamo/")
async def ready_dynamo(nome: Union[str, None] = 'Davi'):
    return dynamodb.lendo(nome)


## FAST API PARA O AWS-S3

@app.get("/criarbucket/")
async def criar_bucket_s3():
    buckets.criando_bucket()

@app.put("/writebucket/")
async def write_bucket(file: UploadFile):
    buckets.inserindo_bucket(file)

@app.get("/listdatabucket/")
async def list_data_bucket():
    return buckets.listando_arquivos_bucket()

@app.get("/deletardatabucket/")
def deletar_data_bucket(key: Union[str, None] = 'Grupo03.txt'):
    buckets.deletando_arquivo_bucket(key)

@app.get("/deletarbucket/")
def deletar_bucket():
    buckets.deletar_bucket()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
