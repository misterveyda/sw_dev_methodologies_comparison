def register(username, password):
    if len(password) < 6:
        return "Weak password"
    return "User registered"
