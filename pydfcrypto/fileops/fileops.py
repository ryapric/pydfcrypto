import pydfcrypto.crypto.crypto as crypto
import pandas as pd
import os
import sys

delim_dict = {
    '.csv': ',',
    '.csv2': ';',
    '.tsv': '\t',
    '.txt': '\n',
    '.xlsx': 'excel'
}

def get_delim(filename):
    ext = os.path.splitext(filename)[1]
    return delim_dict[ext]

def guess_read(filename, **kwargs):
    delim = get_delim(filename)
    if delim == 'excel':
        df_0 = pd.read_excel(filename, **kwargs)
    else:
        df_0 = pd.read_table(filename, sep = delim, **kwargs)
    return df_0

def guess_write(df_out, filename, **kwargs):
    delim = get_delim(filename)
    if delim == 'excel':
        df_out.to_excel(filename, **kwargs)
    else:
        df_out.to_csv(filename, sep = delim, **kwargs)

def encrypt_file(filename, cipher, **kwargs):
    df = guess_read(filename, **kwargs)
    df_enc = crypto.dfencrypt(df, cipher)
    guess_write(df_enc, filename)

def decrypt_file(filename, cipher, **kwargs):
    df = guess_read(filename, **kwargs)
    df_enc = crypto.dfdecrypt(df, cipher)
    guess_write(df_enc, filename)
