class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, min=0, sec=0):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        self.sec = sec
    
    def inc_second(self):
        if self.sec >= 59:
            self.inc_minute()
            self.sec = 0
        else:
            self.sec += 1
        
    def inc_minute(self):
        if self.min >= 59:
            self.inc_hour()
            self.min = 0
        else:
            self.min += 1

    def inc_hour(self):
        if self.hour >= 23:
            self.inc_day()
            self.hour = 0
        else:
            self.hour += 1

    def inc_day(self):
        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            if self.day >= 31:
                self.inc_month()
                self.day = 1
            else:
                self.day += 1
        elif self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                if self.day >= 29:
                    self.inc_month()
                    self.day = 1
                else:
                    self.day += 1
            else:
                if self.day >= 28:
                    self.inc_month()
                    self.day = 1
                else:
                    self.day += 1
        else:
            self.day += 1
    def inc_month(self):
        if self.month >= 12:
            self.inc_year()
            self.month = 1
        else:
            self.month += 1

    def inc_year(self):
        self.year += 1

    def clock_as_string(self):
        string = f"{self.day:02d}:{self.month:02d}:{self.year:04d}:{self.hour:02d}:{self.min:02d}:{self.sec:02d}"

        return string

    def set_clock(self, day, month, year, hour, min, sec):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        self.sec = sec
