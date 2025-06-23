def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
             return "Unkonwn Status"
         
n =int(input("Enter a status code: "))
print(https_status(n))