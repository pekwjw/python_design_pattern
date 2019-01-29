# -*- coding:utf-8 -*-
# author: pekwjw
# date: 2019-01-29

class Button(object):
    def __init__(self,shape = 'circle'):
        self.button_shape = shape

    def create(self):
        pass

    def usage(self):
        pass

class circle(Button):
    def __init__(self,shape):
        Button.__init__(self,shape)
        print "Button shape is: {0}.".format(self.button_shape)

    def usage(self):
        print "Draw one {0}.".format(self.button_shape)

class rhombus(Button):
    def __init__(self,shape):
        super(rhombus,self).__init__(shape)
        print "Button shape is: {0}.".format(self.button_shape)

    def usage(self):
        print "Draw one {0}.".format(self.button_shape)

class rectangle(Button):
    def __init__(self,shape):
        super(rectangle,self).__init__(shape)
        print "Button shape is: {0}.".format(self.button_shape)

    def usage(self):
        print "Draw one {0}.".format(self.button_shape)

class ButtonFactory(object):
    def __init__(self):
        pass

    def create_instance(self):
        pass

class circle_factory(ButtonFactory):
    def create_instance(self):
        ins = circle("circle")
        return ins

class rhombus_factory(ButtonFactory):
    def create_instance(self):
        ins = rhombus("rhombus")
        return ins

class rectangle_factory(ButtonFactory):
    def create_instance(self):
        ins = rectangle("rectangle")
        return ins

def test_client():
    cir = circle_factory().create_instance()
    cir.usage()

    rho = rhombus_factory().create_instance()
    rho.usage()

    rec = rectangle_factory().create_instance()
    rec.usage()

    del cir,rho,rec

def main():
    test_client()

if __name__ == "__main__":
    main()
