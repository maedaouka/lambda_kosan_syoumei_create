import json
from pyqldb.driver.qldb_driver import QldbDriver
import datetime

qldb_driver = QldbDriver(ledger_name='kosansyoumei-registration')


def lambda_handler(event, context):

    from_name = event['queryStringParameters']['from_name']
    to_name = event['queryStringParameters']['to_name']
    memo = event['queryStringParameters']['memo']
    device = event['queryStringParameters']['device']


    person_list = []

    def insert_documents(transaction_executor, arg_1):

        transaction_executor.execute_statement("INSERT INTO Certificate ?", arg_1)


    doc_1 = {'FromName' : from_name,
        'ToName' : to_name,
        'DOB': str(datetime.date.today()),
        'MEMO' : memo,
        'DeviceId' : device
    }

    qldb_driver.execute_lambda(lambda x: insert_documents(x, doc_1))

    return {
        'statusCode': 200,
        'body': json.dumps("success")
    }
