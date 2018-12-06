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

def test_encrypt_file_excel(df_0):
    df_0.to_excel('test.xlsx')
    assert os.path.isfile('test.xlsx')

def test_teardown(teardown):
    assert 1 == 1
