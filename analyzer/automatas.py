AUTOMATAS = {

    "CLIENTE": {

        "regex": "C[0-9]{3}",

        "quintupla": """
            Q = {q0, q1, q2, q3, q4}
            Σ = {C, 0-9}
            q0 = q0
            F = {q4}
        """,

        "afnd": """
            q0 --C--> q1
            q1 --0-9--> q2
            q2 --0-9--> q3
            q3 --0-9--> q4
        """,

        "afnd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|C| q1
            q1 -->|0-9| q2
            q2 -->|0-9| q3
            q3 -->|0-9| q4((Final))
        """,

        "afd": """
            q0 --C--> q1
            q1 --0-9--> q2
            q2 --0-9--> q3
            q3 --0-9--> q4
        """,

        "afd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|C| q1
            q1 -->|0-9| q2
            q2 -->|0-9| q3
            q3 -->|0-9| q4((Final))
        """,

        "tabla": """
            Estado | C | 0-9

            q0     | q1 | -
            q1     | -  | q2
            q2     | -  | q3
            q3     | -  | q4
        """
    },

    "PRODUCTO": {

        "regex": "P[0-9]{3}",

        "quintupla": """
            Q = {q0, q1, q2, q3, q4}
            Σ = {P, 0-9}
            q0 = q0
            F = {q4}
        """,

        "afnd": """
            q0 --P--> q1
            q1 --0-9--> q2
            q2 --0-9--> q3
            q3 --0-9--> q4
        """,

        "afnd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|P| q1
            q1 -->|0-9| q2
            q2 -->|0-9| q3
            q3 -->|0-9| q4((Final))
        """,


        "afd": """
            q0 --P--> q1
            q1 --0-9--> q2
            q2 --0-9--> q3
            q3 --0-9--> q4
        """,

        "afd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|P| q1
            q1 -->|0-9| q2
            q2 -->|0-9| q3
            q3 -->|0-9| q4((Final))
        """,

        "tabla": """
            Estado | P | 0-9
            
            q0     | q1 | -
            q1     | -  | q2
            q2     | -  | q3
            q3     | -  | q4
        """
    },

    "NUMERO": {

        "regex": "[0-9]+",

        "quintupla": """
            Q = {q0, q1}
            Σ = {0-9}
            q0 = q0
            F = {q1}
        """,

        "afnd": """
            q0 --0-9--> q1
            q1 --0-9--> q1
        """,

        "afnd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|0-9| q1((Final))
            q1 -->|0-9| q1
        """,

        "afd": """
            q0 --0-9--> q1
            q1 --0-9--> q1
        """,

        "afd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|0-9| q1((Final))
            q1 -->|0-9| q1
        """,

        "tabla": """
            Estado | 0-9
            q0     | q1
            q1     | q1
        """
    },

    "METODO_PAGO": {

        "regex": "EFECTIVO|TRANSFERENCIA|TARJETA",

        "quintupla": """
            Q = {q0,q1}
            Σ = {EFECTIVO,TRANSFERENCIA,TARJETA}
            q0 = q0
            F = {q1}
        """,

        "afnd": """
            q0 --> EFECTIVO --> q1
            q0 --> TRANSFERENCIA --> q1
            q0 --> TARJETA --> q1
        """,

        "afnd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|EFECTIVO| q1((Final))
            q0 -->|TRANSFERENCIA| q1
            q0 -->|TARJETA| q1
        """,

        "afd": """
            q0 --> EFECTIVO --> q1
            q0 --> TRANSFERENCIA --> q1
            q0 --> TARJETA --> q1
        """,

        "afd_mermaid": """
            graph LR
            inicio((Inicio)) --> q0
            q0 -->|EFECTIVO| q1((Final))
            q0 -->|TRANSFERENCIA| q1
            q0 -->|TARJETA| q1
        """,

        "tabla": """
        Estado | EFECTIVO | TRANSFERENCIA | TARJETA
        q0     | q1 | q1 | q1
        """
    }

}