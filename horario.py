#Para el horario, dos comidas al día

from datetime import datetime
horarios_comida = [("08:00", "mañana"), ("20:00", "noche")]

def hora_comida():
  ahora = datetime.now().strftime("%H:%M")
  return any(hora == ahora for hora, _ in horarios_comida)