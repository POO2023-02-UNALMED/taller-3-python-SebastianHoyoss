class Control:
    def enlazar(self,tv):
        self.tv=tv
        tv.setControl(self)
    def getTv(self):
        return self.tv
    def setTv(self,tv):
        self.tv=tv
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()
    def setCanal(self, can:int):
        self.tv.setCanal(can)
    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    def setVolumen(self, vol:int):
        self.tv.setVolumen(vol)
    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()
