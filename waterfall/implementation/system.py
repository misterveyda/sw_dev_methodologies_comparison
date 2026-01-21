def login(username, password):
    return username != "" and password != ""

def register(username, password):
    return len(password) >= 6
