class Time:
  def __init__(self,hour=0,minute=0,second=0):
    self._hour=hour #private menbers
    self.minute=minute #private members
    self.second=second #private members
  def__add__(self,other):
    total_seconds=self._hour*3600+self._minute*60+self.second+\other._hour*3600+other._minute*60+other._second
    new_hour,remainder=divmod(total_seconds,3600)
    new_minute, new_second = divmod(remainder, 60)
    return Time(new_hour, new_minute, new_second)
  def __str__(self):
    return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"
    
print("Time 1")
hour=int(input("enter the hour:"))    
minute=int(input("enter the minute:"))
second=int(input("enter the second:"))
t1=Time(hour,minute,second)
print("Time 2")
hour=int(input("enter the hour:"))
minute=int(input("enter the minute:"))
second=int(input("enter the second:"))

