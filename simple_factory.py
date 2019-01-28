# -*- coding:utf-8 -*-
# author: pekwjw
# date: 2019-01-28

class Car(object):
    def __init__(self,car_name = "suv"):
        self.name = car_name

    def create(self):
        print "create one {0}.".format(str(self.name))

class tank(Car):
    def __init__(self,car_name):
        Car.__init__(self,car_name)

    def create(self):
        print "Create one {0}".format(str(self.name))

    def wheel(self):
        print "{0}'s wheel is made of caterpillar.".format(str(self.name))

class suv(Car):
    def __init__(self,car_name):
        #Car.__init__(self,car_name)
        super(suv,self).__init__(car_name)

    def create(self):
        print "Create one {0}".format(str(self.name))

    def usage(self):
        print "{0} is used for cross_country.".format(str(self.name))

class bus(Car):
    def __init__(self,car_name):
        Car.__init__(self,car_name)

    def usage(self):
        print "{0} is used for transportation in big cities.".format(str(self.name))

def car_factory(car_name):
    if "tank" == car_name:
        car_instance = tank(car_name)
        return car_instance
    elif "suv" == car_name:
        car_instance = suv(car_name)
        return car_instance
    elif "bus" == car_name:
        car_instance = bus(car_name)
        return car_instance
    else:
        return None

def test_client():
    t = car_factory("tank")
    s = car_factory("suv")
    b = car_factory("bus")

    t.create()
    t.wheel()

    s.create()
    s.usage()

    b.create()
    b.usage()

    del t,s,b

def main():
    test_client()

if __name__ == "__main__":
    main()
