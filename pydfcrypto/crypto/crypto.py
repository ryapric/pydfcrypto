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

def encrypt_cols(df_0, cipher, as_bytes = False):
    df = df_0.copy()
    cols_enc = [cipher.encrypt(x.encode('utf-8')) for x in list(df.columns.values)]
    if not as_bytes:
        cols_enc = [x.decode('utf-8') for x in cols_enc]
    df.columns = cols_enc
    return df

def decrypt_cols(df_0, cipher):
    df = df_0.copy()
    cols_dec = [cipher.decrypt(x).decode('utf-8') for x in list(df.columns.values)]
    df.columns = cols_dec
    return df

def encrypt_body(df_0, cipher, as_bytes = False):
    df = df_0.copy()
    df = df.applymap(str)
    df = df.applymap(lambda x: cipher.encrypt(x.encode('utf-8')))
    if not as_bytes:
        df = df.applymap(lambda x: x.decode('utf-8'))
    return df

def decrypt_body(df_0, cipher):
    df = df_0.copy()
    df = df.applymap(lambda x: cipher.decrypt(x).decode('utf-8'))
    df = df.apply(lambda x: pd.to_numeric(x, errors = 'ignore'))
    return df

def dfencrypt(df_0, cipher, as_bytes = False):
    df = df_0.copy()
    df = encrypt_body(df, cipher, as_bytes)
    df = encrypt_cols(df, cipher, as_bytes)
    return df

def dfdecrypt(df_0, cipher):
    df = df_0.copy()
    if not all([type(x) is bytes for x in df.columns.values]):
        cols_bytes = [x.encode('utf-8') for x in list(df.columns.values)]
        df.columns = cols_bytes
    for i in df.columns.values:
        if not all([type(x) is bytes for x in df[i]]):
            df[i] = df[i].apply(lambda x: x.encode('utf-8'))
    df = decrypt_cols(df, cipher)
    df = decrypt_body(df, cipher)
    return df
