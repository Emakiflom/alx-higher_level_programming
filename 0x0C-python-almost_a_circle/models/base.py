#!/usr/bin/python3
"""
module base importing json
"""
import json
import os.path
import csv


class Base:
    """
    module base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor method init
        """
        if(id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        conversion to json-- j
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save --- class file
        """
        tmp_list = []
        if list_objs is not None:
            for item in list_objs:
                tmp_list.append(item.to_dictionary())

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            file.write(cls.to_json_string(tmp_list))

    @staticmethod
    def from_json_string(json_string):
        """
        from json to string-- static method
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        """
        if cls.__name__ == "Rectangle":
            txt = cls(1, 1)
        elif cls.__name__ == "Square":
            txt = cls(1)
        cls.update(txt, **dictionary)
        return txt

    @classmethod
    def load_from_file(cls):
        """
        class to create a rectangle object-- class method
        """
        new_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, "r") as read_file:
                new_list = cls.from_json_string(read_file.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        else:
            pass
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to file--- class method
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            text = ["width", "height", "x", "y", "id"]
        elif cls.__name__ == "Square":
            text = ["size", "x", "y", "id"]

        with open(filename, 'w') as file:
            saver = csv.DictWriter(file, fieldnames=text)
            if list_objs is not None:
                saver.writeheader()
                for text1 in list_objs:
                    saver.writerow(text1.to_dictionary())
            else:
                saver.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        new_list = []
        if os.path.exists(filename):
            with open(filename, newline="") as csvFile:
                read = csv.DictReader(csvFile)
                for row in read:
                    for k, v in row.items():
                        row[k] = int(v)
                    new_list.append(row)
            return [cls.create(**oj) for oj in new_list]
        else:
            return [[]]
