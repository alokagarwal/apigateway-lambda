def lambda_handler(event, context):
    
    print (event)
    
    auth = "Deny"
    
    if event["authorizationToken"] == 'xyz123' :
        auth = 'Allow'
    else :
        auth = 'Deny'
    
    authResponse = { "principalId": "abcdef", "policyDocument": { "Version": "2012-10-17", "Statement": [ { "Action": "execute-api:Invoke", "Effect": auth, "Resource": "arn:aws:execute-api:us-east-1:846558749899:576fzn6z95/dev/GET/demo" } ] } }
    
    return authResponse