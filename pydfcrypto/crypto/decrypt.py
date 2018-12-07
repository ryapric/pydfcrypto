import pandas as pd

def decrypt_cols(df_0, cipher):
    df = df_0.copy()
    cols_dec = [cipher.decrypt(x).decode('utf-8') for x in list(df.columns.values)]
    df.columns = cols_dec
    return df

def decrypt_body(df_0, cipher):
    df = df_0.copy()
    df = df.applymap(lambda x: cipher.decrypt(x).decode('utf-8'))
    df = df.apply(lambda x: pd.to_numeric(x, errors = 'ignore'))
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
