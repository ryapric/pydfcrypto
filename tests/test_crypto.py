import pytest
import pydfcrypto.crypto.crypto as crypto
import tests.dummy_data as dd

def test_generate_key(key):
    assert type(key) is bytes

def test_generate_bad_key():
    with pytest.raises(Exception):
        key = crypto.generate_key('asymmetric')

def test_generate_cipher(cipher):
    assert cipher is not None

def test_dfencrypt(df_enc):
    assert all([type(x) is str for x in df_enc.columns.values])
    for i in df_enc.columns.values:
        assert all([type(x) is str for x in df_enc[i]])

def test_dfencrypt_bytes(df_enc_bytes):
    assert all([type(x) is bytes for x in df_enc_bytes.columns.values])
    for i in df_enc_bytes.columns.values:
        assert all([type(x) is bytes for x in df_enc_bytes[i]])

def test_dfdecrypt(df_0, df_dec):
    for i in df_dec.columns.values:
        assert all([type(x) is not bytes for x in df_dec[i]])
        assert all(df_0[i] == df_dec[i])
    assert sum(df_dec['ints']) == sum(df_0['ints'])
    assert sum(df_dec['floats']) == sum(df_0['floats'])
    assert sum(df_dec['floats']) != (sum(df_0['floats'] + 1))
