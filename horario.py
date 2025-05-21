from datetime import datetime, timedelta

horarios_comida = [("08:00", "mañana"), ("13:26", "noche")]

def hora_comida(margen_minutos=5):
    ahora = datetime.now()
    for hora_str, _ in horarios_comida:
        hora_obj = datetime.strptime(hora_str, "%H:%M").replace(
            year=ahora.year, month=ahora.month, day=ahora.day
        )
        diferencia = abs((ahora - hora_obj).total_seconds() / 60)
        if diferencia <= margen_minutos:
            return True
    return True
