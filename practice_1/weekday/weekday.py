
weekdays = [
  'Saturday',
  'Sunday',
  'Monday',
  'Tuesday',
  'Wendsday',
  'Thursday',
  'Friday'
]

def get_weekday(index = 0):
  if index < 0 or index > 6: return 'Invalid index'
  return weekdays[index]
