class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        print('Getting', self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('Setting', self.name)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('Deleting', self.name)


class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
