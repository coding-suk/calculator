# ch 5.2.1 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculator(self):
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)
