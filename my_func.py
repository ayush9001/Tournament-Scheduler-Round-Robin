class Date():
    def __init__(self,date_list):
        self.year = date_list[0]
        self.month = date_list[1]
        self.day = date_list[2]
        self.firstdate = date_list
    
    def get_date(self):
        return [self.year,self.month,self.day]

    def resetDate(self):
        self.year = self.firstDate[0]
        self.month = self.firstDate[1]
        self.day = self.firstDate[2]
    
    def inc_day(self):
        daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
        if self.year % 4 == 0:
            daysInMonths[1] += 1

        self.day += 1
        if self.day > daysInMonths[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1


class Time():
    def __init__(self,hours,minutes,period=None):
        self.hours = hours
        self.minutes= minutes
        self.period = period.upper()
        if self.period == 'AM':
            if self.hours == 12:
                self.hours = 0
        elif self.period == 'PM':
            if self.hours < 12:
                self.hours += 12

    def getTimeString(self):
        m = str(self.minutes)
        if len(m)==1:
            m = '0'+m
            
        if self.hours < 12:
            #AM
            if self.hours == 0:
                h = '12'
            else:
                h = str(self.hours)
                if len(h)==1:
                    h = '0'+h
            ts = h+':'+m+' AM'
        else:
            #PM
            if self.hours > 12:
                h = str(self.hours -12)
                if len(h)==1:
                    h = '0'+h
            else:
                h = '12'
            ts = h+':'+m+' PM'
            
        return ts
        
        

#Subtract two dates
def subtractDates(date1,date2):
    from datetime import datetime
    d1, d2 = date1.get_date(), date2.get_date()
    d1 = datetime(d1[0],d1[1],d1[2],0,0,0)
    d2 = datetime(d2[0],d2[1],d2[2],0,0,0)
    if d1 > d2:
        diff = d1 - d2
    else:
        diff = d2 - d1
    return diff.days
    



#Get day of week from time tuple
def get_dayOfWeek(date):
    datelist = date.get_date()
    time_tuple = (datelist[0],datelist[1],datelist[2],0,0,0,0,)
    from _datetime import datetime as dt
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    return days[dt(*time_tuple).isocalendar()[2] - 1]
