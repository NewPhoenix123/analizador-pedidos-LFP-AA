import re

def analizar_lexico(codigo):

    patron_general = r'''
    REGLA|
    WHEN|
    THEN|
    AND|
    OR|
    APROBAR|
    RECHAZAR|
    DESCUENTO|
    PRIORIDAD|
    >=|
    <=|
    >|
    <|
    =|
    [0-9]+|
    [a-zA-Z][a-zA-Z0-9_]*|
    ;
    '''

    lexemas = re.findall(
        patron_general,
        codigo,
        re.VERBOSE
    )

    resultado = []

    for lexema in lexemas:

        if lexema == "REGLA":
            token = "KW_REGLA"

        elif lexema == "WHEN":
            token = "KW_WHEN"

        elif lexema == "THEN":
            token = "KW_THEN"

        elif lexema == "AND":
            token = "KW_AND"

        elif lexema == "OR":
            token = "KW_OR"

        elif lexema == "APROBAR":
            token = "KW_APROBAR"

        elif lexema == "RECHAZAR":
            token = "KW_RECHAZAR"

        elif lexema == "DESCUENTO":
            token = "KW_DESCUENTO"

        elif lexema == "PRIORIDAD":
            token = "KW_PRIORIDAD"

        elif lexema == ">":
            token = "OP_MAYOR"

        elif lexema == "<":
            token = "OP_MENOR"

        elif lexema == ">=":
            token = "OP_MAYOR_IGUAL"

        elif lexema == "<=":
            token = "OP_MENOR_IGUAL"

        elif lexema == "=":
            token = "OP_IGUAL"

        elif lexema == ";":
            token = "FIN_REGLA"

        elif re.fullmatch(r"[0-9]+", lexema):
            token = "NUMERO"

        elif lexema == "cantidad":
            token = "ATR_CANTIDAD"

        elif lexema == "stock":
            token = "ATR_STOCK"

        elif lexema == "compras":
            token = "ATR_COMPRAS"

        elif lexema == "producto":
            token = "ATR_PRODUCTO"
        elif re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]*", lexema):
            token = "IDENTIFICADOR"

        else:
            token = "DESCONOCIDO"

        resultado.append({
            "lexema": lexema,
            "token": token
        })

    return resultado