def list_functions_use_case(client) -> list:    
    functions_list = []
    result = client.list_functions()
    
    for function in result["Functions"]:
        functions_list.append({
            "FunctionName": function["FunctionName"],
            "FunctionArn": function["FunctionArn"],
        })

    return functions_list