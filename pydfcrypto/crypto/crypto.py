from cryptography.fernet import Fernet
import pandas as pd

def generate_key(keytype = 'symmetric'):
    if keytype == 'symmetric':
        key = Fernet.generate_key()
    else:
        raise Exception(f'Key type {keytype} not yet implemented')
    return key

def make_cipher(key):
    cipher = Fernet(key)
    return cipher

def dfencrypt(df_0, cipher):
    df_enc = df_0.applymap(str)
    df_enc = df_enc.applymap(lambda x: cipher.encrypt(x.encode('utf-8')))
    cols_enc = [cipher.encrypt(x.encode('utf-8')) for x in list(df_enc.columns.values)]
    df_enc.columns = cols_enc
    return df_enc

def dfdecrypt(df_enc, cipher):
    cols_dec = [cipher.decrypt(x).decode('utf-8') for x in list(df_enc.columns.values)]
    df_enc.columns = cols_dec
    df_dec = df_enc.applymap(lambda x: cipher.decrypt(x).decode('utf-8'))
    df_dec = df_dec.apply(lambda x: pd.to_numeric(x, errors = 'ignore'))
    return df_dec
