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

    df = df[0].str.split(',', expand=True)

    for k in range(df.shape[0]):
        df.iloc[k] = df.iloc[k].str.strip('"')  # remove double quotes

    # transpose
    df_t = df.T.copy()

    # make 1st row as the column head
    df.columns = df.iloc[0]

    df = df.drop(index=df.iloc[0].name).reset_index(drop=True)

    #  make 1st row as column head
    df_t.columns = df_t.iloc[0]

    # Dropping the 1st row
    df_t = df_t.drop(index=df_t.iloc[0].name).reset_index(drop=True)

    return df, df_t

# create function to produce arable land dataframe


def arable_land(df):
    """ This function will produce a dataframe of arable land with all the countries """

    arable_land = df.loc[df.loc[:, 'Indicator Name'] ==
                         'Arable land (% of land area)', :].reset_index(drop=True).transpose()

    # delete unwanted columns
    arable_land = arable_land.drop(
        ['Country Code', 'Indicator Name', 'Indicator Code'])

    #  make 1st row as column head
    arable_land.columns = arable_land.iloc[0]

    # select years from 1961 to 2020
    arable_land = arable_land.loc['1961':'2021']

    return arable_land


# create fucntion for producing line plot of arable land
def arable_land_plot(df):
    """This dataframe will produce line plot of the arable land of selected countries."""

    years = [f"{i:04d}" for i in range(1961, 2021, 10)]   # generate years

    plt.figure(figsize=(5.4, 3.8))

    plt.plot(arable_land.loc[years, 'Pakistan'].astype(
        float), 'b-.', label='Pakistan')
    plt.plot(arable_land.loc[years, 'Germany'].astype(
        float), 'r-.', label='Germany')
    plt.plot(arable_land.loc[years, 'Italy'].astype(
        float), 'g-.', label='Italy')
    plt.plot(arable_land.loc[years, 'Mexico'].astype(
        float), 'c-.', label='Mexico')
    plt.plot(arable_land.loc[years, 'Australia'].astype(
        float), 'y-.', label='Australia')
    plt.plot(arable_land.loc[years, 'Japan'].astype(
        float), 'k-.', label='Japan')
    plt.plot(arable_land.loc[years, 'India'].astype(
        float), 'C1-.', label='India')
    plt.plot(arable_land.loc[years, 'China'].astype(
        float), 'm-.', label='China')

    # set title, legend
    plt.title('Arable Land', fontsize=8)
    plt.legend(bbox_to_anchor=(1.30, 0.81), loc='upper right')

    # save the graph as png
    plt.savefig("arable_land.png", bbox_inches = "tight", dpi=300)
    plt.show()

    return


# create function to produce forerst land dataframe
def forest_land(df):
    """ This function will produce a dataframe of forest land with all the countries """

    forest_land = df.loc[df.loc[:, 'Indicator Name'] ==
                         'Forest area (% of land area)', :].reset_index(drop=True).transpose()

    # delete unwanted columns
    forest_land = forest_land.drop(
        ['Country Code', 'Indicator Name', 'Indicator Code'])

    #  make 1st row as column head
    forest_land.columns = forest_land.iloc[0]

    # select years from 1990 to 2020
    forest_land = forest_land.loc['1990':'2020']

    return forest_land


# create fucntion for producing line plot of forest land
def forest_land_plot(df):
    """This dataframe will produce line plot of the forest land of selected countries."""

    # f string to generate years
    years = [f"{i:04d}" for i in range(1961, 2021, 10)]
    plt.figure()
    plt.plot(arable_land.loc[years, 'Pakistan'].astype(
        float), 'b-.', label='Pakistan')
    plt.plot(arable_land.loc[years, 'Germany'].astype(
        float), 'r-.', label='Germany')
    plt.plot(arable_land.loc[years, 'Italy'].astype(
        float), 'g-.', label='Italy')
    plt.plot(arable_land.loc[years, 'Mexico'].astype(
        float), 'c-.', label='Mexico')
    plt.plot(arable_land.loc[years, 'Australia'].astype(
        float), 'y-.', label='Australia')
    plt.plot(arable_land.loc[years, 'Japan'].astype(
        float), 'k-.', label='Japan')
    plt.plot(arable_land.loc[years, 'India'].astype(
        float), 'C1-.', label='India')
    plt.plot(arable_land.loc[years, 'China'].astype(
        float), 'm-.', label='China')

    # set title, legend
    plt.title('Forest Land', fontsize=8)
    plt.legend(bbox_to_anchor=(1.27, 0.81), loc='upper right')

    # save the graph as png
    plt.savefig("forest_land.png", bbox_inches = "tight", dpi=300)
    plt.show()

    return


