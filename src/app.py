from RiemannSum import RiemannSum
from sympy import parse_expr
from PySimpleGUI import PySimpleGUI as gui

gui.theme("Reddit")
layout = [
  [gui.Text("Informe o valor de a: "), gui.Input(key="min", size=(10, 1))],
  [gui.Text("Informe o valor de b: "), gui.Input(key="max", size=(10, 1))],
  [gui.Text("Informe o número de intervalos: "), gui.Input(key="n", size=(10, 1))],
  [gui.Text("Informe o f(x): "),gui.Input(key="fx", size=(20, 1))],
  [gui.Button("Calcular")],
]

window = gui.Window("Soma de Reimann", layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    if event == "Calcular":
        try:
            min_value = float(values["min"])
            max_value = float(values["max"])
            n = int(values["n"])
            exp = parse_expr(values["fx"])

            riemannSum = RiemannSum(min_value, max_value, n, exp)

            gui.popup("Soma de Riemann à esquerda: " + str(riemannSum.resultLeft()),
                     "Soma de Riemann à direita: " + str(riemannSum.resultRight()),
                     "O resultado da integral definida é: " + str(riemannSum.resultIntegral()))

        except Exception as e:
            gui.popup("Erro: Certifique-se de que os valores estão corretos.")
            
window.close()