import re

def analizar_sintaxis(codigo):

    patron = r'''
    ^REGLA\s+
    [a-zA-Z][a-zA-Z0-9_]*\s+
    WHEN\s+
    (cantidad|stock|compras|producto)\s*
    (>|<|>=|<=|=)\s*
    ([0-9]+|[a-zA-Z][a-zA-Z0-9_]*)\s+
    THEN\s+
    (
        DESCUENTO\s*=\s*[0-9]+
        |
        PRIORIDAD\s*=\s*[a-zA-Z][a-zA-Z0-9_]*
        |
        APROBAR
        |
        RECHAZAR
    )
    ;
    $
    '''

    return bool(
        re.match(
            patron,
            codigo.strip(),
            re.VERBOSE
        )
    )