class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        pass
    
    
    def kkkkkk(self):
        pass
        
    def connectSignals(self):
        self.view.btn2.clicked.connect(self.view.clearMessage)
        self.view.btn2()

    def sum(self, a, b): # 예외 처리 기능 추가
        try:
            return str(a+b)
        except:
            return 'Calculation Error'
        
        
    def ks(ls):
        pass