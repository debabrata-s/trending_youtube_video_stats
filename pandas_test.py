import pandas as pd
y=1
n=1
df = pd.read_csv('dataset/INvideos.csv', sep = ',')
print(df)
for d in df.description:
	if ('yes' in str(d)):
		y = y+1;
	elif ('no' in str(d)):
		n = n+1
print("number of yes in description: ",y)
print("number of no in description: ",n)
