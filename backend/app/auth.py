import random

sessions = {}

def is_username_and_password_correct(username, password):
    return False

# create a session and return the token
def create_or_replace_session_for_user(username):

    token = random.randint(10**19, 10**20 - 1) # nombre aléatoire à 20 chiffres
    while token in sessions:
        token = random.randint(10**19, 10**20 - 1) # on s'assure que le token existe pas déjà
    sessions[token] = username
    return token

def delete_session(token):
    if token in sessions:
        del sessions[token]

def verify_session(token):
    if token in sessions:
        return sessions[token]
    return None