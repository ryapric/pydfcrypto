import pydfcrypto.crypto.crypto as crypto
import pandas as pd
from functools import wraps
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

def guess_read(filename, *args, **kwargs):
    delim = get_delim(filename)
    if delim == 'excel':
        df_0 = pd.read_excel(filename, *args, **kwargs)
    else:
        df_0 = pd.read_table(filename, sep = delim, *args, **kwargs)
    return df_0

def guess_write(df_out, filename, *args, **kwargs):
    delim = get_delim(filename)
    if delim == 'excel':
        df_out.to_excel(filename, *args, **kwargs)
    else:
        df_out.to_csv(filename, sep = delim, *args, **kwargs)

def encrypt_file(filename, cipher, *args, **kwargs):
    df_0 = guess_read(filename, *args, **kwargs)
    df_enc = crypto.dfencrypt(df_0, cipher)
    guess_write(df_enc, filename)
