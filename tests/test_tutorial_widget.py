from Qt import QtCore, QtWidgets

from pyside_tutorial_system.tutorial_widget import TutorialWidget


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    widget = QtWidgets.QWidget()

    widget.show()

    tutorial_dialog = TutorialWidget()
    # tutorial_dialog.show()

    tutorial = [
        {
            "text": (
"""<html><head/><body><p><span style=" font-size:8.25pt;">Headline</span></p><p><span style=" font-size:8.25pt;">Some text</span></p><p><span style=" font-size:8.25pt;">A link: </span><a href="https://de.wikipedia.org/wiki/Reformation#Reaktion_der_katholischen_Kirche"><span style=" font-size:8.25pt; text-decoration: underline; color:#0000ff;">Website</span></a></p></body></html>"""
),
            "widget": widget,
            "alignment": "top",
            "size": [100, 100]
        },
        {
            "text": "#2 - text",
            "widget": widget,
            "alignment": "right",
            "size": [200, 100]
        },
        {
            "text": "#3 - text",
            "widget": widget,
            "alignment": "bottom",
            "size": [100, 200]
        },
        {
            "text": "#4 - text",
            "widget": widget,
            "alignment": "left",
            "size": [200, 200]
        }
    ]


    tutorial_dialog.start(tutorial)

    sys.exit(app.exec_())
