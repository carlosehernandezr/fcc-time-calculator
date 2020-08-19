DAYS_OF_WEEK=["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
HOUR_ABBS= ["am","pm"]

def add_time(start, duration,day=""):

  day = day.lower()

  start_items = start.split(" ")
  start_time_items = start_items[0].split(":")

  startHours= int(start_time_items[0])
  startMinute = int(start_time_items[1])
  abb = start_items[1]

  duration_items = duration.split(":")
  durationHours = int(duration_items[0])
  durationMinute = int(duration_items[1])

  newHour =startHours + durationHours
  newMinute = startMinute + durationMinute

  daysLater = int(round(newHour/12)/2)

  if int(round(newHour/12))==1 and abb=="PM":
    daysLater+=1

  abb = getAbb(newHour,abb)
      
  newHour = round(((newHour/12)-int(newHour/12))*12)

  if newMinute/60>=1.0:
    newHour+= int(round(newMinute/60))
    newMinute = int(round(((newMinute/60)-int((newMinute/60)))*60))
    abb = getAbb(newHour,abb)
    if abb=="AM":
      daysLater+= int(round(newHour/12))

  hour = str(newHour) + ":" + formatNum(str(newMinute)) +" "+ abb

  if daysLater==0 and len(day)>0:
    hour+=", " + getDay(day,daysLater)
  elif daysLater > 1 and len(day)>0:
    hour+=", " + getDay(day,daysLater) + " ("+str(daysLater)+" days later)"
  elif daysLater > 1 and len(day)==0:
    hour+= " ("+str(daysLater)+" days later)"
  elif daysLater == 1 and len(day)>0:
     hour+=", " + getDay(day,daysLater) + " (next day)"
  elif daysLater==1:
    hour+=" (next day)"


  return hour

def isPar(num):
  if num%2==0:
    return True

  return False

def formatNum(num):
  if len(num)==1:
    return "0"+num

  return num

def getDay(day,daysLater):

  aux = int(daysLater + DAYS_OF_WEEK.index(day))
  
  if aux > 7:
    aux= aux-7*(int(aux/7))

  return str(DAYS_OF_WEEK[aux]).capitalize()

def isValidDay(day):
  try:
    if DAYS_OF_WEEK.index(day)>-1:
      return True
  except:
    return False

def getAbb(hour,abb):
  if not isPar(int(hour/12)):
    if abb == "AM":
      abb = "PM" 
    else:
      abb="AM"
  return abb