from PySide6 import QtCore, QtWidgets, QtGui
from Neumorphism.Neumorphism import *

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        light_outside = [{"outside": True, "offset": [6, 6], "blur": 8, "color": QtGui.QColor(111, 140, 176, 105)},
                   {"outside": True, "offset": [-6, -6], "blur": 8, "color": "#FFFFFF"}]
        light_inside = [{"inside": True, "offset": [6, 6], "blur": 8, "color": "#C1D5EE"},
                  {"inside": True, "offset": [-6, -6], "blur": 8, "color": "#FFFFFF"}]
        dark_outside = [{"outside": True, "offset": [6, 6], "blur": 8, "color": QtGui.QColor(0, 0, 0, 178)},
                   {"outside": True, "offset": [-6, -6], "blur": 8, "color": QtGui.QColor(58, 58, 58, 255)}]
        dark_inside = [{"inside": True, "offset": [6, 6], "blur": 8, "color": QtGui.QColor(0, 0, 0, 178)},
                  {"inside": True, "offset": [-6, -6], "blur": 8, "color": QtGui.QColor(58, 58, 58, 255)}]

        light_style = "QObject{background: #E3EDF7; border: none; border-radius: 5px; color: #979797;} QPushButton{ border-radius: 15px; border: 1px solid white; width: 50px; height: 30px}"
        dark_style = "QObject{background: #232428; border: none; border-radius: 5px; color: rgb(4, 236, 180);} QPushButton{ border-radius: 15px; border: 1px solid #1A1A1A;; width: 50px; height: 30px}"

        # set outside and inside shadow and style
        self.outside = dark_outside
        self.inside = dark_inside
        self.setStyleSheet(dark_style)

        self.resize(300, 250)
        display = QtWidgets.QLCDNumber(10)
        display.setFixedHeight(70)
        display.display(1234567890)

        calc_grid = QtWidgets.QGridLayout()
        calc_grid.setSpacing(0)

        btn_plus = QtWidgets.QPushButton("+")
        btn_plus.pressed.connect(self.button_pressed)
        btn_plus.released.connect(self.button_released)

        btn_minus = QtWidgets.QPushButton("-")
        btn_minus.pressed.connect(self.button_pressed)
        btn_minus.released.connect(self.button_released)

        btn_multiply = QtWidgets.QPushButton("*")
        btn_multiply.pressed.connect(self.button_pressed)
        btn_multiply.released.connect(self.button_released)

        btn_deliver = QtWidgets.QPushButton("÷")
        btn_deliver.pressed.connect(self.button_pressed)
        btn_deliver.released.connect(self.button_released)

        btn_percent = QtWidgets.QPushButton("%")
        btn_percent.pressed.connect(self.button_pressed)
        btn_percent.released.connect(self.button_released)

        btn_clear = QtWidgets.QPushButton("AC")
        btn_clear.pressed.connect(self.button_pressed)
        btn_clear.released.connect(self.button_released)

        btn_plus_minus = QtWidgets.QPushButton("+/-")
        btn_plus_minus.pressed.connect(self.button_pressed)
        btn_plus_minus.released.connect(self.button_released)

        btn_decimals = QtWidgets.QPushButton(",")
        btn_decimals.pressed.connect(self.button_pressed)
        btn_decimals.released.connect(self.button_released)

        btn_result = QtWidgets.QPushButton("=")
        btn_result.pressed.connect(self.button_pressed)
        btn_result.released.connect(self.button_released)

        calc_grid.addWidget(BoxShadowWrapper(display, self.outside, disable_margins=True), 0, 0, 1, 4)
        calc_grid.addWidget(BoxShadowWrapper(btn_result, self.outside, border=1, disable_margins=True), 5, 3)

        calc_grid.addWidget(BoxShadowWrapper(btn_clear, self.outside, border=1, disable_margins=True), 1, 0)
        calc_grid.addWidget(BoxShadowWrapper(btn_percent, self.outside, border=1, disable_margins=True), 1, 1)
        calc_grid.addWidget(BoxShadowWrapper(btn_plus_minus, self.outside, border=1, disable_margins=True), 1, 2)
        calc_grid.addWidget(BoxShadowWrapper(btn_plus, self.outside, border=1, disable_margins=True), 1, 3)
        calc_grid.addWidget(BoxShadowWrapper(btn_minus, self.outside, border=1, disable_margins=True), 2, 3)
        calc_grid.addWidget(BoxShadowWrapper(btn_multiply, self.outside, border=1, disable_margins=True), 3, 3)
        calc_grid.addWidget(BoxShadowWrapper(btn_deliver, self.outside, border=1, disable_margins=True), 4, 3)
        calc_grid.addWidget(BoxShadowWrapper(btn_decimals, self.outside, border=1, disable_margins=True), 5, 2)

        buttons = [QtWidgets.QPushButton("0")]
        # buttons[0].setObjectName("0")
        buttons[0].pressed.connect(self.button_pressed)
        buttons[0].released.connect(self.button_released)
        calc_grid.addWidget(BoxShadowWrapper(buttons[0], self.outside, border=1, disable_margins=True), 5, 0, 1, 2)

        x, y = 2, 0
        for i in range(1, 10):
            buttons.append(QtWidgets.QPushButton(f"{i}"))
            # buttons[-1].setObjectName(f"i")
            buttons[-1].pressed.connect(self.button_pressed)
            buttons[-1].released.connect(self.button_released)
            calc_grid.addWidget(BoxShadowWrapper(buttons[-1], self.outside, border=1, disable_margins=True), x, y)

            y += 1
            if y == 3:
                x += 1
                y = 0
        self.setLayout(calc_grid)
        self.show()

    def button_pressed(self):
        self.sender().parent().setShadowList(self.inside)
        self.sender().update()

    def button_released(self):
        self.sender().parent().setShadowList(self.outside)
        self.sender().update()



app = QtWidgets.QApplication([])
app.setStyle("Fusion")
w = Calculator()
app.exec()
