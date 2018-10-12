##
##      Jackson Pike | If Statments We Face Every day

from datetime import datetime
#Defining Variables
schoolStart = "8:00"
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
    timex = str(current_hour)+":"+ str(current_minutes)+tag
    return timex

##def Wakeup:
##    startMigraine()
##    startBlankCeilingStare(15)
##    getOutOfBed()
##    def timeAvail = (schoolStart-10) - currentTime
##    def timeNeed  = takeShower + brushTeeth + takeMeds + washFace
##    if(timeAvail > timeNeed):
##        takeShower()
##        brushTeeth()
##        takeMeds()
##        washFace()
##        leaveHouse()
##    else:
##        getDressed()
##        gatherSchoolMaterials()
##        leaveHouse()
##
##Wakeup()

        
    
