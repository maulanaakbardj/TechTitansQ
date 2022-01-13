import pandas as pd
data = pd.read_csv('pricing.txt', sep=",")
a1=data['Unit'][0]*data['Price'][0]
a2=data['Unit'][2]*data['Price'][2]
a3=data['Unit'][4]*data['Price'][4]
a4=data['Unit'][8]*data['Price'][8]
data['Currency'][0]='IDR, '+ str(a1)
data['Currency'][2]='IDR, '+ str(a2)
data['Currency'][4]='IDR, '+ str(a3)
data['Currency'][8]='IDR, '+ str(a4)
b1=data['Unit'][1]*data['Price'][1]*19000
b2=data['Unit'][5]*data['Price'][5]*19000
data['Currency'][1]='EUR, '+ str(b1)
data['Currency'][5]='EUR, '+ str(b2)
c1=data['Unit'][3]*data['Price'][3]*1400
c2=data['Unit'][6]*data['Price'][6]*1400
c3=data['Unit'][7]*data['Price'][7]*1400
c4=data['Unit'][9]*data['Price'][9]*1400
data['Currency'][3]='USD, '+ str(c1)
data['Currency'][6]='USD, '+ str(c2)
data['Currency'][7]='USD, '+ str(c3)
data['Currency'][9]='USD, '+ str(c4)
data.to_csv(r'converted.txt', sep=',')
