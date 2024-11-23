#!/usr/bin/env python3
"""
Script containing classes as per the test file.
"""
# Standard imports
import math
from datetime import datetime


class Person:
    """
    Class representing a person with first name, last name and birth year.
    """
    def __init__(self, first_name, last_name, birth_year):
        """
        Constructor for the Person class.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._birth_year = birth_year
        self._age = None
        self._base_salary = 50000
        self._bonus = 10
        self._current_year = datetime.now().year

    def set_birth_year(self, birth_year):
        """
        Setter for the birth year of the person.
        """
        self._birth_year = birth_year

    @property
    def current_year(self):
        """
        Read only property to get the current year.
        """
        return self._current_year

    @property
    def age(self):
        """
        Read only property to get the age of the person.
        """
        return self._current_year - self._birth_year

    @property
    def first_name(self):
        """
        Read only property to get the first name of the person.
        """
        return self._first_name

    @property
    def last_name(self):
        """
        Read only property to get the last name of the person.
        """
        return self._last_name

    @property
    def full_name(self):
        """
        Property to get the full name of the person.
        """
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, full_name):
        """
        Setter for the full name of the person.
        """
        self._first_name, self._last_name = full_name.split()

    @property
    def bonus(self):
        """
        Property to get the bonus of the person.
        """
        return self._bonus
    
    @bonus.setter
    def bonus(self, bonus):
        """
        Setter for the bonus of the person.
        """
        if bonus < 0 or bonus > 100:
            raise ValueError("Bonus must be between 0 and 100")
        self._bonus = bonus

    @property
    def base_salary(self):
        """
        Read only property to get the base salary of the person.
        """
        return self._base_salary

    @base_salary.setter
    def base_salary(self, base_salary):
        """
        Setter for the base salary of the person.
        """
        self._base_salary = base_salary

    @property
    def salary(self):
        """
        Read only property to get the salary of the person.
        """
        return self._base_salary + (self._base_salary * (self._bonus/100.0))


class Circle:
    """
    Class representing a circle with a radius.
    """
    def __init__(self, radius):
        """
        Constructor for the Circle class.
        """
        self._radius = radius
        self._cached_area = {}

    @property
    def radius(self):
        """
        Property to get the radius of the circle.
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Setter for the radius of the circle.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    @property
    def diameter(self):
        """
        Read only property to get the diameter of the circle.
        """
        return self._radius * 2

    @property
    def area(self):
        """
        Read only property to get the area of the circle.
        """
        if self._radius in self._cached_area:
            return self._cached_area[self._radius]
        area = math.pi * (self._radius ** 2)
        self._cached_area[self._radius] = area
        return area


class Vehicle:
    """
    Class representing a vehicle with a make, model and year.
    """
    vehicle_count = 0

    def __init__(self, make, model, year):
        """
        Constructor for the Vehicle class.
        """
        Vehicle.vehicle_count += 1
        self._make = make
        self._model = model
        self._year = year

    @classmethod
    def get_vehicle_count(cls):
        """
        Class method to get the number of vehicles.
        """
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(vehicle_type):
        """
        Static method to classify the vehicle type.
        """
        return f"This is a {vehicle_type}"


class ElectricVehicle(Vehicle):
    """
    Class representing an electric vehicle with a make, model and year.
    """
    def __init__(self, make, model, year):
        """
        Constructor for the ElectricVehicle class.
        """
        super().__init__(make, model, year)

    @staticmethod
    def classify_vehicle(vehicle_type):
        """
        Class method to classify the vehicle type.
        """
        return f"This is an electric {vehicle_type}"


class DynamicClass:
    """
    Class representing a dynamic class with dynamic attribute creation.
    """
    static_value = 10

    def __init__(self, **kwargs):
        """
        Constructor for the DynamicClass class.
        Allows dynamic creation of attributes through keyword arguments.
        
        Args:
            **kwargs: Arbitrary keyword arguments that will be set as attributes
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dynamic_attr(self, attr_name, value):
        """
        Dynamically creates a new attribute with the given name and value.
        
        Args:
            attr_name: Name of the attribute to create
            value: Value to assign to the attribute
        """
        setattr(self, attr_name, value)

    def __getattr__(self, attr_name):
        """
        Called when an attribute lookup fails. Returns the value from _data
        if it exists, otherwise raises AttributeError.
        """
        if attr_name in self.__dict__:
            return self._data[attr_name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")


class ValidatedAttribute:
    """
    Class that can work both as a descriptor and as a standalone class for validating positive numbers.
    """
    def __init__(self):
        """
        Constructor for the ValidatedAttribute class/descriptor.
        """
        self.name = None
        self._value = None

    def __set_name__(self, owner, name):
        """
        Called when the descriptor is assigned to a class attribute.
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Getter method - works both as descriptor and property
        """
        if instance is None:
            return self
        # If used as descriptor
        if self.name is not None:
            return instance.__dict__.get(self.name)
        # If used as standalone
        return self._value

    def __set__(self, instance, value):
        """
        Setter method - works both as descriptor and property
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value <= 0:
            raise ValueError("Value must be positive")
        # If used as descriptor
        if self.name is not None:
            instance.__dict__[self.name] = int(value)
        # If used as standalone
        else:
            self._value = int(value)

    @property
    def value(self):
        """
        Property to access the value when used as standalone
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Property setter to set the value when used as standalone
        """
        self.__set__(None, value)
