import numpy as np
import matplotlib.pyplot as pyplot



uAndes = open("tiempo_uandes_exportado.csv")
qNormal = open("330020_202208_AguaCaida.csv")

qNormal.readline()
uAndes.readline()

andes = uAndes.readlines()
qnormal = qNormal.readlines()

print(len(andes))
print(len(qnormal))

andesPrec = []
qNormalPrec = []
timeStamp = []

for i in range(len(andes)):
    if andes[i].split(",")[1] != "0.0" and qnormal[i*5].split(";")[4] != "0.0":

        andesPrec.append(float(andes[i].split(",")[1]))
        qNormalPrec.append(float(qnormal[i*5].split(";")[4]))
        timeStamp.append(qnormal[i*5].split(";")[3])


#print(andesPrec)
#print(qNormalPrec)



diff = np.subtract(andesPrec, qNormalPrec)
num = [i for i in range(len(diff))]

print(diff)
print(num)

pyplot.scatter(num, diff)
pyplot.show()

maxIndex = np.argmax(diff)

print("Maximo error: ", diff[maxIndex])
print("Tiempo: ", timeStamp[maxIndex])

uAndes.close()
qNormal.close()