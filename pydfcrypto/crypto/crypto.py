from cryptography.fernet import Fernet

def generate_key(keytype = 'symmetric'):
    if keytype == 'symmetric':
        key = Fernet.generate_key()
    else:
        raise Exception(f'Key type {keytype} not yet implemented')
    return key

def make_cipher(key):
    cipher = Fernet(key)
    return cipher
