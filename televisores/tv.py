class TV:
    numTV=0
    def __init__ (self,marca,estado):
        self.marca=marca
        self.estado=estado
        self.canal=1
        self.volumen=1
        self.precio=500
        TV.numTV+=1
    @classmethod
    def getnumTV(cls):
        return cls.numTV
    @classmethod
    def setnumTV(cls,numTV):
        cls.numTV=numTV
    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio=precio
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    def getCanal(self):
        return self.canal
    def setCanal(self,canal):
        if self.estado==True and canal<=120 and canal>=1:
            self.canal=canal
    def getVolumen(self):
        return self.volumen
    def setVolumen(self,volumen):
        if self.estado==True and volumen>=0 and volumen<=7:
            self.volumen=volumen
    def getControl(self):
        return self.control
    def setControl(self,control):
        self.control=control
    def turnOn(self):
        self.estado=True
    def turnOff(self):
        self.estado=False
    def getEstado(self):
        return self.estado
    def canalUp(self,canal):
        if self.estado==True and canal<120:
            volumen+=1
    def canalDown(self,canal):
        if self.estado==True and canal>1:
            volumen-=1
    def volumenUp(self,vol):
        if self.estado==True and vol<7:
            volumen+=1
    def volumenDown(self,vol):
        if self.estado==True and vol>0:
            volumen-=1