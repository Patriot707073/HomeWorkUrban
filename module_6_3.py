import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed <0:
            print ("It's too deep, i can't dive :(" )
        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print (f"X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]})

    def attack (self):
        if self._DEGREE_OF_DANGER <5:
            print ("Sorry, i'm peaceful :)")
        else:
            print ("Be careful, i'm attacking you 0_0" )

class Bird (Animal):
    beak = True

    def lay_eggs(self):
        rand_int = random.randint(1,4)
        print (f"Here are(is) <случайное число от 1 до 4> eggs for you")

class AquaticAnimal (Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):












