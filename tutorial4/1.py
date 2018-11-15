class Parent:
    def __init__(self, id):
        self.__id = id

class Child(Parent):
    def __init__(self, id, attribute):
        super().__init__(id)
        self.__own_attribute = attribute

