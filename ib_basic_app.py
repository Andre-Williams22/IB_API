# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
    
    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {} ".format(reqId, errorCode, errorString))
        
        
    def contractDetails(self, reqId, contractDetails):
        print("redID: {}, contract:{}".format(reqId, contractDetails))
    
        
    
def websocket_connection():
    # creates our connection
    app.run()
        


app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)

    
con_thread = threading.Thread(target=websocket_connection, daemon=True)
con_thread.start()
time.sleep(1)


contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"


app.reqContractDetails(100, contract)
# closes after 5 seconds
time.sleep(5)



         
    
    
    

 