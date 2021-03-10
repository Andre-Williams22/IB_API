#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:04:55 2021

@author: andrewilliams
"""

from ibapi.client import EClient
# helps us tanslate data in a way python can understand
from ibapi.wrapper import EWrapper 
from ibapi.contract import Contract 
import threading
import time 

class TradingApp(EWrapper, EClient):
    
    def __init__(self):
        EClient.__init__(self, self)
    
    
    def historicalData(self, reqId, bar):
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)
    
def websocket_connection(): 
    app.run()
        
    
    

app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)

    
con_thread = threading.Thread(target=websocket_connection, daemon=True)
con_thread.start()
time.sleep(1)


contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK" #stock
contract.currency = "USD"
contract.exchange = "SMART"

app.reqHistoricalData(reqId=1,
                      contract=contract, 
                      endDateTime='', # everything up until now
                      durationStr='3 M',
                      barSizeSetting='5 mins',
                      whatToShow='MIDPOINT',
                      useRTH=1,
                      formatDate=1,
                      keepUpToDate=0,
                      chartOptions=[]
                      )	


# app.reqContractDetails(100, contract)
# closes after 5 seconds
time.sleep(5)
