from RiemannSum import RiemannSum
from sympy import parse_expr
from PySimpleGUI import PySimpleGUI as gui

gui.theme("DarkGrey5")
layout = [
  [gui.Text("Informe o valor de a: ", size=(15, 1), justification="right"), gui.Input(key="min", size=(20, 1))],
  [gui.Text("Informe o valor de b: ", size=(15, 1), justification="right"), gui.Input(key="max", size=(20, 1))],
  [gui.Text("Número de intervalos: ", size=(15, 1), justification="right"), gui.Input(key="n", size=(20, 1))],
  [gui.Text("Informe o f(x): ", size=(15, 1), justification="right"),gui.Input(key="fx", size=(20, 1))],
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