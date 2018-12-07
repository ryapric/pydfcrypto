def encrypt_cols(df_0, cipher, as_bytes = False):
    df = df_0.copy()
    cols_enc = [cipher.encrypt(x.encode('utf-8')) for x in list(df.columns.values)]
    if not as_bytes:
        cols_enc = [x.decode('utf-8') for x in cols_enc]
    df.columns = cols_enc
    return df

def encrypt_body(df_0, cipher, as_bytes = False):
    df = df_0.copy()
    df = df.applymap(str)
    df = df.applymap(lambda x: cipher.encrypt(x.encode('utf-8')))
    if not as_bytes:
        df = df.applymap(lambda x: x.decode('utf-8'))
    return df

def dfencrypt(df_0, cipher, as_bytes = False):
    df = df_0.copy()
    df = encrypt_body(df, cipher, as_bytes)
    df = encrypt_cols(df, cipher, as_bytes)
    return df
