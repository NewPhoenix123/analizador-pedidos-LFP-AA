from flask import Flask, render_template, request

from analyzer.lexer import analizar_lexico
from analyzer.parser import analizar_sintaxis
from analyzer.automatas import AUTOMATAS

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    tokens = []
    sintaxis_correcta = None
    codigo = ""

    if request.method == 'POST':

        codigo = request.form.get('codigo')

        archivo = request.files.get('archivo')

        if archivo and archivo.filename.endswith('.txt'):

            contenido = archivo.read().decode('utf-8')

            if contenido.strip():
                codigo = contenido

        tokens = analizar_lexico(codigo)

        sintaxis_correcta = analizar_sintaxis(codigo)

    return render_template(
        'index.html',
        tokens=tokens,
        sintaxis_correcta=sintaxis_correcta,
        automatas=AUTOMATAS,
        codigo=codigo
    )


if __name__ == '__main__':
    app.run(debug=True)
