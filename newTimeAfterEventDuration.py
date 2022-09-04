hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
newMins = (mins + dura)%60
newHour = (hour+(mins+dura)//60)%24

print(newHour,":",newMins)