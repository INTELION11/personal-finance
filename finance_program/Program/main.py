# JQ 2nd Loginout 
import csv  
import hashlib
from helper import sprint, processing, clearr
from Jacob.loginout import regis, login, hash
from Jacob.coding import currency, budgeting, time_frame


username = regis()
budgeting(username,time_frame(username,"mo"))
