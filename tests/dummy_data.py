import pandas as pd

def make_dummy_data():
    df = pd.DataFrame({
        'strings': ['a', 'b', 'c', 'd', 'e'],
        'ints': [1, 2, 3, 4, 5],
        'floats': [1.1, 2.2, 3.33, 4.444, 5.6789]
    })
    return df
