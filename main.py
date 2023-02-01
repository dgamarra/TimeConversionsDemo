def convertirHorasAMinutos(hours):
  if not isinstance(hours, (int, float)):
    return "Oops! Las horas deben ser int o float. 'horas' como una <class 'str'>"
  return 60 * hours

print(convertirHorasAMinutos(30))