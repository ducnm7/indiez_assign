def clean_data(df):
    df = df.dropna()
    df = df[df['column'] > 0]
    return df