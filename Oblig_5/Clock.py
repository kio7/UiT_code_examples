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
            self.sec = 0
            self.inc_minute()
        else:
            self.sec += 1
        
    def inc_minute(self):
        if self.min >= 59:
            self.min = 0
            self.inc_hour()
        else:
            self.min += 1

    def inc_hour(self):
        if self.hour >= 23:
            self.hour = 0
            self.inc_day()
        else:
            self.hour += 1

    def inc_day(self):
        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            if self.day >= 31:
                self.day = 0
                self.inc_month()
            else:
                self.day += 1
        if self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                if self.day >= 29:
                    self.day = 0
                    self.inc_month()
                else:
                    self.day += 1
            else:
                if self.day >= 28:
                    self.day = 0
                    self.inc_month()
                else:
                    self.day += 1

    def inc_month(self):
        if self.month >= 12:
            self.month = 0
            self.inc_year()
        else:
            self.month += 1

    def inc_year(self):
        self.year += 1

    def clock_as_string(self):
        string = f"{self.day:02d}:{self.month:02d}:{self.year}:{self.hour:02d}:{self.min:02d}:{self.sec:02d}"

        return string

    def set_clock(self, day, month, year, hour, min, sec):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        self.sec = sec

if __name__ == "__main__":
    clock = Clock(1,12,2021,2,9,3)

    print(clock.clock_as_string())
