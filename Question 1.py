from datetime import date

def time_existed ():
  current_date = date.today()
  print("Todays date is: ", current_date)

  name = input("What is your name: ")
  y = int(input("Enter your year of birth: "))
  m = int(input("Enter the month of birth: "))
  d = int(input("Enter your day of birth: "))
  # print(type(d))
  dob = date(y,m,d)
  # print(dob)
  days = (current_date - dob).days
  #print(days)
  print(name, "has lived for",days )


time_existed()
