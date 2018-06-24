"""Guide a user through an interactive tutorial of another widget."""
from functools import partial

from Qt import QtCore, QtWidgets


class TutorialWidget(QtWidgets.QWidget):
    """Show sections of tutorial at positions relative to a parent widget."""

    def __init__(self, parent=None):
        """Initialize the widget."""
        super(TutorialWidget, self).__init__()
        self.setWindowFlags(QtCore.Qt.Widget |
                            QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textedit = QtWidgets.QTextEdit(self)
        self.textedit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textedit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textedit.setReadOnly(True)
        self.textedit.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textedit.setObjectName("textedit")
        self.verticalLayout_2.addWidget(self.textedit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setMaximumSize(QtCore.QSize(24, 24))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.page_label = QtWidgets.QLabel(self)
        self.page_label.setObjectName("page_label")
        self.horizontalLayout.addWidget(self.page_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.previous_button = QtWidgets.QPushButton(self)
        self.previous_button.setMinimumSize(QtCore.QSize(24, 24))
        self.previous_button.setMaximumSize(QtCore.QSize(24, 24))
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setMinimumSize(QtCore.QSize(24, 24))
        self.next_button.setMaximumSize(QtCore.QSize(24, 24))
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.close_button.setText(u"X")
        self.page_label.setText("Page 1/4")
        self.previous_button.setText(u"\u25C0")
        self.next_button.setText(u"\u25B6")

        # Connect Signals
        #
        self.close_button.clicked.connect(self.close)
        self.next_button.clicked.connect(partial(self._show_tutorial, 1))
        self.previous_button.clicked.connect(partial(self._show_tutorial, -1))

    def start(self, tutorial):
        """Initialize the widget with the given tutorial data."""
        self.tutorial = tutorial
        self.index = 0
        self.show()
        self._show_tutorial(0)

    def _show_tutorial(self, direction):
        """Show the next section of the tutorial or close if last."""
        # Clear up the current section
        #
        self._reset_widget()

        # Move to the next section
        #
        self.index += direction
        if self.index < len(self.tutorial):
            widget = self.tutorial[self.index]["widget"]
            alignment = self.tutorial[self.index]["alignment"]

            self.tutorial[self.index]["style_sheet"] = widget.styleSheet()

            widget.setStyleSheet("background-color: rgba(255, 100, 100, 100);")

            geo = self.geometry()
            w = self.tutorial[self.index]["size"][0]
            h = self.tutorial[self.index]["size"][1]
            self.setGeometry(geo.x(), geo.y(), w, h)

            parent_widget = widget.parentWidget()
            if parent_widget:
                pos = parent_widget.mapToGlobal(widget.pos())
            else:
                pos = widget.pos()

            x = pos.x()
            if alignment == "right":
                x += widget.geometry().width()
            elif alignment == "left":
                x -= self.geometry().width()
            y = pos.y()
            if alignment == "top":
                y -= self.geometry().height()
            elif alignment == "bottom":
                y += widget.geometry().height()
            geo = self.geometry()
            w = self.tutorial[self.index]["size"][0]
            h = self.tutorial[self.index]["size"][1]
            self.setGeometry(x, y, w, h)

            self.textedit.setHtml(self.tutorial[self.index]["text"])

            self.page_label.setText("{0}/{1}".format(self.index + 1,
                                                     len(self.tutorial)))

            if self.index + 1 == len(self.tutorial):
                self.next_button.hide()
            else:
                self.next_button.show()

            if self.index == 0:
                self.previous_button.hide()
            else:
                self.previous_button.show()

        else:
            self.close()

    def closeEvent(self, event):
        """@todo documentation for onClose."""
        self._reset_widget()
        event.accept()

    def _reset_widget(self):
        """@todo documentation for _reset_widget."""
        if self.index < len(self.tutorial):
            widget = self.tutorial[self.index]["widget"]
            style_sheet = self.tutorial[self.index].get("style_sheet", "")
            widget.setStyleSheet(style_sheet)
