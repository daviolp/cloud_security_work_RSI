import boto3

def criando_tabela():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='grupo03',
        KeySchema=[
            {
                'AttributeName': 'nome',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'linkedin',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'nome',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'linkedin',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print(table.item_count)

def escrevendo(nome, linkedin):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grupo03')

    table.put_item(
        Item={
            'nome': nome,
            'linkedin': linkedin
        }
    )


def lendo(nome):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grupo03')

    response = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('nome').eq(nome))
    item = response['Items']
    return item

def deletando_tabela():

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grupo03')
    table.delete()
