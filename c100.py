class Car(object):
    def __init__(self,model,color,company,speedlimit,typeofcar,milage):
        self.model=model
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
        self.typeofcar=typeofcar
        self.milage=milage

    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")

    def acceleration(self):
        print("the car accelerating")

    def changegear(self,geartype):
        print("gear changed")

audi=Car("A6","red","audi","200","luxury","30")
print(audi.color)
audi.start()
audi.stop()
audi.acceleration()
audi.changegear(4)
