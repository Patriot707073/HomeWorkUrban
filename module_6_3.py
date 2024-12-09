import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self, dx,dy,dz):
        factor_dz = dz * self.speed
        if factor_dz <0:
            print ("It's too deep, i can't dive :(" )

        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed

    def get_cords (self):
        print (f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack (self):
        if self._DEGREE_OF_DANGER <5:
            print ("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >=5:
            print ("Be careful, i'm attacking you 0_0" )

    def speak (self):
        if self.sound is not None:
            print (self.sound)

class Bird (Animal):
    beak = True

    def lay_eggs(self):
        rand_int = random.randint(1,4)
        print  (f"Here are(is) {rand_int} eggs for you")

class AquaticAnimal (Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        new_dz = self._cords[2] - dz * (self.speed / 2)
        if new_dz < 0:
            self._cords[2] = 0
        else:
            self._cords[2] = new_dz

class PoisonousAnimal:
    _DEGREE_OF_DANGER = 8

class Duckbill (PoisonousAnimal, AquaticAnimal, Bird ):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()








