import os
import pandas as pd
import io
import numpy as np
import datetime as dt

# select weather features
# w_cols_select and w_cols must be consistent
w_cols_select = ["F", "D", "R1", "TT_STD", "RF_STD", "V_N", "PP_TER"]
w_cols = ['F', 'R1', 'TT_STD', 'RF_STD', 'V_N', 'PP_TER', 
          'wind_E', 'wind_N', 'wind_NE', 'wind_NW', 'wind_S', 'wind_SE', 'wind_SW', 'wind_W']

def get_description():
    description = pd.DataFrame( [ 
                ["Datum","pandas datetime","general"],
                ["PM10","PM10 measured (µg/m³)","air_quality"],
                ["Ozon","Ozon measured  (µg/m³)","air_quality"],
                ["NO2","NO2 measured(µg/m³)","air_quality"],
                ["Quality","Stundenwerte der Relativen Feuchte (in %)","air_quality"],
                ["Schulfrei","school free in SH (1/0)","Schulfrei"],
                ["Feiertag","feiertag (1/0)","Feiertage"],
                ["QN_3_W","Qualitätsniveau (Wind)","Wind"],
                ["F","wind velocity (in m/sec)","Wind"],
                ["D","wind direction (in deg)","Wind"],
                ["QN_8_W","Qualitätsniveau (Wind)","Windspitzen"],
                ["FX_911","max wind velocity (in m/sec)","Windspitzen"],
                ["QN_9_T","Qualitätsniveau  (Temperatur und relative Luftfeuchte)","Temperatur und relative Luftfeuchte"],
                ["TT_TU","airtemperature (in °C)","Temperatur und relative Luftfeuchte"],
                ["RF_TU","relative humidity (in %)","Temperatur und relative Luftfeuchte"],
                ["QN_8_N","Qualitätsniveau  (Niederschlag)","Niederschlag"],
                ["R1","rain amount per hour (in mm)","Niederschlag"],
                ["RS_IND","hourly indictaion of rain (1/0)","Niederschlag"],
                ["WRTR","type of rainfall (numeric code)","Niederschlag"],
                ["QN_8_F","Qualitätsniveau  (Feuchtigkeit)","Feuchtigkeit"],
                ["ABSF_STD","absolute humidity","Feuchtigkeit"],
                ["VP_STD","berechnete Stundenwerte des Dampfdruckes (in hpa)","Feuchtigkeit"],
                ["TF_STD","berechnete Stundenwerte der Feuchttemperatur (in °C)","Feuchtigkeit"],
                ["P_STD","Stundenwerte Luftdruck (in hpa)","Feuchtigkeit"],
                ["TT_STD","air temperature at 2m height (in °C)","Feuchtigkeit"],
                ["RF_STD","relative humidity (in %)","Feuchtigkeit"],
                ["TD_STD","Taupunkttemperatur in 2m Hoehe (in °C)","Feuchtigkeit"],
                ["QN_8_B","Qualitätsniveau  (Bewölkung)","Bewölkung"],
                ["V_N_I"," ","Bewölkung"],
                ["V_N","degree of coverage of all clouds (in eights)","Bewölkung"],
                ["QN_4_L","Qualitätsniveau  (Luft)","Luftdruck"],
                ["PP_TER","air pressure (in hpa)","Luftdruck"] ],
                columns = ("column", "description", "source") )
    return description

def custom_to_datetime(date):
    """------------------------------------------------------------------
    Konvertiere einen String mit Datum und Zeit (MEZ) in ein datetime type (UTC) ###
    Parameter: 
        date: String im Format "TT.MM.YY SS:MM" (MEZ)
    Rueckgabe: 
        ein datetime (UTC)
    ------------------------------------------------------------------"""

    # If the time is 24, set it to 0 and increment day by 1
    if date[12:14] == '24':
        date = date.replace('24:00', '00:00')
        return pd.to_datetime(date, format = "%d.%m.%Y %H:%M", exact=False) + pd.Timedelta(days=1) + pd.Timedelta(hours=-1)
    else:
        return pd.to_datetime(date, format = "%d.%m.%Y %H:%M", exact=False) + pd.Timedelta(hours=-1)

