from datetime import datetime
import time

class timemanager():
    """Klasi sem heldur utan um tíma fyrir keylogger"""
    def __init__(self):
        self.lastPressTime = time.time()#Tíminn þegar síðast var ýtt á takka

    def getTimeStamp(self):
        """Skilar tímastimpli sem streng"""
        return str(datetime.now())
    
    def checkTime(self):
        """Skilar True ef meira en 10 sekúndur eru liðnar síðan síðast var ýtt á takka"""
        curr = time.time()
        if curr >= self.lastPressTime + 10:
            self.lastPressTime = curr
            return True
        else:
            self.lastPressTime = curr
            return False