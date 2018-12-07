import pytest
import pydfcrypto.crypto.crypto as crypto
import pydfcrypto.crypto.encrypt as enc
import pydfcrypto.crypto.decrypt as dec
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
    df_enc = enc.dfencrypt(df_0, cipher)
    return df_enc

@pytest.fixture
def df_enc_bytes(df_0, cipher):
    df_enc_bytes = enc.dfencrypt(df_0, cipher, as_bytes = True)
    return df_enc_bytes

@pytest.fixture
def df_dec(df_enc, cipher):
    df_dec = dec.dfdecrypt(df_enc, cipher)
    return df_dec

@pytest.fixture
def teardown():
    for i in glob.glob('test.*'):
        os.remove(i)
