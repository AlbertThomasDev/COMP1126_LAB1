def majorSportYear(year):
  if year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0:
    return "Olympics, Copa America and European Championship"
  elif year%4 == 2:
    return "Men’s FIFA World Cup"
  elif year%4 == 3:
    return "ICC Cricket World Cup, FIFA Women’s World Cup and Netball World Cup" #" and also ""IAAF World Athletic Championships and Gold Cup" 
  return "IAAF World Athletic Championships and Gold Cup"
  
