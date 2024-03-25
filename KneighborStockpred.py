import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

    
def model(stock_tick, new_data): # where stock tick is the csv file for data
    stock_data = pd.read_csv('C:\\Users\\rflem\\OneDrive\\Desktop\\Website Stock bettor\\Data for stock price\\'+stock_tick+'.csv')
    cols = stock_data.columns
    sample_data = stock_data[cols[1:4]]
    sample_data = np.array(sample_data)
    target_data = stock_data['Adj Close']
    target_data = np.array(target_data)
    dataset = {'Samples': sample_data, 'targets': target_data}

    X_train, X_test, y_train, y_test = train_test_split(dataset['Samples'],dataset['targets'], random_state= 0)
    reg = KNeighborsRegressor(n_neighbors= 3)
    reg.fit(X_train, y_train)
    new_data = np.array(new_data)
    new_data = new_data.reshape(1,-1)

    prediction = reg.predict(new_data)

    return prediction 

print('AAPL',model('AAPL',[162.44,165,162.13]))
print('MSFT',model('MSFT',[287.73,288.81,283.03]))
print('AMZN',model('AMZN',[102.16,103.42,101.95]))
print('TSLA',model('TSLA',[197.53,207.79,197.23]))
print('GOOGL',model('GOOGL',[101.3,103.89,101.05]))
print('GOOG',model('GOOG',[101.71,104.19,101.44]))
print('NVDA',model('NVDA',[271.4,278.34,271.05]))
print('BRKB',model('BRKB.VI',[305.9,308.81,304.99]))
print('META',model('META',[207.24,212.17,206.77]))
print('UNH',model('UNH',[485.55,486.29,461.08]))




    
