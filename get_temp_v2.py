import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('330020_202211_Temperatura.csv', sep=';')
df2 = pd.read_csv('tiempo_uandes_exportado.csv', sep=',')

df1.drop(['codigoNacional', 'idEquipo', 'idPista', 'tsMin15m', 'tMin12Horas', 'tMin24Horas', 'tsMax15m', 'tMax12Horas', 'tMax24Horas',
'horaTMin12Horas', 'horaTMax12Horas', 'horaTMin24Horas', 'horaTMax24Horas', 'momentoRegistro', 'ts02', 'ts10', 'ts30',
'tsMed15m', 'tsSupMax15m', 'tsSupMed15m', 'tsSupMin15m', 'tMin1M', 'tMax1M'], axis=1, inplace=True)
df1['momento'] = pd.to_datetime(df1['momento'])
df2['Local_Time'] = pd.to_datetime(df2['Local_Time']).round('1min')
# add 1 hour to local time
df2['Local_Time'] = df2['Local_Time'] + pd.Timedelta(hours=1)

df1.rename(columns={'momento': 'Local_Time'}, inplace=True)

result = pd.merge(df1, df2, on='Local_Time')

print(result.head())

cols = result.columns
figure, ax1 = plt.subplots()
ax1.plot(result[cols[0]], result[cols[1]],linewidth=0.5,zorder=1, label = "Quinta Normal")
ax1.plot(result[cols[0]], result[cols[4]],linewidth=0.5,zorder=1, label = "U Andes")
plt.legend(loc='upper left')
plt.show()

#dataframe with temp diffs
df3 = pd.DataFrame()
df3['Local_Time'] = result['Local_Time']
df3['diff'] = result['ts'] - result['Temp']
mean = df3['diff'].mean()
std = df3['diff'].std()
max = df3['diff'].max()
print("Promedio: ",mean)
print("Desviación Estándar",std)
print("Máximo: ",max)
#plot diff
figure, ax1 = plt.subplots()
ax1.plot(df3['Local_Time'], df3['diff'],linewidth=0.5,zorder=1, label = "Diferencia")
plt.legend(loc='upper left')
plt.show()