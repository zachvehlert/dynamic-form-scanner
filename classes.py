# Class: DataObject
# Creates an object with a name (header) and list of keys

class DataObject:
    def __int__(self, name, keys):
        self.name = name
        self.keys = keys


# Class: Form
# img = form in png file format
# data_objects = list of DataObject objects

class Form:

    def __int__(self, img, data_objects):
        self.img = img
        self.data_objects = data_objects

    def find_tables(self):
        # Locate and isolate tables with edge detection
        return

    def find_keys(self):
        # Iterate over the data and search for keys
        # If keys contain multiple words, join them together into a single key object
        return

    def read_vertical_table(self):
        # Associate key value pairs with specific rules for vertical tables
        return

    def read_horizontal_table(self):
        # Associate key value pairs with specific rules for horizontal tables
        return
