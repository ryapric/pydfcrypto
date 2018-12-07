import pydfcrypto.fileops.fileops as dfo
import pydfcrypto.crypto.crypto as crypto
import pandas as pd
import os

def test_encrypt_file_csv(df_0, df_enc, cipher):
    filename = 'test.csv'
    df_0.to_csv(filename, sep = ',')
    assert os.path.isfile(filename)
    dfo.encrypt_file(filename, cipher)
    file_enc = pd.read_csv(filename)
    assert file_enc == df_enc

def test_decrypt_file_csv(df_dec, cipher):
    filename = 'test.csv'
    file_enc = pd.read_csv(filename)
    file_dec = crypto.dfdecrypt(file_enc, cipher)
    assert file_dec == df_dec

def test_encrypt_file_excel(df_0, df_enc, cipher):
    filename = 'test.xlsx'
    df_0.to_excel(filename)
    assert os.path.isfile(filename)
    dfo.encrypt_file(filename, cipher)
    file_enc = pd.read_excel(filename)
    assert file_enc.columns.values == df_enc.columns.values

def test_teardown(teardown):
    pass
