# Neumorphism-effects-in-PyQt-PySide
This repository contains two classes: BoxShadow is a graphical effect in which you need to set a list of shadows and a border width. BoxShadow Wrapper - a handy wrapper for displaying the shadow effect.

    BoxShadow(shadow_effects: tiple[dict], border: int = 0).
    BoxShadowWrapper(widget: QtWidgets.QObject, hadow_effects: tiple[dict], border: int = 0, disable_margins: bool = False, margins: tuple[float, float, float, float] | tuple[float, float] = None)

The shadow is set as follows:
 
    {"outside": True, "offset": [6, 6], "blur": 8, "color": QtGui.QColor(111, 140, 176, 105)}
    {"inside": True, "offset": [-6, -6], "blur": 8, "color": "#FFFFFF"}
   
 NOTE: If you are using a border and inner shadows, then you must specify the width of the border. This is necessary so that the shadow is not drawn on the border.
 
 By default, BoxShadowWrapper sets margins based on the distance needed to display the entire shadow. If you want to disable setting margins and use standard ones, then specify disable _margins = true. if you want to change the margins, then specify your margins in the following format:

    margins= [X, Y] or [left, top, right, bottom]
   
 You can change the shadows in the BoxShadow Wrapper at runtime using the setShadowList function. This can be useful for buttons or switches:

    btn = QtWidgets.QPushButton("im button:)
    outside = [{"outside": True, "offset": [6, 6], "blur": 8, "color": QtGui.QColor(0, 0, 0, 178)},
                   {"outside": True, "offset": [-6, -6], "blur": 8, "color": QtGui.QColor(58, 58, 58, 255)}]
    inside = [{"inside": True, "offset": [6, 6], "blur": 8, "color": QtGui.QColor(0, 0, 0, 178)},
                  {"inside": True, "offset": [-6, -6], "blur": 8, "color": QtGui.QColor(58, 58, 58, 255)}]
    BoxShadowWrapper(btn, outside, disable_margins=True)
    btn.pressed.connect(lambda: btn.parent().setShadowList(inside) or btn.update())
    btn.released.connect(lambda: btn.parent().setShadowList(outside) or btn.update())
  
  # Example file preview
  ![neumorphism light normal](https://g-leo.fun/media/portfolio_4/neumorphism_light_normal.png)
  ![neumorphism dark pressed](https://g-leo.fun/media/portfolio_4/neumorphism_dark_pressed.png)
