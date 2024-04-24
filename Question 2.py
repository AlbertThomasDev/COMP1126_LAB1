def barstool(num):
  if num%3 == 0 and num%7 == 0 :
    return "BarStool"
  elif num%3 == 0:
    return "Bar"
  elif num%7 == 0:
    return "Stool"
  return "No Bar No Stool"
