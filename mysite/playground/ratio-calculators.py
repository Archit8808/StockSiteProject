from pyparsing import col
pd.options.display.float_format = '{:.2f}'.format  #changing number output from scientific notation to floating point

stock_list = {} 
for idx,ticker in enumerate(sp500list) : 
    stock_list[ticker] = Stock(ticker)



def vertical_analyzer(stock : Stock , visualize = False) : 
    dI = stock.income_statement.dfI
    dIbyrev = dI.dropna().apply(lambda p : (p / p['totalRevenue']))  
    dIbyrevout = dIbyrev.to_string(formatters={
    '2018': '{:,.2%}'.format,
    '2019': '{:,.2%}'.format,
    '2020': '{:,.2%}'.format,
    '2021': '{:,.2%}'.format,
})
    if visualize == True : 
        iterable = dIbyrev.shape[0]
        for i in range(0,iterable):
            plt.plot(dIbyrev.iloc[i,:].index , 
                dIbyrev.iloc[i,:])
            plt.title(dIbyrev.iloc[i].name)
            plt.show()
   
    
        
 

def horizontal_analyzer(stock:Stock,visualize = False) : 
    dB = stock.balance_sheet.dfBT 
    dB.dropna() 
    print(dB.pct_change())
    dBt = dB.pct_change().transpose()
    if visualize == True : 
        iterable = dBt.shape[0]
        for i in range(0,iterable):
            plt.plot(dBt.iloc[i,:].index , 
                dBt.iloc[i,:])
            plt.title(dBt.iloc[i].name)
            plt.show()

        
def liquidity_ratios(stock : Stock,visualize = False) : 
    dB = stock.balance_sheet.dfBT
    print(dB.transpose())
    print(dB.totalCurrentAssets)
    print(dB.inventory)
    dBquickratio = dB.totalCurrentAssets.dropna().apply(lambda p : (p - dB.inventory) / dB.totalCurrentLiabilities)
    dBcurrentratio = dB.totalCurrentAssets.dropna().apply(lambda p : (p) / dB.totalCurrentLiabilities)
    #dBcashratio 
    print(dBquickratio) 
    print(dBcurrentratio)
 
   
def leverage_ratios(stock : Stock,visualize = False) : 
    dB = stock.balance_sheet.dfBT
    print(dB.transpose())
 
    dBdebtequityratio = dB.totalCurrentLiabilities.dropna().apply(lambda p : (p) / dB.totalStockholderEquity) 
    dBdebtcapitalratio = dB.totalCurrentLiabilities.dropna().apply(lambda p : (p+ dB.totalLiabilities/total))
    print(dBdebtequityratio)
    

horizontal_analyzer(Stock('AAPL'),visualize=True)
      
    
    




    

    




    
                    
        
