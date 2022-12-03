import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns
from scipy import stats
from scipy.stats import yeojohnson


uAndes = open("tiempo_uandes_exportado.csv")
qNormal = open("330020_202211_Temperatura.csv")

qNormal.readline()
uAndes.readline()

andes = uAndes.readlines()
qnormal = qNormal.readlines()

print(len(andes))
print(len(qnormal))

andesTemp = []
qNormalTemp = []
timeStamp = []

for i in range(len(andes)):
    andesTemp.append(float(andes[i].split(",")[2]))
    qNormalTemp.append(float(qnormal[i*5].split(";")[4]))
    timeStamp.append(qnormal[i*5].split(";")[3])




diff = np.subtract(andesTemp, qNormalTemp)
num = [i for i in range(len(diff))]

#print(diff)
#print(num)

'''pyplot.scatter(num, diff)
#adjust the size of plot
pyplot.gcf().set_size_inches(15, 10)

pyplot.show()


diff.sort()
pyplot.scatter(num, diff)
#adjust the size of plot
pyplot.gcf().set_size_inches(15, 10)

pyplot.show()'''

# Apply Normalization

x_norm, _ = yeojohnson(diff)

# Plot the distribution
ax = sns.displot(x_norm, kind = "kde",color = "#e64e4e", height=10, aspect=2,
            linewidth = 5 )
ax.fig.suptitle('Distribution after YeoJohnson transfomation', size = 20)
ax.set(xlabel = 'BoxCox transformed data', ylabel = 'Density')
# Plot the mean and standard deviation
ax.ax.axvline(x = np.mean(x_norm), color = "#4e4e4e", linestyle = "--", label = "Mean")
ax.ax.axvline(x = np.mean(x_norm) + np.std(x_norm), color = "#4ee64e", linestyle = "--", label = "Std")
ax.ax.axvline(x = np.mean(x_norm) - np.std(x_norm), color = "#4ee64e", linestyle = "--")
ax.ax.legend()



pyplot.show()
maxIndex = np.argmax(diff)

print("Maximo error: ", diff[maxIndex])
print("Average error: ", np.average(diff))
print("Standard deviation: ", np.std(diff))

print("Tiempo: ", timeStamp[maxIndex])

uAndes.close()
qNormal.close()