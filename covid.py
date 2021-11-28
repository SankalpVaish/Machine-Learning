import pandas as pd
import matplotlib.pyplot as plt
c=pd.read_csv('covid_19_clean_complete.csv',parse_dates=['Date'])
print(c.dtypes)
c['Active']=c['Confirmed']-c['Deaths']-c['Recovered']
latest=c[c['Date'] == c['Date'].max()]
latest=latest.groupby('Country/Region')['Confirmed','Deaths','Recovered','Active'].sum().sort_values(['Confirmed'],ascending=False).reset_index()
deaths = c.groupby('Date')['Deaths'].sum().reset_index()
active = c.groupby('Date')['Active'].sum().reset_index()
recovered = c.groupby('Date')['Recovered'].sum().reset_index()
confirmed = c.groupby('Date')['Confirmed'].sum().reset_index()
plt.figure(figsize=(15,12))
plt.xticks(rotation=90)
#plt.plot(active['Date'],active['Active'])
#plt.plot(confirmed['Date'],confirmed['Confirmed'],color='red')
#plt.plot(recovered['Date'],recovered['Recovered'],color='green')
#plt.plot(deaths['Date'],deaths['Deaths'],color='brown')
#plt.show()
US = c[c['Country/Region'] == 'US']
US = US.groupby('Date')['Confirmed','Deaths','Recovered','Active'].sum().reset_index()
US.head(10)
russ = c[c['Country/Region'] == 'Russia']
russ = russ.groupby('Date')['Confirmed','Deaths','Recovered','Active'].sum().reset_index()
US.head(10)
chin = c[c['Country/Region'] == 'China']
chin = chin.groupby('Date')['Confirmed','Deaths','Recovered','Active'].sum().reset_index()
US.head(10)
ind = c[c['Country/Region'] == 'India']
ind = ind.groupby('Date')['Confirmed','Deaths','Recovered','Active'].sum().reset_index()
ind.head(10)
ger = c[c['Country/Region'] == 'Germany']
ger = ger.groupby('Date')['Confirmed','Deaths','Recovered','Active'].sum().reset_index()
US.head(10)
plt.plot(US['Date'], US['Confirmed'], c="red",label= 'USA')
plt.plot(ger['Date'], ger['Confirmed'], c="green",label="GERMANY")
plt.plot(ind['Date'], ind['Confirmed'], c="blue",label="INDIA")
plt.plot(chin['Date'], chin['Confirmed'], c="black",label="CHINA")
plt.plot(russ['Date'], russ['Confirmed'], c="brown",label="RUSSIA")
plt.legend()
plt.show()


top_20 = latest.head(20)
#plt.bar(top_20['Country/Region'],top_20['Confirmed'])
#plt.bar(top_20['Country/Region'],top_20['Recovered'],color='green')
#plt.bar(top_20['Country/Region'],top_20['Active'],color='red')
#plt.show()