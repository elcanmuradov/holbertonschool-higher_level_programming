#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish classes.
It explores method resolution order (MRO) in Python's multiple inheritance system.
"""


class Fish:
    """A Fish class representing aquatic animals."""
    
    def swim(self):
        """Method for swimming behavior."""
        print("The fish is swimming")
    
    def habitat(self):
        """Method describing the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A Bird class representing flying animals."""
    
    def fly(self):
        """Method for flying behavior."""
        print("The bird is flying")
    
    def habitat(self):
        """Method describing the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish class that demonstrates multiple inheritance.
    
    This class inherits from both Fish and Bird, showcasing how Python
    handles multiple inheritance and method resolution order (MRO).
    """
    
    def fly(self):
        """Override the fly method with flying fish specific behavior."""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Override the swim method with flying fish specific behavior."""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """Override the habitat method with flying fish specific behavior."""
        print("The flying fish lives both in water and the sky!")


# Demonstration of Method Resolution Order (MRO)
if __name__ == "__main__":
    print("Method Resolution Order (MRO) for FlyingFish:")
    print(FlyingFish.mro())
    print("\nAlternatively, using __mro__ attribute:")
    print(FlyingFish.__mro__)
    
    print("\n" + "="*50)
    print("Testing FlyingFish methods:")
    print("="*50)
    
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    
    print("\n" + "="*50)
    print("Testing inheritance - calling parent methods:")
    print("="*50)
    
    # Demonstrating that FlyingFish has access to both parent classes
    print("isinstance(flying_fish, Fish):", isinstance(flying_fish, Fish))
    print("isinstance(flying_fish, Bird):", isinstance(flying_fish, Bird))
    print("isinstance(flying_fish, FlyingFish):", isinstance(flying_fish, FlyingFish))