from flask import Flask, render_template

app = Flask(__name__)

# Diccionario anidado que representa el menú de navegación
menu = {
    "Inicio": {},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Ing. Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Electrónica": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Industrial": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Posgrado": {}
    },
    "Contacto": {}
}

@app.route("/")
def inicio():
    return render_template("menu.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)