def make_DateTime_features(df):
    ## create additional columns with year, week, weekday, hour
    df["year"] = df["Datum"].apply(lambda x: x.year)
    #df["week"] = df["Datum"].apply(lambda x: x.isocalendar().week)
    df['month'] = df['Datum'].dt.month
    df["day_of_week"] = df["Datum"].apply(lambda x: x.isocalendar().weekday)
    df["hour"] = df['Datum'].dt.hour
    
    # one hot encoding of column Wochentag
    one_hot = pd.get_dummies(df['day_of_week'])
    one_hot.columns = (["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
    df = df.drop('day_of_week',axis = 1)
    df = df.join(one_hot)
    
    # one hot encoding of columns Monat
    one_hot = pd.get_dummies(df['month'], prefix = 'month')
    df = df.drop('month',axis = 1)
    df = df.join(one_hot)
    
    # one hot encoding of column Stunde
    one_hot = pd.get_dummies(df['hour'], prefix = 'hour')
    df = df.drop('hour',axis = 1)
    df = df.join(one_hot)
    
    return df

def make_PM10_df(luftmessstation, wetterstation, verzeichnis = os.path.join("..", "resources", "Data"), bundesland = 'SH'):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
    Rückgabe:
        ein data_frame mit allen Daten 
    ------------------------------------------------------------------"""
     
    Luftqualitaet = pd.read_csv(os.path.join(verzeichnis,luftmessstation),sep = ';')
    Schulfrei = pd.read_csv(os.path.join(verzeichnis,"Schulfrei_"+bundesland+".csv"),sep = ',')
    Feiertage = pd.read_csv(os.path.join(verzeichnis,"Feiertage_"+bundesland+".csv"),sep = ',')

    path = os.path.join(verzeichnis, wetterstation)

    Wind = pd.read_csv(os.path.join(path,"Wind.csv"),sep = ',')
    Temp = pd.read_csv(os.path.join(path,"Temperatur_und_relative_Feuchte.csv"),sep = ',')
    Windspitzen = pd.read_csv(os.path.join(path,"Windspitzen.csv"),sep = ',')
    Bewoelkung = pd.read_csv(os.path.join(path,"Bewoelkung.csv"),sep = ',')
    Luftdruck = pd.read_csv(os.path.join(path,"Luftdruck.csv"),sep = ',')
    Feuchtigkeit = pd.read_csv(os.path.join(path,"Feuchtigkeit.csv"),sep = ',')
    Niederschlag = pd.read_csv(os.path.join(path,"Niederschlag.csv"),sep = ',')

    Luftqualitaet.columns = ['Stationscode', 'Datum', 'PM10', 'Ozon', 'NO2', 'Quality']
    Wind.columns = ['Stations_ID', 'Datum', 'QN_3_W', 'F', 'D', 'eor']
    Windspitzen.columns = ['Stations_ID', 'Datum', 'QN_8_W', 'FX_911', 'eor']
    Luftdruck.columns = ['Stations_ID', 'Datum', 'QN_4_L','PP_TER', 'eor']
    Feuchtigkeit.columns = ['Stations_ID', 'Datum', 'QN_8_F', 'ABSF_STD', 'VP_STD', 'TF_STD', 
                            'P_STD', 'TT_STD', 'RF_STD', 'TD_STD', 'eor']
    Temp.columns = ['Stations_ID', 'Datum', 'QN_9_T', 'TT_TU', 'RF_TU' , 'eor']
    Niederschlag.columns = ['Stations_ID', 'Datum', 'QN_8_N', 'R1', 'RS_IND', 'WRTR', 'eor']
    Bewoelkung.columns = ['Stations_ID', 'Datum', 'QN_8_B', 'V_N_I', 'V_N', 'eor']

    Luftqualitaet.Datum = Luftqualitaet.Datum.apply(custom_to_datetime)
    Schulfrei.Datum     = pd.to_datetime(Schulfrei.Datum, format = "%d.%m.%Y")
    Feiertage.Datum     = pd.to_datetime(Feiertage.Datum, format = "%Y-%m-%d")
    Wind.Datum          = pd.to_datetime(Wind.Datum, format = "%Y%m%d%H")
    Windspitzen.Datum   = pd.to_datetime(Windspitzen.Datum, format = "%Y%m%d%H")
    Luftdruck.Datum     = pd.to_datetime(Luftdruck.Datum, format = "%Y%m%d%H")
    Feuchtigkeit.Datum  = pd.to_datetime(Feuchtigkeit.Datum, format = "%Y%m%d%H")
    Temp.Datum          = pd.to_datetime(Temp.Datum, format = "%Y%m%d%H")
    Niederschlag.Datum  = pd.to_datetime(Niederschlag.Datum, format = "%Y%m%d%H")
    Bewoelkung.Datum    = pd.to_datetime(Bewoelkung.Datum, format = "%Y%m%d%H")

    #dfx = Luftqualitaet.drop(columns=['Stationscode']).copy()

    # ensure for each hour a row in the dataset
    start = Luftqualitaet[Luftqualitaet["PM10"].notna()].min()["Datum"]
    end = Luftqualitaet[Luftqualitaet["PM10"].notna()].max()["Datum"]
    num_hours = (end - start) / np.timedelta64(1, 'h') + 1
    dfx = pd.DataFrame(pd.date_range(start, periods=num_hours, freq="60min"), columns = ["Datum"])

    # merge data into data set
    dfx = pd.merge(dfx, Luftqualitaet.drop(columns=['Stationscode']), how='left', on="Datum")
    dfx = pd.merge_ordered(dfx , Wind.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)
    dfx = pd.merge_ordered(dfx , Windspitzen.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)
    dfx = pd.merge_ordered(dfx , Temp.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)
    dfx = pd.merge_ordered(dfx , Niederschlag.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)
    dfx = pd.merge_ordered(dfx , Feuchtigkeit.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)
    dfx = pd.merge_ordered(dfx , Bewoelkung.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)
    dfx = pd.merge_ordered(dfx , Luftdruck.drop(columns=['Stations_ID', 'eor']), 
                                    on= 'Datum', how = 'left', fill_method=None)

    dfx["Day"] = pd.to_datetime(dfx['Datum']).dt.date
    dfx["Day"] = pd.to_datetime(dfx["Day"], format = "%Y-%m-%d")
    dfx = pd.merge_ordered(dfx , Feiertage, left_on= 'Day', right_on= 'Datum', 
                           fill_method=None, how = "left", suffixes=(None, "_y"))
    dfx = dfx.drop('Datum_y',axis = 1)
    dfx['Feiertag'] = dfx['Feiertag'].fillna(0)
    dfx = pd.merge_ordered(dfx , Schulfrei, left_on= 'Day', right_on= 'Datum', 
                           fill_method=None, how = "left", suffixes=(None, "_y"))
    dfx = dfx.drop('Datum_y',axis = 1)
    #dfx = dfx.drop('Day',axis = 1)

    # set missing values to NaN
    dfx["D"] = dfx["D"].mask(dfx["D"] == 0)
    dfx["V_N"] = dfx["V_N"].mask(dfx["V_N"] == -1)

    c1 = ['F', 'FX_911', 'TT_TU', 'RF_TU', 'R1', 'TF_STD', 'P_STD', 'RS_IND', 'WRTR',  'PP_TER']
    for c in c1:
        dfx[c] = dfx[c].mask(dfx[c] < 0)

    # delete any duplicates of hours, always keep first row
    Datum = ""
    for index, row in dfx.iterrows():
        if row["Datum"] == Datum:
            dfx.drop(index, inplace = True)
        else:
            Datum = row["Datum"]
    
    return dfx

def make_PM10_df1(luftmessstation, wetterstation, verzeichnis = os.path.join("..", "resources", "Data"), bundesland = 'SH'):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
    ------------------------------------------------------------------"""
    
    df = make_PM10_df(luftmessstation, wetterstation, verzeichnis, bundesland)
    df = df.loc[:, ["Datum", "PM10", "Schulfrei", "Feiertag"] + w_cols]
    
    return df

def prep_base_model_1(luftmessstation, verzeichnis = os.path.join("..", "resources", "Data")):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        verzeichnis: Pfad zu den Daten
    Rückgabe:
        ein data_frame mit PM10 Werten und one-hot encoded Datumsfeldern
    ------------------------------------------------------------------"""
     
    Luftqualitaet = pd.read_csv(os.path.join(verzeichnis,luftmessstation),sep = ';')
    Luftqualitaet.columns = ['Stationscode', 'Datum', 'PM10', 'Ozon', 'NO2', 'Quality']
    
    # cast "Datum" into datetime type
    Luftqualitaet.Datum = Luftqualitaet.Datum.apply(custom_to_datetime)

    # select target and features
    df = Luftqualitaet.loc[:, ("Datum", "PM10")]
    
    # delete any duplicates of hours, always keep first row
    Datum = ""
    for index, row in df.iterrows():
        if row["Datum"] == Datum:
            df.drop(index, inplace = True)
        else:
            Datum = row["Datum"]
    
    df = make_DateTime_features(df)
    
    df = df.dropna()
       
    return df

def prep_data_model_0(luftmessstation, wetterstation, verzeichnis = os.path.join("..", "resources", "Data"), bundesland = 'SH'):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
    ------------------------------------------------------------------"""
    
    df = make_PM10_df(luftmessstation, wetterstation, verzeichnis, bundesland)
    df = df.loc[:, ["Datum", "PM10", "Schulfrei", "Feiertag"] + w_cols_select]
    
    df = make_DateTime_features(df)
                
    ## forward fill any NaNs in PP_TER (air-pressure)
    df["PP_TER"] = df["PP_TER"].fillna(method = 'ffill')
    df["PP_TER"] = df["PP_TER"].fillna(method = 'bfill') # for few rows at the beginning
    
    ## forward fill any NaNs in D (wind-direction)
    df["D"] = df["D"].fillna(method = 'ffill')
    df["D"] = df["D"].fillna(method = 'bfill') # for few rows at the beginning
    
    ## forward fill any NaNs in V_N (clouds)
    df["V_N"] = df["V_N"].fillna(method = 'ffill')
    df["V_N"] = df["V_N"].fillna(method = 'bfill') # for few rows at the beginning
    
    # encoding of wind direction
    def wind_direction(grad):
        direction = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = int((grad + 22.5) / 45) % 8
        return direction[index]
    
    df["D"] = df["D"].apply(lambda x : wind_direction(x))
    
    # one hot encoding of column Feiertag
    one_hot = pd.get_dummies(df['Feiertag'])
    df = df.drop('Feiertag',axis = 1) # Drop column Feiertag as it is now encoded
    df = df.join(one_hot)
    df = df.drop(0,axis = 1)
    
    # one hot encoding of column D (Wind Direction)
    one_hot = pd.get_dummies(df['D'], prefix = 'wind')
    df = df.drop('D',axis = 1)
    df = df.join(one_hot)
    
    

    return df

def prep_data_model_1(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', interval = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        intervall: für wie viele Stunden werden Wetterdaten embedded
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten über
        die vergangenen "interval" Stunden
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_0(luftmessstation, wetterstation, verzeichnis, bundesland)
    
    # embedding of weather for "interval" hours
    interval = 24
    df = df.sort_values(by="Datum")
    df_w = df[w_cols]
    df_neu = df[interval - 1:].copy()
    len_neu = df_neu.shape[0]

    for i in range(0, interval-1):
        df_append = df_w[i: i + len_neu].copy()
        new_cols = []
        for col in list(df_append.columns):
            new_cols += [col + "_{:n}".format(i)]
        df_append.columns = new_cols
        df_append.head(10)

        for col in new_cols:
            df_neu[col] = list(df_append[col])

    df_neu = df_neu.dropna()
    df = df_neu.copy() # de-fragment resulting dataframe  
        
    return df

def prep_data_model_2(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', gap = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        gap: für welche Stunde zurück werden Wetterdaten embedded
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten der aktuellen 
        Stunde und der Stunde "gap" Stunden vorher.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_0(luftmessstation, wetterstation, verzeichnis, bundesland)
    
    df = df.sort_values(by="Datum")
    df_w = df[w_cols]
    df_neu = df[gap:].copy()
    len_neu = df_neu.shape[0]
    new_cols = []
    
    for col in w_cols:
        new_cols += [col + "_gap"]
        
    df_append = df_w[0: len_neu].copy()
    df_append.columns = new_cols
    
    for col in new_cols:
        df_neu[col] = list(df_append[col])

    df_neu = df_neu.dropna()
    df = df_neu.copy() # de-fragment resulting dataframe     
            
    return df

def prep_data_model_3(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', gap = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        gap: für welche Stunde zurück wird der PM10 Wert embedded
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten der aktuellen 
        Stunde und der Stunde "gap" Stunden vorher.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³) (NOW)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
                "PM10_gap" - PM10 measured (µg/m³) (gap hours BEFORE)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_0(luftmessstation, wetterstation, verzeichnis, bundesland)
    
    w_cols = "PM10"
    df = df.sort_values(by="Datum")
    df_w = df[w_cols]
    df_neu = df[gap:].copy()
    len_neu = df_neu.shape[0]       
    df_append = df_w[0: len_neu].copy()
    df_append.columns = ["PM10_gap"]
    df_neu["PM10_gap"] = list(df_append)
    
    df_neu = df_neu.dropna()
    df = df_neu.copy() # de-fragment resulting dataframe   
            
    return df

def prep_data_model_5(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', embeddings = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        embedding: für welche Stunde zurück wird der PM10 Wert embedded und
                   für wie viele Stunden werden Wetterdaten embedded
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten der aktuellen 
        Stunde und der Stunde "gap" Stunden vorher.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³) (NOW)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
                "PM10_gap" - PM10 measured (µg/m³) (gap hours BEFORE)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_1(luftmessstation, wetterstation, 
                           verzeichnis = verzeichnis, 
                           bundesland = bundesland , 
                           interval = embeddings+1)
    
    df = df.sort_values(by="Datum")
    df_PM10 = df["PM10"]
    df_neu = df[embeddings:].copy()
    len_neu = df_neu.shape[0]       
    df_append = df_PM10[0: len_neu].copy()
    df_neu["PM10_24"] = list(df_append)
    
    df_neu = df_neu.dropna()
    df = df_neu.copy() # de-fragment resulting dataframe   
            
    return df

def prep_data_model_6(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', embeddings = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        embedding: für wie viele Stunden werden Wetterdaten und PM10 Daten embedded
                   PM10 wird nicht für die ersten24 Stunden embedded
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten der aktuellen 
        Stunde und der Stunde "gap" Stunden vorher.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³) (NOW)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
                "PM10_gap" - PM10 measured (µg/m³) (gap hours BEFORE)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_0(luftmessstation, wetterstation, 
                           verzeichnis = verzeichnis, 
                           bundesland = bundesland )
    
    
    cols_24 = list(df.columns[1:])           ## embedd all columns but "Datum"
    cols_23 = cols_24[1:]                    ## embedd all columns but "Datum and "PM10" 
    df = df.sort_values(by="Datum")
    df_neu = df.tail(df.shape[0] -embeddings)
    len_neu = df_neu.shape[0]

    for i in range(1, embeddings+1):
        if i > embeddings - 23: #< 24:
            embedd_cols = cols_23
        else:
            embedd_cols = cols_24

    df = df_neu.copy() # de-fragment resulting dataframe    
            
    return df

def prep_data_model_7(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', embeddings = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        embedding: für wie viele Stunden werden alle Daten ausser PM10 embedded

    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten der aktuellen 
        Stunde und der Stunde "gap" Stunden vorher.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³) (NOW)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
                "PM10_gap" - PM10 measured (µg/m³) (gap hours BEFORE)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_0(luftmessstation, wetterstation, 
                           verzeichnis = verzeichnis, 
                           bundesland = bundesland )
    
    ## embedd all columns but "Datum and "PM10"
    embedd_cols = list(df.columns[2:])
 
    df = df.sort_values(by="Datum")
    df_neu = df.tail(df.shape[0] -embeddings)
    len_neu = df_neu.shape[0]

    for i in range(1, embeddings+1):
        df_append = df.iloc[i-1:len_neu+i-1 , :][embedd_cols]        ## extract data to be embedded from df

        for col in embedd_cols:                                      ## embedd all cols to df_neu
            df_neu[col + "_{:n}".format(i)] = list(df_append[col])
    
    df = df_neu.copy() # de-fragment resulting dataframe    
            
    return df



def prep_data_model_8(luftmessstation, wetterstation, 
                      verzeichnis = os.path.join("..", "resources", "Data"), 
                      bundesland = 'SH', embeddings = 24):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
        bundesland: 'SH', 'BW'
        embedding: für welche Stunde zurück werden der PM10 Wert, die Schul und Feiertage embedded und
                   für wie viele Stunden werden Wetterdaten embedded
    Rückgabe:
        ein data_frame mit PM10 Werten und ausgewählten Wetterdaten der aktuellen 
        Stunde und der Stunde "gap" Stunden vorher.
        Gleiche Wetterdaten können auf Wetter.com für eine Vorhersage
        der nächsten 7 Tage abgerufen werden.
        Folgende Daten werden geliefert:
                "Datum"- pandas datetime
                "PM10" - PM10 measured (µg/m³) (NOW)
                "Schulfrei" - school free in SH (1/0)
                "Feiertag" - feiertag (1/0)
                "F" - wind velocity (in m/sec
                "D" - wind direction (in deg)
                "R1" - rain amount per hour (in mm)"
                "TT_STD" - Lufttemperatur in 2m Hoehe (in °C)
                "RF_STD" - Stundenwerte der Relativen Feuchte (in %)
                "V_N" - degree of coverage of all clouds (in eights)
                "PP_TER" - air pressure (in hpa)
                "PM10_gap" - PM10 measured (µg/m³) (gap hours BEFORE)
    ------------------------------------------------------------------"""
    
    df = prep_data_model_1(luftmessstation, wetterstation, 
                           verzeichnis = verzeichnis, 
                           bundesland = bundesland , 
                           interval = embeddings+1)
    
    df = df.sort_values(by="Datum")
    df_PM10 = df["PM10"]
    df_neu = df[embeddings:].copy()
    len_neu = df_neu.shape[0]       
    df_append = df_PM10[0: len_neu].copy()
    df_neu["PM10_24"] = list(df_append)
    
    df_append = df_neu[1:].copy()
    df_neu = df_neu[0:-1]
    new_cols = ['F', 'R1', 'TT_STD', 'RF_STD', 'V_N', 'PP_TER',
                'wind_E', 'wind_N', 'wind_NE', 'wind_NW', 'wind_S', 'wind_SE', 'wind_SW', 'wind_W']
    
    for col in new_cols:
        df_neu[col+"_next"] = list(df_append[col])
   
    df_neu = df_neu.dropna()
    df = df_neu.copy() # de-fragment resulting dataframe   
            
    return df


def build_data_arrays(df, split = 8760, f = 0.5, seed = 42, shuffle_train = False):
    """------------------------------------------------------------------
    Create training, validation and test data sets (last "split" hours for validation and test).
        - training data set: all data before the last available data from 365 days
        - validation data set: 50% of all data from last 365 days (shuffled)
        - test data set: 50% of all data from last 365 days (shuffled) 
    parameter:
        df    : the full pandas dataset
        split : how many hours will be split from df for test and validation data (8760 = 1 year)
        f     : the fraction of data for validation (1 = size of test + validation data)
        seed  : the seed value for random_state
    returns
        numpy arrays for train_Y, train_X, val_Y, val_X, test_Y, test_X
        and pandas datasets for train, val and test
    ------------------------------------------------------------------"""
    # split pandas dataframes
    df = df.sort_values(by="Datum")
    len_df = df.shape[0]
    df_train=df[:len_df-split]
    df_val=df[len_df-split:]
    df_test = df_val
    f = 0.5 
    df_val=df_val.sample(frac=1-f,random_state=seed)
    df_test=df_test.drop(df_val.index)
    
    ## shuffle train dataframe
    if shuffle_train:
        df_train = df_train.sample(frac=1)
        
    # create numpy arrays for targets from pandas dataframes
    train_Y = np.array(df_train.loc[:, ["PM10"]])
    train_Y = np.reshape(train_Y,(1,len(train_Y))).T
    val_Y = np.array(df_val.loc[:, ["PM10"]])
    val_Y = np.reshape(val_Y,(1,len(val_Y))).T
    test_Y = np.array(df_test.loc[:, ["PM10"]])
    test_Y = np.reshape(test_Y,(1,len(test_Y))).T

    ## create numpy arrays for features from pandas dataframes
    cols = list(df.columns)
    train_X = np.array(df_train.loc[:, cols[2:]])  # remove "Datum" and "PM10" from features
    val_X = np.array(df_val.loc[:, cols[2:]])      # remove "Datum" and "PM10" from features
    test_X = np.array(df_test.loc[:, cols[2:]])    # remove "Datum" and "PM10" from features
    
    return train_Y, train_X, val_Y, val_X, test_Y, test_X, df_train, df_val, df_test

def make_PM10_df_v0(luftmessstation, wetterstation, verzeichnis = os.path.join("..", "resources", "Data")):
    """------------------------------------------------------------------
    Einlesen und Zusammenstellen der Daten
    Parameter:
        luftmessstation: Daten der Luftmessstation
        wetterstation: Name des Verzeichnisses zu den Wetterdaten
        verzeichnis: Pfad zu den Daten
    Rückgabe:
        ein data_frame mit allen Daten
    ------------------------------------------------------------------"""

    def custom_to_datetime(date):
        """------------------------------------------------------------------
        Konvertiere einen String mit Datum und Zeit (MEZ) in ein datetime type (UTC) ###
        Parameter:
            date: String im Format "TT.MM.YY SS:MM" (MEZ)
        Rueckgabe:
            ein datetime (UTC)
        ------------------------------------------------------------------"""

        # If the time is 24, set it to 0 and increment day by 1
        if date[12:14] == '24':
            date = date.replace('24:00', '00:00')
            return pd.to_datetime(date, format = "%d.%m.%Y %H:%M", exact=False) + pd.Timedelta(days=1) + pd.Timedelta(hours=-1)
        else:
            return pd.to_datetime(date, format = "%d.%m.%Y %H:%M", exact=False) + pd.Timedelta(hours=-1)

    Luftqualitaet = pd.read_csv(os.path.join(verzeichnis,luftmessstation),sep = ';')
    Schulfrei = pd.read_csv(os.path.join(verzeichnis,"Schulfrei_SH.csv"),sep = ',')
    Feiertage = pd.read_csv(os.path.join(verzeichnis,"Feiertage_SH.csv"),sep = ',')

    path = os.path.join(verzeichnis, wetterstation)

    Wind = pd.read_csv(os.path.join(path,"Wind.csv"),sep = ',')
    Temp = pd.read_csv(os.path.join(path,"Temperatur_und_relative_Feuchte.csv"),sep = ',')
    Windspitzen = pd.read_csv(os.path.join(path,"Windspitzen.csv"),sep = ',')
    Bewoelkung = pd.read_csv(os.path.join(path,"Bewoelkung.csv"),sep = ',')
    Luftdruck = pd.read_csv(os.path.join(path,"Luftdruck.csv"),sep = ',')
    Feuchtigkeit = pd.read_csv(os.path.join(path,"Feuchtigkeit.csv"),sep = ',')
    Niederschlag = pd.read_csv(os.path.join(path,"Niederschlag.csv"),sep = ',')

    Luftqualitaet.columns = ['Stationscode', 'Datum', 'PM10', 'Ozon', 'NO2', 'Luftquality']
    Wind.columns = ['Stations_ID', 'Datum', 'QN_3_W', 'F', 'D', 'eor']
    Feuchtigkeit.columns = ['Stations_ID', 'Datum', 'QN_8_F', 'ABSF_STD', 'VP_STD', 'TF_STD', 'P_STD', 'TT_STD', 'RF_STD', 'TD_STD', 'eor']
    Temp.columns = ['Stations_ID', 'Datum', 'QN_9_T', 'TT_TU', 'RF_TU' , 'eor']
    Niederschlag.columns = ['Stations_ID', 'Datum', 'QN_8_N', 'R1', 'RS_IND', 'WRTR', 'eor']
    Bewoelkung.columns = ['Stations_ID', 'Datum', 'QN_8_B', 'V_N_I', 'V_N', 'eor']
    if Luftdruck.shape[1]==5:
        Luftdruck.columns = ['Stations_ID', 'Datum', 'QN_4_L', 'PP_TER', 'eor']
    else:
        Luftdruck.columns = ['Stations_ID', 'Datum', 'QN_4_L', 'PP_TER', 'P0', 'eor']
    Windspitzen.columns = ['Stations_ID', 'Datum', 'QN_8_W', 'FX_911', 'eor']

    Luftqualitaet.Datum = Luftqualitaet.Datum.apply(custom_to_datetime)
    Schulfrei.Datum     = pd.to_datetime(Schulfrei.Datum, format = "%d.%m.%Y")
    Feiertage.Datum     = pd.to_datetime(Feiertage.Datum, format = "%Y-%m-%d")
    Wind.Datum          = pd.to_datetime(Wind.Datum, format = "%Y%m%d%H")
    Windspitzen.Datum   = pd.to_datetime(Windspitzen.Datum, format = "%Y%m%d%H")
    Luftdruck.Datum     = pd.to_datetime(Luftdruck.Datum, format = "%Y%m%d%H")
    Feuchtigkeit.Datum  = pd.to_datetime(Feuchtigkeit.Datum, format = "%Y%m%d%H")
    Temp.Datum          = pd.to_datetime(Temp.Datum, format = "%Y%m%d%H")
    Niederschlag.Datum  = pd.to_datetime(Niederschlag.Datum, format = "%Y%m%d%H")
    Bewoelkung.Datum    = pd.to_datetime(Bewoelkung.Datum, format = "%Y%m%d%H")

    Dataset_long = Luftqualitaet.drop(columns=['Stationscode']).copy()

    Dataset_long = pd.merge_asof(Dataset_long , Schulfrei, on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Feiertage, on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Wind.drop(columns=['Stations_ID', 'eor']), on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Windspitzen.drop(columns=['Stations_ID', 'eor']), on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Temp.drop(columns=['Stations_ID', 'eor']), on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Niederschlag.drop(columns=['Stations_ID', 'eor']), on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Feuchtigkeit.drop(columns=['Stations_ID', 'eor']), on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Bewoelkung.drop(columns=['Stations_ID', 'eor']), on= 'Datum')
    Dataset_long = pd.merge_asof(Dataset_long , Luftdruck.drop(columns=['Stations_ID', 'eor']), on= 'Datum')

    # set missing values to NaN
    Dataset_long["D"] = Dataset_long["D"].mask(Dataset_long["D"] == 0)
    Dataset_long["V_N"] = Dataset_long["V_N"].mask(Dataset_long["V_N"] == -1)

    c1 = ['F', 'FX_911', 'TT_TU', 'RF_TU', 'R1', 'TF_STD', 'P_STD', 'RS_IND', 'WRTR',  'PP_TER']
    for c in c1:
        Dataset_long[c] = Dataset_long[c].mask(Dataset_long[c] < 0)

    return Dataset_long