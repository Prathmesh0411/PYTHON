def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "internal server"
        case _:
            return "Unknown status"
        
print(https_status(509))