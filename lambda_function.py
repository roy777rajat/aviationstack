from package.some_module import hello

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': hello()
    }