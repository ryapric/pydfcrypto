import pytest
import pydfcrypto.crypto.crypto as crypto
import tests.dummy_data as dd
import os
import glob

@pytest.fixture
def df_0():
    df_0 = dd.make_dummy_data()
    return df_0

@pytest.fixture
def key():
    key = crypto.generate_key()
    return key
    
@pytest.fixture
def cipher(key):
    cipher = crypto.make_cipher(key)
    return cipher

@pytest.fixture
def df_enc(df_0, cipher):
    df_enc = crypto.dfencrypt(df_0, cipher)
    return df_enc

@pytest.fixture
def df_dec(df_enc, cipher):
    df_dec = crypto.dfdecrypt(df_enc, cipher)
    return df_dec

@pytest.fixture
def teardown():
    os.remove(glob.glob('test.*'))
