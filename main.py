def convert_hours_to_minutes(hours):
  if not isinstance(hours, (int, float)):
    return "Oops! Hours must be an int or float. 'hours' us a <class 'str'>"
  return 60 * hours

