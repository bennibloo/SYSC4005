# This class represents the Products that are assembled in the workstations
import time


class Product:
    def __init__(self, id, type):
        self.id = id  # the unique product ID
        self.type = type  # what type of product P1, P2, or P3
        self.time_created = time.clock_gettime(START_INSPECTION)  # get the current time for the clock that started the moment the inspector began to sort

    # Return the Products unique ID
    def get_id(self):
        return self.id

    # Return the tpe of the Product (i.e., P1, P2, or P3)
    def get_type(self):
        return self.type

    # Return the total time it took for the item to be produced.
    def get_created(self):
        return self.time_created

