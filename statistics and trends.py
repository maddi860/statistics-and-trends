# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:24:11 2025

@author: mt24abs
"""

import pandas as pd
import matplotlib.pyplot as plt

"""
data is being read from the csv filed and are being made into dataframes,
then the data is being cleaned by removing the NaN rows.
"""

co2 = pd.read_csv('co2.csv')
#print(co2)

df_co2 = pd.DataFrame(co2)
#print(df)

df_new = df_co2.dropna()
#print(df_new)

#using .describe() to get the summary statistics
summary_co2 = df_co2.describe()
#print(summary_co2)

"""
I'm going to use the slicing method iloc, so i can have only the first and 
last 20 years of the dataframe for each category of country (rich, poor, and
middle).
"""
#rich
pop_uk_f20 = df_co2.iloc[46, 1:22]
pop_usa_f20 = df_co2.iloc[134, 1:22]
pop_uk_l20 = df_co2.iloc[46, 34:55]
pop_usa_l20 = df_co2.iloc[134, 34:55]

#middle
co2_thia_f20 = df_co2.iloc[125, 1:22]
co2_ken_f20 = df_co2.iloc[69, 1:22]
co2_thia_l20 = df_co2.iloc[125, 34:55]
co2_ken_l20 = df_co2.iloc[69, 34:55]

#poor
co2_ven_f20 = df_co2.iloc[136, 1:22]
co2_ven_l20 = df_co2.iloc[136, 34:55]
co2_gin_f20 = df_co2.iloc[104, 1:22]
co2_gin_l20 = df_co2.iloc[104, 34:55]


"""
Now I will use pyplot to plot a scatter graph and bar chart for the population,
and the amount of co2 for the first and last 20 years in each country.
"""
#rich countries first and last 20 years of CO2 emissions
#UK
plt.figure()
plt.subplot(2, 2, 1).set_title('UK CO2 emissions 1970-90')
plt.plot(pop_uk_f20, color = 'red')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.6)

plt.subplot(2, 2, 2).set_title('UK CO2 emissions 2003-23')
plt.plot(pop_uk_l20, color = 'green')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.6)
#USA
plt.subplot(2, 2, 3).set_title('USA CO2 emissions 1970-90')
plt.plot(pop_usa_f20, color = 'blue')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.004)

plt.subplot(2, 2, 4).set_title('USA CO2 emissions 2003-23')
plt.plot(pop_usa_l20, color = 'purple')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.004)

plt.subplots_adjust(wspace = 0.5, hspace = 0.6)#adjusts the subplots
plt.savefig('rich plots')

#middle countries first and last 20 years of CO2 emissions
#Thialand
plt.figure()#creares a new figure for each category
plt.subplot(2, 2, 1).set_title('Thialand CO2 emissions 1970-90')
plt.plot(co2_thia_f20, color = 'red')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.02)

plt.subplot(2, 2, 2).set_title('Thialand CO2 emissions 2003-23')
plt.plot(co2_thia_l20, color = 'green')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.02)
#Kenya
plt.subplot(2, 2, 3).set_title('Kenya CO2 emissions 1970-90')
plt.plot(co2_ken_f20, color = 'blue')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.0025)

plt.subplot(2, 2, 4).set_title('Kenya CO2 emissions 2003-23')
plt.plot(co2_ken_l20, color = 'purple')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.0025)

plt.subplots_adjust(wspace = 0.3, hspace = 0.6)
plt.savefig('middle plots')

#poor countries first and last 20 years of CO2 emissions
#Venuzuela
plt.figure()
plt.subplot(2, 2, 1).set_title('Venuzuela CO2 emissions 1970-90')
plt.plot(co2_ven_f20, color = 'red')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.02)

plt.subplot(2, 2, 2).set_title('Venuzuela CO2 emissions 2003-23')
plt.plot(co2_ven_l20, color = 'green')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.02)
#Papua New Guinea
plt.subplot(2, 2, 3).set_title('Papua New Guinea CO2 emissions 1970-90')
plt.plot(co2_gin_f20, color = 'blue')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.0011)

plt.subplot(2, 2, 4).set_title('Papua New Guinea CO2 emissions 2003-23')
plt.plot(co2_gin_l20, color = 'purple')
plt.xlabel('Years')
plt.xticks(rotation = 270, fontsize = 8)
plt.ylim(0, 0.0011)

plt.subplots_adjust(wspace = 0.7, hspace = 0.6)
plt.savefig('poor plots')





