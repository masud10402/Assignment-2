# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:35:43 2023

@author: Masud Rana
     ID: 21091274
     MSc in Data Science
     University of Hertforshire
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ignore warnings
import warnings
warnings.filterwarnings('ignore')

# creating function to make two different dataframe
def make_two_df(df):
    
    df = df[0].str.split(',', expand = True)

    for k in range(df.shape[0]):
        df.iloc[k]=df.iloc[k].str.strip('"')  #Getting rid of double quotes

    df_t = df.T.copy()         # For countries as columns

    #print(climate_t)

    df.columns = df.iloc[0]   # making the 1st row as the column head

    df = df.drop(index=df.iloc[0].name).reset_index(drop = True)
    
    df_t.columns = df_t.iloc[0]   #  making the 1st row as each column head
    df_t = df_t.drop(index=df_t.iloc[0].name).reset_index(drop=True) # Dropping the 1st ro  # Dataframe with countries as columns
    
    return df, df_t

def arable_land(df):
    arable_land = df.loc[df.loc[:,'Indicator Name']=='Arable land (% of land area)',:].reset_index(drop=True).transpose()

    arable_land = arable_land.drop(['Country Code', 'Indicator Name', 'Indicator Code'])
    arable_land.columns = arable_land.iloc[0]    #  making the 1st row as each column head
    arable_land = arable_land.loc['1961':'2021']
    
    return arable_land

def arable_land_plot(df):
    years = [f"{i:04d}" for i in range(1961,2021,10)] #f string to generate years
    plt.figure()
    plt.plot(arable_land.loc[years,'Pakistan'].astype (float) ,'b-.', label = 'Pakistan')
    plt.plot(arable_land.loc[years,'Germany'].astype (float) ,'r-.', label = 'Germany')
    plt.plot(arable_land.loc[years,'Italy'].astype (float) ,'g-.', label = 'Italy')
    plt.plot(arable_land.loc[years,'Mexico'].astype (float) ,'c-.', label = 'Mexico')
    plt.plot(arable_land.loc[years,'Sri Lanka'].astype (float) ,'m-.', label = 'Sri Lanka')
    plt.plot(arable_land.loc[years,'Australia'].astype (float) ,'y-.', label = 'Australia')
    plt.plot(arable_land.loc[years,'Japan'].astype (float) ,'k-.', label = 'Japan')
    plt.plot(arable_land.loc[years,'Ireland'].astype (float) ,'C1-.', label = 'Ireland')
    plt.plot(arable_land.loc[years,'India'].astype (float) ,'-.', label = 'India')
    #plt.plot(temp1.loc[years,'China'].astype (float) ,'b-.', label = 'Pakistan')

    plt.legend(bbox_to_anchor=(1.27, 0.81), loc = 'upper right')
    plt.show()
    
    return

def forest_land(df):
    
    forest_land = df.loc[df.loc[:,'Indicator Name']=='Forest area (% of land area)',:].reset_index(drop=True).transpose()

    forest_land = forest_land.drop(['Country Code', 'Indicator Name', 'Indicator Code'])
    forest_land.columns = forest_land.iloc[0]    #  making the 1st row as each column head
    forest_land = forest_land.loc['1990':'2020']
    
    return forest_land

def forest_land_plot(df):
    years = [f"{i:04d}" for i in range(1990,2020,5)] #f string to generate years
    plt.figure()
    plt.plot(forest_land.loc[years,'Pakistan'].astype (float) ,'b-.', label = 'Pakistan')
    plt.plot(forest_land.loc[years,'Germany'].astype (float) ,'r-.', label = 'Germany')
    plt.plot(forest_land.loc[years,'Italy'].astype (float) ,'g-.', label = 'Italy')
    plt.plot(forest_land.loc[years,'Mexico'].astype (float) ,'c-.', label = 'Mexico')
    plt.plot(forest_land.loc[years,'Sri Lanka'].astype (float) ,'m-.', label = 'Sri Lanka')
    plt.plot(forest_land.loc[years,'Australia'].astype (float) ,'y-.', label = 'Australia')
    plt.plot(forest_land.loc[years,'Japan'].astype (float) ,'k-.', label = 'Japan')
    plt.plot(forest_land.loc[years,'Ireland'].astype (float) ,'C1-.', label = 'Ireland')
    plt.plot(forest_land.loc[years,'India'].astype (float) ,'-.', label = 'India')
    #plt.plot(temp1.loc[years,'China'].astype (float) ,'b-.', label = 'Pakistan')
    
    plt.legend(bbox_to_anchor=(1.27, 0.81), loc = 'upper right')
    plt.show()
    return

