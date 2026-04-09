# JQ 2nd Loginout 
import csv  
import hashlib
from helper import sprint, processing, clearr
from Jacob.loginout import regis, login, hash
from Jacob.coding import currency, budgeting, time_frame
#from Arsh.gui import *


username = "kenya"
while True:
    budgeting(username,time_frame(username,"mo"))


"""loop = True
while loop == True:
    option = input("Do you wan to login or logout?").strip().lower()
    if option == "logout":"""