from django.db import models
import ast
import pandas as pd
ticker = 'AAPL'

with open ('Static/stockdata/balancesheet_sp500.txt','r') as input:
        balancesheet = ast.literal_eval(input.read())
with open ('Static/stockdata/incomestatement_sp500.txt' , 'r' ) as input : 
        incomestatement = ast.literal_eval(input.read()) 
with open('Static/stockdata/cashflowstatement_sp500.txt' , 'r' ) as input: 
        cashflowstatement = ast.literal_eval(input.read())

    

  



class Services(models.Model) : 
    title = models.CharField(max_length=120) 
    description = models.TextField(blank = True , null = True) 
    price = models.DecimalField(decimal_places=2,max_digits=10000,default = 0)


faulty = set()




class BalanceSheets(models.Model):
    def __init__(self, ticker,*args, **kwargs):
        self.ticker = ticker
        self.source = balancesheet
        self.yearlydict = {'2018': {}, '2019': {}, '2020': {}, '2021': {}}

        try : 
            for yearlystatements in self.source[self.ticker] : 
                for year,statements in yearlystatements.items() : 
                    for year1 in self.yearlydict.keys() : 
                        if year[0:4] == year1 : 
                            self.yearlydict[year1] = statements
        except : 
            faulty.add(self.ticker)
        

        self.dfB = pd.DataFrame(self.yearlydict)
        self.dfBT = self.dfB.transpose() 
     
        

class IncomeStatements(models.Model):
    def __init__(self, ticker,*args, **kwargs):
        self.ticker = ticker 
        self.source = incomestatement
        self.yearlydict = {'2018': {}, '2019': {}, '2020': {}, '2021': {}}
        try : 
            for yearlystatements in self.source[self.ticker] : 
                for year,statements in yearlystatements.items() : 
                    for year1 in self.yearlydict.keys() : 
                        if year[0:4] == year1 : 
                            self.yearlydict[year1] = statements
        except : 
            faulty.add(self.ticker)
        self.dfI = pd.DataFrame(self.yearlydict)
        self.dfIT = self.dfI.transpose() 
        super(*args, **kwargs)


class CashflowStatements(models.Model):
    def __init__(self,ticker , *args, **kwargs):
        self.ticker = ticker 
        self.source = cashflowstatement
        self.yearlydict = {'2018': {}, '2019': {}, '2020': {}, '2021': {}}
        try : 
            for yearlystatements in self.source[self.ticker] : 
                for year,statements in yearlystatements.items() : 
                    for year1 in self.yearlydict.keys() : 
                        if year[0:4] == year1 : 
                            self.yearlydict[year1] = statements
        except : 
            faulty.add(self.ticker)
        self.dfC = pd.DataFrame(self.yearlydict)
        self.dfCT = self.dfC.transpose() 
        
        super(*args, **kwargs)


class Stock(models.Model): 
    
    
    def __init__(self, ticker, freq='Annual'):
        
        self.ticker = ticker
        self.balance_sheet = BalanceSheets(self.ticker)
        self.income_statement = IncomeStatements(self.ticker)
        self.cashflow_statement = CashflowStatements(self.ticker) 

    


# Create your models here
