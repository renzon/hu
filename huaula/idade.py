from datetime import datetime


def minutos_desde_nascimento(ano, mes, dia, hora=0, minutos=0, segundos=1):
    nascimento = datetime(ano, mes, dia, hora, minutos, segundos)
    agora = get_agora()
    delta = agora - nascimento

    return round(delta.total_seconds())


# essa funcao está aqui só para ser mocada
def get_agora():
    return datetime.now()
