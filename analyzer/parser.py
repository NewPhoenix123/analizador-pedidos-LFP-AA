import re


def analizar_sintaxis(codigo):

    patron = r'^PEDIDO\(cliente=C[0-9]{3}, producto=P[0-9]{3}, cantidad=[0-9]+, pago=(EFECTIVO|TRANSFERENCIA|TARJETA)\);$'

    if re.match(patron, codigo.strip()):
        return True

    return False