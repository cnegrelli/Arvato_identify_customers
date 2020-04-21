import numpy as np
import pandas as pd
import datetime
from sklearn.preprocessing import Imputer

def clean_df4(df, del_rows = True):
    
    '''
    INPUT: (pandas dataframe) df
    
    OUTPUT: (pandas dataframe) cleaned df
    
    This funtion returns the df cleaned:
    1. Coverts unknown values to NaN
    2. Drops columuns with more than 50% missing values
    3. Remove rows with more than 10% missing values
    4. Clean and convert object columns to numeric. In same cases by hot-encoding.
    5. Drop id column
    6. Fill NaNs with mode.
    7. Drop high correlated columns 
    
    '''
    
    for column in list(df.columns.values):
        df[column].replace(-1, np.NaN, inplace=True)
    null0 = ['ALTERSKATEGORIE_GROB', 'ALTER_HH', 'ANREDE_KZ', 'CJT_GESAMTTYP', 'GEBAEUDETYP', 'HH_EINKOMMEN_SCORE', 'KBA05_BAUMAX', 'KBA05_GBZ', 'KKK', 'NATIONALITAET_KZ', 'PRAEGENDE_JUGENDJAHRE', 'REGIOTYP', 'RETOURTYP_BK_S', 'TITEL_KZ', 'WOHNDAUER_2008', 'W_KEIT_KIND_HH']
    for column in null0:
        try:
            df[column].replace(0, np.NaN, inplace=True)
        except:
            continue
    null9 = ['KBA05_ALTER1', 'KBA05_ALTER2', 'KBA05_ALTER3', 'KBA05_ALTER4', 'KBA05_ANHANG', 'KBA05_AUTOQUOT', 'KBA05_CCM1', 'KBA05_CCM2', 'KBA05_CCM3', 'KBA05_CCM4', 'KBA05_DIESEL', 'KBA05_FRAU', 'KBA05_HERST1', 'KBA05_HERST2', 'KBA05_HERST3', 'KBA05_HERST4', 'KBA05_HERST5', 'KBA05_KRSAQUOT', 'KBA05_KRSHERST1', 'KBA05_KRSHERST2', 'KBA05_KRSHERST3', 'KBA05_KRSKLEIN', 'KBA05_KRSOBER', 'KBA05_KRSVAN', 'KBA05_KRSZUL', 'KBA05_KW1', 'KBA05_KW2', 'KBA05_KW3', 'KBA05_MAXAH', 'KBA05_MAXBJ', 'KBA05_MAXHERST', 'KBA05_MAXSEG', 'KBA05_MAXVORB', 'KBA05_MOD1', 'KBA05_MOD2', 'KBA05_MOD3', 'KBA05_MOD4', 'KBA05_MOD8', 'KBA05_MOTOR', 'KBA05_MOTRAD', 'KBA05_SEG1', 'KBA05_SEG2', 'KBA05_SEG3', 'KBA05_SEG4', 'KBA05_SEG5', 'KBA05_SEG6', 'KBA05_SEG7', 'KBA05_SEG8', 'KBA05_SEG9', 'KBA05_SEG10', 'KBA05_VORB0', 'KBA05_VORB1', 'KBA05_VORB2', 'KBA05_ZUL1', 'KBA05_ZUL2', 'KBA05_ZUL3', 'KBA05_ZUL4', 'RELAT_AB', 'SEMIO_SOZ', 'SEMIO_FAM', 'SEMIO_REL', 'SEMIO_MAT', 'SEMIO_VERT', 'SEMIO_LUST', 'SEMIO_ERL', 'SEMIO_KULT', 'SEMIO_RAT', 'SEMIO_KRIT', 'SEMIO_DOM', 'SEMIO_KAEM', 'SEMIO_PFLICHT', 'SEMIO_TRADV', 'ZABEOTYP', 'KBA05_HERSTTEMP']
    for column in null9:
        try:
            df[column].replace(9, np.NaN, inplace=True)
        except:
            continue

    dropcol = ['ALTER_KIND4','ALTER_KIND3', 'ALTER_KIND2', 'ALTER_KIND1', 'TITEL_KZ', 'AGER_TYP', 'EXTSEL992', 'KK_KUNDENTYP', 'KBA05_BAUMAX']
    for col in dropcol:
        try:
            df.drop(col, axis=1, inplace=True)
        except:
            continue
            
    if del_rows:
        row_nulls= (df.isnull().sum(axis=1)/df.shape[1])
        df.drop(list(row_nulls[row_nulls > 0.1].index.values),inplace=True)
    
    df['CAMEO_DEUG_2015'].replace('X',np.NaN, inplace=True)
    df['CAMEO_INTL_2015'].replace('XX',np.NaN, inplace=True)
    df['CAMEO_DEUG_2015'] = df['CAMEO_DEUG_2015'].astype(float)
    df['CAMEO_INTL_2015'] = df['CAMEO_INTL_2015'].astype(float)
    
    df['OST_WEST_KZ'] = df.OST_WEST_KZ.map({'W':0,'O':1})

    columna =  'EINGEFUEGT_AM'
    if columna in (list(df.columns.values)):
        df['year'] = pd.DatetimeIndex(df['EINGEFUEGT_AM']).year
        df.drop('EINGEFUEGT_AM', axis=1, inplace=True)
    
    df['CAMEO_DEU_2015'].replace('XX',np.NaN, inplace=True)
    df = pd.get_dummies(df, columns=['D19_LETZTER_KAUF_BRANCHE', 'CAMEO_DEU_2015'])
    
    df = df.astype(float)
    
    df.drop('LNR',axis=1,inplace=True)
    
    imputer = Imputer(strategy='most_frequent')
    df_col = list(df.columns.values)
    df_imp = imputer.fit_transform(df)
    df = pd.DataFrame(df_imp, columns= df_col)
    
    drop = ['KBA13_HERST_SONST',  'PLZ8_GBZ',  'PLZ8_HHZ',  'CAMEO_INTL_2015',  'ANZ_STATISTISCHE_HAUSHALTE',  'LP_LEBENSPHASE_GROB',  'LP_STATUS_GROB',  'KBA13_KMH_250']
    df.drop(drop,axis=1,inplace=True)
    
    
    return df


