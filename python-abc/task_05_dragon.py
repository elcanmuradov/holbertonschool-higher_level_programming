#!/usr/bin/env python3
"""
This module demonstrates the use of mixins to compose behaviors in classes.
Mixins provide focused, single-purpose functionality that can be combined
to create classes with multiple capabilities.
"""


class SwimMixin:
    """
    A mixin class that provides swimming functionality.
    
    This mixin is designed to be combined with other classes to add
    swimming behavior without creating complex inheritance hierarchies.
    """
    
    def swim(self):
        """Method that provides swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying functionality.
    
    This mixin is designed to be combined with other classes to add
    flying behavior without creating complex inheritance hierarchies.
    """
    
    def fly(self):
        """Method that provides flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that demonstrates mixin composition.
    
    This class inherits from both SwimMixin and FlyMixin, gaining
    both swimming and flying capabilities through mixin composition.
    It also adds its own dragon-specific behavior.
    """
    
    def roar(self):
        """Dragon-specific method for roaring behavior."""
        print("The dragon roars!")
    
    def __init__(self):
        """
        Initialize a Dragon instance.
        
        This constructor can be used to set up dragon-specific attributes
        if needed in the future.
        """
        pass


# Demonstration of mixin functionality and method resolution order
if __name__ == "__main__":
    print("Dragon Mixin Demonstration")
    print("=" * 30)
    
    # Create a dragon instance
    dragon = Dragon()
    
    # Demonstrate inherited behaviors from mixins
    print("Testing inherited behaviors:")
    dragon.swim()  # From SwimMixin
    dragon.fly()   # From FlyMixin
    dragon.roar()  # Dragon's own method
    
    print("\n" + "=" * 30)
    print("Method Resolution Order (MRO):")
    print(Dragon.mro())
    
    print("\n" + "=" * 30)
    print("Instance checks:")
    print(f"isinstance(dragon, Dragon): {isinstance(dragon, Dragon)}")
    print(f"isinstance(dragon, SwimMixin): {isinstance(dragon, SwimMixin)}")
    print(f"isinstance(dragon, FlyMixin): {isinstance(dragon, FlyMixin)}")
    
    print("\n" + "=" * 30)
    print("Available methods:")
    methods = [method for method in dir(dragon) 
               if not method.startswith('_') and callable(getattr(dragon, method))]
    for method in methods:
        print(f"  - {method}")