# create function to produce green house gas emmision dataframe
def green_house_gas_emmi(df):
    """ This function will produce a dataframe of total green house gas emission with all the countries """

    green_house_gas_emmi = df.loc[df.loc[:, 'Indicator Name'] ==
                                  'Total greenhouse gas emissions (kt of CO2 equivalent)', :].reset_index(drop=True).transpose()

    # delete unwanted columns
    green_house_gas_emmi = green_house_gas_emmi.drop(
        ['Country Code', 'Indicator Name', 'Indicator Code'])

    #  make 1st row as column head
    green_house_gas_emmi.columns = green_house_gas_emmi.iloc[0]

    # select years from 1990 to 2020
    green_house_gas_emmi = green_house_gas_emmi.loc['1990':'2019']

    return green_house_gas_emmi


# create fucntion for producing green house gas emission bar plot
def green_house_gas_bar_plot(df):
    """This function will product the bar plot of green house gas emission of different countries of different years. """

    green_house_df = pd.DataFrame({'Pakistan': green_house_gas_emmi['Pakistan'].astype(float),
                                   'Germany': green_house_gas_emmi['Germany'].astype(float),
                                   'Italy': green_house_gas_emmi['Italy'].astype(float),
                                   'Mexico': green_house_gas_emmi['Mexico'].astype(float),
                                   'China': green_house_gas_emmi['China'].astype(float),
                                   'Sri Lanka': green_house_gas_emmi['Sri Lanka'].astype(float),
                                   'Australia': green_house_gas_emmi['Australia'].astype(float),
                                   'Japan': green_house_gas_emmi['Japan'].astype(float),
                                   'Ireland': green_house_gas_emmi['Ireland'].astype(float),
                                   'India': green_house_gas_emmi['India'].astype(float)
                                   })

    green_house_df = green_house_df.transpose()

    rows = green_house_df.index.values
    green_house_df["Country Name"] = rows

    plt.figure(figsize=(5.4, 3.8))
    green_house_df.plot(x="Country Name", y=[
                        f"{i:04d}" for i in range(1990, 2020, 5)], kind="bar")

    # rotate xticks and set fontsize
    plt.xticks(rotation=45, fontsize=8)

    # set yticks font size
    plt.yticks(fontsize=8)

    # set label, title and legend
    plt.xlabel('Country Name', fontsize=8)
    plt.title('Total greenhouse gas emissions (kt of CO2 equivalent)', fontsize=8)
    plt.legend(loc='upper right', fontsize=8)

    # save as png
    plt.savefig("green_house_gas.png", bbox_inches = "tight", dpi=300)

    plt.show()

    return


# create function to produce total gdp dataframe
def gdp_total(df):
    """ This function will produce a dataframe of total gdp of different countries """

    gdp_total = df.loc[df.loc[:, 'Series Name'] ==
                       'GDP (current US$)', :].reset_index(drop=True).transpose()

    # delete unwanted columns
    gdp_total = gdp_total.drop(['Country Code', 'Series Name', 'Series Code'])

    # make 1st row as column head
    gdp_total.columns = gdp_total.iloc[0]

    # select years from 1990 to 2019
    gdp_total = gdp_total.loc['1990 [YR1990]':'2019 [YR2019]']

    return gdp_total


# create fucntion for producing gdp bar plot
def gdp_bar_plot(df):
    """This function will product the bar plot of total gdp of different countries of different years. """

    # create gdp_total dataframe
    gdp_total_df = pd.DataFrame({'Pakistan': gdp_total['Pakistan'].astype(float),
                                 'Germany': gdp_total['Germany'].astype(float),
                                'Italy': gdp_total['Italy'].astype(float),
                                 'Mexico': gdp_total['Mexico'].astype(float),
                                 'China': gdp_total['China'].astype(float),
                                 'Sri Lanka': gdp_total['Sri Lanka'].astype(float),
                                 'Australia': gdp_total['Australia'].astype(float),
                                 'Japan': gdp_total['Japan'].astype(float),
                                 'Ireland': gdp_total['Ireland'].astype(float),
                                 'India': gdp_total['India'].astype(float)
                                 })

    # transpose
    gdp_total_df = gdp_total_df.transpose()

    # change the column names
    gdp_total_df.columns = list(range(1990, 2020, 1))

    # assign index values to rows
    rows = gdp_total_df.index.values

    # create another column named Country Name with index values
    gdp_total_df["Country Name"] = rows

    # plot
    plt.figure()
    gdp_total_df.plot(x="Country Name", y=[
                      i for i in range(1990, 2020, 5)], kind="bar")

    # rotate xticks, set font size
    plt.xticks(rotation=45, fontsize=8)

    # set font size for y ticks
    plt.yticks(fontsize=8)

    # set title, label, legend
    plt.xlabel('Country Name', fontsize=8)
    plt.title('GDP (current US$)', fontsize=8)
    plt.legend(loc='upper right', fontsize=8)

    # save as png
    plt.savefig("gdp_bar_plot.png", bbox_inches = "tight", dpi=300)
    plt.show()

    return


