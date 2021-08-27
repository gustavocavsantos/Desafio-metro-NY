###### Função para resampling da base de dados, deixando em formato horário. 

import pandas as pd
import numpy as np


def time_resampling(path,timeframe):
    
    
    df= pd.read_csv(path)
    df=df[df['desc']=='REGULAR']
    df['time']= pd.to_datetime(df['time'])
    df=df.sort_values(by='time')
    df.index=df.time
    df['entries'] = df['entries'].abs()
    df['exits'] = df['exits'].abs()
    df_sum=df.resample(timeframe).sum()
    
    return df_sum 
    
    
    

