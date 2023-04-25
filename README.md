# Box shadow effects in PyQt/PySide
Tested on PySide6 and PyQt6
This repository contains two classes: BoxShadow is a graphical effect in which you need to set a list of shadows and a border width. BoxShadowWrapper - a handy wrapper for displaying the shadow effect.

    BoxShadow(shadow_effects: tiple[dict], border: int = 0, smooth: bool = False).
    BoxShadowWrapper(widget: QtWidgets.QObject, shadow_effects: tiple[dict], border: int = 0, disable_margins: bool = False, margins: tuple[float, float, float, float] | tuple[float, float] = None, smooth: bool = False)

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
 
 # Smooth rendering
 You can choose the type of rendering: anti-aliasing or not. With smooth rendering, borders are rendered clearly without distortion, but more resources are required. For smooth rendering, specify it: smooth=True.
 
 # Smooth example
 <img width="1041" alt="smooth example" src="https://user-images.githubusercontent.com/87101242/209466761-095e04be-e8b5-4362-b593-724e5e7a62fe.png">

 # Example file preview (with smooth)
 <img width="303" alt="light outside" src="https://user-images.githubusercontent.com/87101242/209801809-53667138-1f34-488b-bc7b-0d1ca20ba0c7.png">
 <img width="304" alt="dark inside" src="https://user-images.githubusercontent.com/87101242/209801821-e1e06aa2-6485-46a0-b7a0-a4a42f72a663.png">
