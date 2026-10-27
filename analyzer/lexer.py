import re


def analizar_lexico(codigo):

    patron_general = r'''
    PEDIDO|
    cliente|
    producto|
    cantidad|
    pago|
    C[0-9]{3}|
    P[0-9]{3}|
    EFECTIVO|TRANSFERENCIA|TARJETA|
    [0-9]+|
    \(|\)|=|,|;
    '''

    lexemas = re.findall(
        patron_general,
        codigo,
        re.VERBOSE
    )

    resultado = []

    for lexema in lexemas:

        if lexema == "PEDIDO":
            token = "KW_PEDIDO"

        elif lexema == "cliente":
            token = "KW_CLIENTE"

        elif lexema == "producto":
            token = "KW_PRODUCTO"

        elif lexema == "cantidad":
            token = "KW_CANTIDAD"

        elif lexema == "pago":
            token = "KW_PAGO"

        elif re.fullmatch(r"C[0-9]{3}", lexema):
            token = "CLIENTE"

        elif re.fullmatch(r"P[0-9]{3}", lexema):
            token = "PRODUCTO"

        elif lexema in ["EFECTIVO", "TRANSFERENCIA", "TARJETA"]:
            token = "METODO_PAGO"

        elif re.fullmatch(r"[0-9]+", lexema):
            token = "NUMERO"

        elif lexema == "(":
            token = "PAREN_ABRE"

        elif lexema == ")":
            token = "PAREN_CIERRA"

        elif lexema == "=":
            token = "IGUAL"

        elif lexema == ",":
            token = "COMA"

        elif lexema == ";":
            token = "PUNTO_COMA"

        else:
            token = "DESCONOCIDO"

        resultado.append({
            "lexema": lexema,
            "token": token
        })

    return resultado