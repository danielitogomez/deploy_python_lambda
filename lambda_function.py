def lambda_handler(event, context):
    print("Hello World")
    return {
        'statusCode': 200,
        'body': 'Hello World'
    }

if __name__ == "__main__":
    event = {}
    context = {}
    response = lambda_handler(event, context)
    print("Response:")
    print(response)
