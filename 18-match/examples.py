def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 500:
            return "Server error"
        case _: # the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.
            return "Something's wrong with the internet"
        

print(http_error(405))
        
