months = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}
days = {
     "1":"01",
     "2":"02",
     "3":"03",
     "4":"04",
     "5":"05",
     "6":"06",
     "7":"07",
     "8":"08",
     "9":"09",
}
should_loop = True
while should_loop:
        
        user_input = input("Date: ").title()

        try:
            if "," in user_input:
                month,day,year= user_input.split()
                if "," in day: # removes comma
                    day = day.replace(",", "")
                else: 
                    continue
                if month in months:
                    month = months[month]
                else:
                     continue
            
            if "/" in user_input:
                user_input = user_input.replace(" ", "")
                month,day,year = user_input.split("/")                           
            if day in days:
                day = days[day]
            if month in days:
                month = days[month]
            if int(month) > 12:
                continue
            if int(day) > 31 or int(day) < 1:
                 continue
            print(f"{year}-{month}-{day}")
            should_loop = False
        except:
            pass
