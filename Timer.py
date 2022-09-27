class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return "%02d:%02d:%02d" %(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        self.__seconds += 1
        self.__formatTime()

    def prev_second(self):
        self.__seconds -= 1
        self.__formatTime()
    
    def __formatTime(self):
        if(self.__seconds > 59):          #if seconds reaches 60, increments minutes and sets seconds to 0
            self.__minutes += 1
            self.__seconds = 0
            if(self.__minutes > 59):      #if minutes reaches 60, increments hours and sets minutes to 0
                self.__hours += 1
                self.__minutes = 0 
                if(self.__hours > 23):         #if hours reaches 24, sets everything hours to 0
                    self.__hours = 0
        
        if(self.__seconds < 0):            #if seconds is less than 0, decrements minutes and sets seconds to 0
            self.__minutes -= 1
            self.__seconds = 0
            if(self.__minutes < 0):        #if minutes is less than 0, decrements hours and sets minutes to 0
                self.__hours -= 1
                self.__minutes = 0
                if(self.__hours < 0):
                    self.__hours, self.__minutes, self.__seconds = 23, 59, 59  #reverts back to the last second of the previous day

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
