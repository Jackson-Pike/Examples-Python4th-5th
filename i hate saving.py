##Imports
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime

def current_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    current_hour = current_hour - 6


    if current_hour >= 12:
        tag="PM"
       
    else:
        tag="AM"

    if current_hour > 12:
        current_hour-=12
        print(current_hour)
    if current_minutes < 10:
        timex = str(current_hour)+":0"+str(current_minutes)
    timex = str(current_hour)+":"+str(current_minutes)
    return timex
print(current_time())
