AUTOMATAS = {

    "NUMERO": {

        "regex": "[0-9]+",

        "quintupla": """
        Q = {q0, q1, q2}
        Σ = {0,1,2,3,4,5,6,7,8,9}
        δ = función de transición
        q0 = estado inicial
        F = {q2}
        """,

        "afnd": """
        q0 --0--> q1
        q0 --1--> q1
        q0 --2--> q1
        ...
        q0 --9--> q1

        q1 --ε--> q2

        q2 --0..9--> q2
        """,

        "afnd_mermaid": """
        graph LR
        inicio((Inicio)) --> q0

        q0 -->|0| q1
        q0 -->|1| q1
        q0 -->|2| q1
        q0 -->|3| q1
        q0 -->|4| q1
        q0 -->|5| q1
        q0 -->|6| q1
        q0 -->|7| q1
        q0 -->|8| q1
        q0 -->|9| q1

        q1 -->|ε| q2((Final))
        """,

        "afd": """
        q0 --0..9--> q1
        q1 --0..9--> q1
        """,

        "afd_mermaid": """
        graph LR
        inicio((Inicio)) --> q0

        q0 -->|0,1,2,3,4,5,6,7,8,9| q1((Final))
        """,

                "tabla": """
        Estado | 0-9
        q0     | q1
        q1     | q1
        """
    },

    "IDENTIFICADOR": {

    "regex": "[a-zA-Z][a-zA-Z0-9_]*",

    "quintupla": """
    Q = {q0, q1, q2}
    Σ = {a-z, A-Z, 0-9, _}
    δ = función de transición
    q0 = estado inicial
    F = {q2}
    """,

    "afnd": """
    q0 --a-z,A-Z--> q1

    q1 --ε--> q2

    q2 --a-z,A-Z--> q2
    q2 --0-9--> q2
    q2 --_--> q2
    """,

    "afnd_mermaid": """
    graph LR
    inicio((Inicio)) --> q0

    q0 -->|a-z,A-Z| q1

    q1 -->|ε| q2((Final))

    q2 -->|a-z,A-Z| q2
    q2 -->|0-9| q2
    q2 -->|_| q2
    """,

    "afd": """
    q0 --a-z,A-Z--> q1

    q1 --a-z,A-Z,0-9,_--> q1
    """,

    "afd_mermaid": """
    graph LR
    inicio((Inicio)) --> q0

    q0 -->|a-z,A-Z| q1((Final))

    q1 -->|a-z,A-Z,0-9,_| q1
    """,

        "tabla": """
    Estado | letra | digito | _
    q0     | q1    | -      | -
    q1     | q1    | q1     | q1
    """
    },

    "KW_REGLA": {

    "regex": "REGLA",

    "quintupla": """
    Q = {q0, q1, q2, q3, q4, q5, q6}
    Σ = {R, E, G, L, A}
    δ = función de transición
    q0 = estado inicial
    F = {q6}
    """,

    "afnd": """
    q0 --R--> q1
    q1 --E--> q2
    q2 --G--> q3
    q3 --L--> q4
    q4 --A--> q5

    q5 --ε--> q6
    """,

    "afnd_mermaid": """
    graph LR
    inicio((Inicio)) --> q0

    q0 -->|R| q1
    q1 -->|E| q2
    q2 -->|G| q3
    q3 -->|L| q4
    q4 -->|A| q5

    q5 -->|ε| q6((Final))
    """,

    "afd": """
    q0 --R--> q1
    q1 --E--> q2
    q2 --G--> q3
    q3 --L--> q4
    q4 --A--> q5
    """,

    "afd_mermaid": """
    graph LR
    inicio((Inicio)) --> q0

    q0 -->|R| q1
    q1 -->|E| q2
    q2 -->|G| q3
    q3 -->|L| q4
    q4 -->|A| q5((Final))
    """,

    "tabla": """
    Estado | R | E | G | L | A
    q0     | q1| - | - | - | -
    q1     | - | q2| - | - | -
    q2     | - | - | q3| - | -
    q3     | - | - | - | q4| -
    q4     | - | - | - | - | q5
    """
    }

}