# create function to produce country dataframe
def country_info(climate, gdp, country_name):
    """this fucntion will produce dataframe of a country with different indicators."""

    green_house = climate.loc[(climate['Country Name'] == country_name) & (
        climate['Indicator Name'] == 'Total greenhouse gas emissions (kt of CO2 equivalent)')]
    green_house = green_house.loc[:, "1990":"2019"].reset_index(drop=True)
    green_house = green_house.iloc[0, :].astype(float)
    green_house.index = list(range(1990, 2020, 1))

    arable_land = climate.loc[(climate['Country Name'] == country_name) & (
        climate['Indicator Name'] == 'Arable land (% of land area)')]
    arable_land = arable_land.loc[:, "1990":"2019"].reset_index(drop=True)
    arable_land = arable_land.iloc[0, :].astype(float)
    arable_land.index = list(range(1990, 2020, 1))

    forest_land = climate.loc[(climate['Country Name'] == country_name) & (
        climate['Indicator Name'] == 'Forest area (% of land area)')]
    forest_land = forest_land.loc[:, "1990":"2019"].reset_index(drop=True)
    forest_land = forest_land.iloc[0, :].astype(float)
    forest_land.index = list(range(1990, 2020, 1))

    urban_pop = climate.loc[(climate['Country Name'] == country_name) & (
        climate['Indicator Name'] == 'Urban population growth (annual %)')]
    urban_pop = urban_pop.loc[:, "1990":"2019"].reset_index(drop=True)
    urban_pop = urban_pop.iloc[0, :].astype(float)
    urban_pop.index = list(range(1990, 2020, 1))

    pop_growth = climate.loc[(climate['Country Name'] == country_name) & (
        climate['Indicator Name'] == 'Population growth (annual %)')]
    pop_growth = pop_growth.loc[:, "1990":"2019"].reset_index(drop=True)
    pop_growth = pop_growth.iloc[0, :].astype(float)
    pop_growth.index = list(range(1990, 2020, 1))

    gdp = gdp.loc[(gdp['Country Name'] == country_name) &
                  (gdp['Series Name'] == 'GDP (current US$)')]
    gdp = gdp.loc[:, "1990 [YR1990]":"2019 [YR2019]"].reset_index(drop=True)
    gdp = gdp.iloc[0, :].astype(float)
    gdp.index = list(range(1990, 2020, 1))

    # Creating DataFrame by passing Dictionary
    df = pd.DataFrame({'Green House Gas': green_house,
                       'Arable Land': arable_land,
                       'Forest Land': forest_land,
                       'Urban Population': urban_pop,
                       'Population Growth': pop_growth,
                       'GDP': gdp
                       })
    return df


# create function to produce heatmap
def heatmap(df, name):
    """This function is for producing the heatmaps."""

    # Plot the heatmap
    plt.figure()
    colormap = sns.color_palette("Set2")
    sns.heatmap(df.corr(), linewidth=1, annot=True, cmap=colormap)

    # set title, xticks and y ticks font size
    plt.title(name, fontsize=8)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)

    # save png
    plt.savefig("india_heatmap.png", bbox_inches = "tight", dpi=300)
    plt.show()

    return


# call make_two_df and create two dataframe
climate, climate_t = make_two_df(pd.read_csv(
    "Data.csv", sep='delimitor', header=None, skiprows=3))


# call arable land
arable_land = arable_land(climate)
arable_land_plot(arable_land)

# call forest land
forest_land = forest_land(climate)
forest_land_plot(forest_land)

# call green_house_gas_emission
green_house_gas_emmi = green_house_gas_emmi(climate)
green_house_gas_bar_plot(green_house_gas_emmi)

# read file into dataframe
gdp = pd.read_csv('gdp.csv')

# call gdp_total
gdp_total = gdp_total(gdp)
gdp_bar_plot(gdp_total)

# call country info with country namee as Mexico
mexico = country_info(climate, gdp, 'Mexico')
heatmap(mexico, "Mexico")

# call country info with country namee as Pakistan
pakistan = country_info(climate, gdp, 'Pakistan')
heatmap(pakistan, 'Pakistan')

# call country info with country namee as India
india = country_info(climate, gdp, 'India')
heatmap(india, 'India')
