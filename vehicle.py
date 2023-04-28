
from abc import ABC, abstractmethod

# abstractmethod - A decorator indicating abstract methods.

# Requires that the metaclass is ABCMeta or derived from it. 
# A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods are overridden. 
# The abstract methods can be called using any of the normal 'super' call mechanisms. 
# abstractmethod() may be used to declare abstract methods for properties and descriptors.

# ABC - Helper class that provides a standard way to create an ABC using inheritance.

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass