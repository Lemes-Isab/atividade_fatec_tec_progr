import pandas as pd
import unittest

from data_cleaner import remove_outliers_temperatura(df)

def test_remove_outliers_temperatura():
    df = pd.DataFrame({
        'temperatura': [25, 999, -500, 60, 100]
    })

    resultado = remove_outliers_temperatura(df)

    self.assertEqual(len(resultado), 5)  # Assuming no outliers to remove
