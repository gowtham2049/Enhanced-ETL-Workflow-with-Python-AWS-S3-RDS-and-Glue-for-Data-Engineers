import pandas as pd
import logging

def transform_df(df):
    df['height'] = pd.to_numeric(df['height'], errors='coerce')
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df['height']=df['height']*0.0254
    df['weight']=df['weight'] *0.453592
    df.columns = ['Name', 'Height_m', 'Weight_kg']
    transformed_df = df.round({'Height_m': 2, 'Weight_kg': 2})
    logging.info("transforming the raw data")

    return transformed_df.drop_duplicates()