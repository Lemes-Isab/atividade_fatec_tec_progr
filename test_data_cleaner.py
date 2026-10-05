import pandas as pd
from data_cleaner import remove_outliers_temperatura


def test_remove_outliers_temperatura():
    df = pd.DataFrame({
        'temperatura': [25, 999, -500, 60, 100]
    })

    resultado = remove_outliers_temperatura(df)

    assert len(resultado) == 2
