# Python Classes

This project demonstrates various Python class implementations with different features and their corresponding test cases.

## Classes Overview

### Person
A class representing a person with the following features:
- First name and last name management
- Age calculation based on birth year
- Salary calculation with base salary and bonus
- Property decorators for controlled attribute access

### Circle
A class representing a geometric circle with:
- Radius and diameter calculations
- Area calculation with caching mechanism
- Input validation for radius
- Property decorators for controlled access

### Vehicle and ElectricVehicle
A base and derived class demonstration:
- Vehicle count tracking using class variables
- Static method for vehicle classification
- Inheritance example with ElectricVehicle
- Method overriding demonstration

### DynamicClass
A class showing dynamic attribute handling:
- Dynamic attribute creation at runtime
- Custom attribute access control
- Flexible initialization with kwargs

### ValidatedAttribute
A descriptor class demonstrating:
- Attribute validation
- Dual usage as descriptor and standalone class
- Type and value validation for numeric inputs

## Test Cases

The test suite (`test_classes.py`) includes comprehensive tests for all classes:

### Person Tests
- Age calculation verification
- Name management
- Salary calculation with bonus

### Circle Tests
- Radius and diameter calculations
- Area computation verification
- Validation for negative radius

### Vehicle Tests
- Vehicle count tracking
- Vehicle classification
- Electric vehicle inheritance

### DynamicClass Tests
- Dynamic attribute creation
- Attribute access

### ValidatedAttribute Tests
- Value validation
- Error handling for invalid inputs
