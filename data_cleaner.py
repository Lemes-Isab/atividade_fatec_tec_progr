
def remove_outliers_temperatura(df):
    return df[
        (df['temperatura'] >= -50) &
        (df['temperatura'] <= 60)
    ]

