class WeekDayError(Exception):
    pass
	

class Weeker:
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if(day not in Weeker.DAYS):
            raise WeekDayError
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        self.day = Weeker.DAYS[(Weeker.DAYS.index(self.day) + n) % 7]

    def subtract_days(self, n):
        
        self.day = Weeker.DAYS[(Weeker.DAYS.index(self.day) - n) % 7]
        
        


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")


