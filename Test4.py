import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

#Telemetry
print("---------------------------------------TELEMETRY-----------------------------------------")
df = pd.read_csv ('telemetry_dataset.csv')
df2 = df.fillna(0.0)
print("\n--Correction of missing values applied--\n")

#Show number of missing data in console
columns = ['timestamp','tel_produced_units','tel_activetime','tel_downtime','availability','performance']

#show statistics for each column
for column in columns:
	if column == 'timestamp':
		print(f"Min value of *{column}: {df2[column].min()}")
		print(f"Max value of *{column}: {df2[column].max()}\n")
		continue

	print(f"Min value of *{column}: {df2[column].min()}")
	print(f"Max value of *{column}: {df2[column].max()}")
	print(f"Mean value of *{column}: {df2[column].mean()}")
	print(f"Standard deviation value of *{column}: {df2[column].std()}\n")

print("--Correlation Matrix--")
df2.columns = ['ts', 'tpu', 'tat', 'tdt', 'avai', 'perf']
matrix = df2.corr().round(2)
print(matrix)
plt.matshow(matrix)
plt.show()

#Alarms
print("---------------------------------------ALARMS-----------------------------------------")
df = pd.read_csv ('alarms_dataset.csv')
print(f"There is {df['alarm_id'].nunique()} unique blocking alarms")

df.drop(df[df['alarm_is_blocking'] == False].index, inplace = True)

print("\n--Ocurrence--")
ocurrence_alarm_id = df['alarm_id'].value_counts(ascending=True)
print (f"{ocurrence_alarm_id}\n")
print("--Percentiles of the total ocurrence alarm_id--")
print(f"{ocurrence_alarm_id.describe()}\n")

quantile_value = ocurrence_alarm_id.quantile(q=0.8)
print(f"80% = {quantile_value}\n Identify alarms above 80%")
df2 = ocurrence_alarm_id.gt(quantile_value)
print(f"{df2}\n")

print("--Top blocking alarms--")
ocurrence_alarm_id.drop(df2[df2 == False].index, inplace = True)
print(ocurrence_alarm_id)

df3 = ocurrence_alarm_id
