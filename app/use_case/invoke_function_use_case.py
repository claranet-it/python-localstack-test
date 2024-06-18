def invoke_functions_use_case(client):    
    return client.invoke(
        FunctionName='lambda_main-dev',        
        Payload='{}',
    )    
    