from urllib import request
import json


# from datetime import datetime, timedelta
# from dateutil.parser import parse
# from dateutil.tz import tzutc
# from lxml import html as html
# import multitry as mt
# from os import path
# import numpy as np
# import sys

arch="tiempo_uandes_exportado.csv"
f=open(arch,'w')

f.write('Local_Time, PrecipTot, Temp\n')

for dia in range(1,31):
    try:
        url=f"https://api.weather.com/v2/pws/history/all?stationId=ILASCO23&format=json&units=m&date=202211{dia:02}&apiKey=5c5b2fcaac8e4c929b2fcaac8eac92f2&numericPrecision=decimal"
        h = request.urlopen(url)
        res=h.read()
        j=json.loads(res)
        for o in j['observations']:
            f.write(",".join(map(str,[o['obsTimeLocal'], o['metric']['precipTotal'], o['metric']['tempAvg']]))+"\n")
    except:
        continue
f.close()

#https://api.weather.com/v2/pws/history/all?stationId=ILASCO23&format=json&units=m&date=20220919&apiKey=5c5b2fcaac8e4c929b2fcaac8eac92f2&numericPrecision=decimal
#https://climatologia.meteochile.gob.cl/application/diario/visorDeDatosEma/330020