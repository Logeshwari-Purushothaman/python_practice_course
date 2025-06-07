class vechicle:
    def __init__(self,make,model):
        self.make= make
        self.model = model
        pass

    def moves(self):
        print("This moves...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car =vechicle('Tesla','Model_Y')

my_car.moves()
print(my_car.make)
print(my_car.model)
my_car.get_make_model()

your_car =vechicle('TATA','GO')
your_car.get_make_model()


##OOPS

##Inheritance
##inherited vechicle class
class Airplane(vechicle):

    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print("This flies...")

class Truck(vechicle):
    def moves(self):
        print("This rumbles")

class GolfCart(vechicle):
    pass


cessna =Airplane('Cessna','Skyhawk','N-124')
mack =Truck('Mack','Pinnacle')
golfwagon =GolfCart('Yamaha','GC100')

print("--------------")
print(cessna.faa_id)

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


print("--------------")


##Polymorphism

for v in (my_car,your_car,cessna,mack,golfwagon):
    v.get_make_model()
    v.moves()