def green_house_gas_emmi(df):
    
    green_house_gas_emmi = df.loc[df.loc[:,'Indicator Name']=='Total greenhouse gas emissions (kt of CO2 equivalent)',:].reset_index(drop=True).transpose()
    
    green_house_gas_emmi = green_house_gas_emmi.drop(['Country Code', 'Indicator Name', 'Indicator Code'])
    green_house_gas_emmi.columns = green_house_gas_emmi.iloc[0]    #  making the 1st row as each column head
    green_house_gas_emmi = green_house_gas_emmi.loc['1990':'2019']
    
    return green_house_gas_emmi

def green_house_gas_bar_plot(df):
    
    green_house_df = pd.DataFrame({'Pakistan': green_house_gas_emmi['Pakistan'].astype (float),
                                 'Germany': green_house_gas_emmi['Germany'].astype (float),
                                'Italy': green_house_gas_emmi['Italy'].astype (float),
                                 'Mexico': green_house_gas_emmi['Mexico'].astype (float),
                                 'China': green_house_gas_emmi['China'].astype (float),
                                 'Sri Lanka': green_house_gas_emmi['Sri Lanka'].astype (float),
                                   'Australia': green_house_gas_emmi['Australia'].astype (float),
                                 'Japan': green_house_gas_emmi['Japan'].astype (float),
                                'Ireland': green_house_gas_emmi['Ireland'].astype (float),
                                 'India': green_house_gas_emmi['India'].astype (float)
                                })

    green_house_df = green_house_df.transpose()

    rows = green_house_df.index.values
    green_house_df["Country Name"] = rows


    green_house_df.plot(x="Country Name", y = [f"{i:04d}" for i in range(1990,2020,5)], kind="bar")
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlabel('Country Name' ,fontsize=8)
    plt.title('Total greenhouse gas emissions (kt of CO2 equivalent)', fontsize=8)
    plt.legend(loc='upper right', fontsize=8)
    
    return


def gdp_total(df):
    
    gdp_total = df.loc[df.loc[:,'Series Name']=='GDP (current US$)',:].reset_index(drop=True).transpose()
    
    gdp_total = gdp_total.drop(['Country Code', 'Series Name', 'Series Code'])
    gdp_total.columns = gdp_total.iloc[0]    #  making the 1st row as each column head
    gdp_total = gdp_total.loc['1990 [YR1990]':'2019 [YR2019]']
    
    return gdp_total

def gdp_bar_plot(df):
    
    gdp_total_df = pd.DataFrame({'Pakistan': gdp_total['Pakistan'].astype (float),
                                 'Germany': gdp_total['Germany'].astype (float),
                                'Italy': gdp_total['Italy'].astype (float),
                                 'Mexico': gdp_total['Mexico'].astype (float),
                                 'China': gdp_total['China'].astype (float),
                                 'Sri Lanka': gdp_total['Sri Lanka'].astype (float),
                                   'Australia': gdp_total['Australia'].astype (float),
                                 'Japan': gdp_total['Japan'].astype (float),
                                'Ireland': gdp_total['Ireland'].astype (float),
                                 'India': gdp_total['India'].astype (float)
                                })

    gdp_total_df = gdp_total_df.transpose()
    gdp_total_df.columns = list(range(1990, 2020, 1))
    rows = gdp_total_df.index.values
    gdp_total_df["Country Name"] = rows

    gdp_total_df.plot(x="Country Name", y = [i for i in range(1990,2020,5)], kind="bar")
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlabel('Country Name' ,fontsize=8)
    plt.title('GDP (current US$)', fontsize=8)
    plt.legend(loc='upper right', fontsize=8)
    
    return


