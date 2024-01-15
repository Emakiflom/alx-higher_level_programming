#!/usr/bin/python3
"""
module square of rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    module square of rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor methos of rectangle
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """
        getter gets the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter sets the size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        str string
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.width))

    def update(self, *args, **kwargs):
        """
        update method -- self arg
        """
        if args:
            tmp_list = ["id", "size", "x", "y"]
            for v in range(len(args)):
                setattr(self, tmp_list[v], args[v])
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        square to dictionary
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.height}