def country_info(climate, gdp, country_name):
    
    green_house = climate.loc[(climate['Country Name'] == country_name) & (climate['Indicator Name'] == 'Total greenhouse gas emissions (kt of CO2 equivalent)')]
    green_house = green_house.loc[:,"1990":"2019"].reset_index(drop=True)
    green_house = green_house.iloc[0,:].astype(float)
    green_house.index = list(range(1990, 2020, 1))
    
    arable_land = climate.loc[(climate['Country Name'] == country_name) & (climate['Indicator Name'] == 'Arable land (% of land area)')]
    arable_land = arable_land.loc[:,"1990":"2019"].reset_index(drop=True)
    arable_land = arable_land.iloc[0,:].astype(float)
    arable_land.index = list(range(1990, 2020, 1))
    
    forest_land = climate.loc[(climate['Country Name'] == country_name) & (climate['Indicator Name'] == 'Forest area (% of land area)')]
    forest_land = forest_land.loc[:,"1990":"2019"].reset_index(drop=True)
    forest_land = forest_land.iloc[0,:].astype(float)
    forest_land.index = list(range(1990, 2020, 1))
    
    urban_pop = climate.loc[(climate['Country Name'] == country_name) & (climate['Indicator Name'] == 'Urban population growth (annual %)')]
    urban_pop = urban_pop.loc[:,"1990":"2019"].reset_index(drop=True)
    urban_pop = urban_pop.iloc[0,:].astype(float)
    urban_pop.index = list(range(1990, 2020, 1))
    
    
    pop_growth = climate.loc[(climate['Country Name'] == country_name) & (climate['Indicator Name'] == 'Population growth (annual %)')]
    pop_growth = pop_growth.loc[:,"1990":"2019"].reset_index(drop=True)
    pop_growth = pop_growth.iloc[0,:].astype(float)
    pop_growth.index = list(range(1990, 2020, 1))
    
    
    gdp = gdp.loc[(gdp['Country Name'] == country_name) & (gdp['Series Name'] == 'GDP (current US$)')]
    gdp = gdp.loc[:,"1990 [YR1990]":"2019 [YR2019]"].reset_index(drop=True)
    gdp = gdp.iloc[0,:].astype(float)
    gdp.index = list(range(1990, 2020, 1))
    
    frame = {'Green House Gas': green_house,
         'Arable Land': arable_land,
          'Forest Land': forest_land,
             'Urban Population': urban_pop,
             'Population Growth': pop_growth,
             'GDP': gdp
         }
 
    # Creating DataFrame by passing Dictionary
    df = pd.DataFrame(frame)
    return df


def heatmap(df, name):
    
    # Plot the heatmap
    plt.figure(figsize=(6.4, 4.8))
    colormap = sns.color_palette("Set2")
    sns.heatmap(df.corr(), linewidth = 1 , annot = True, cmap=colormap)
    plt.title( name, fontsize = 8)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.show()
    return


climate, climate_t = make_two_df(pd.read_csv("Data.csv", sep='delimitor', header=None, skiprows=3))

arable_land = arable_land(climate)
arable_land_plot(arable_land)

forest_land = forest_land(climate)
forest_land_plot(forest_land)

green_house_gas_emmi = green_house_gas_emmi(climate)
green_house_gas_bar_plot(green_house_gas_emmi)

gdp = pd.read_csv('gdp.csv')

gdp_total = gdp_total(gdp)
gdp_bar_plot(gdp_total)

mexico = country_info(climate, gdp, 'Mexico')
heatmap(mexico, "Mexico")

pakistan = country_info(climate, gdp, 'Pakistan')
heatmap(pakistan, 'Pakistan')

india = country_info(climate, gdp, 'India')
heatmap(india, 'India')

