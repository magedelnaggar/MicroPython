"""
Stepper Motor Control Library

This library provides an interface to control a stepper motor using GPIO pins.
It allows users to set the direction and number of steps with adjustable speed.

Author: ChatGPT
"""

from machine import Pin
from time import sleep

class StepperMotor:
    """
    A class to control a stepper motor using GPIO pins.
    """
    def __init__(self, step_pin: int, dir_pin: int):
        """
        Initializes the stepper motor with given GPIO pins.

        :param step_pin: GPIO pin connected to the step signal.
        :param dir_pin: GPIO pin connected to the direction signal.
        """
        self.step_pin = Pin(step_pin, Pin.OUT)
        self.dir_pin = Pin(dir_pin, Pin.OUT)

    def rotate(self, steps: int, direction: bool, delay: float = 0.001):
        """
        Rotates the stepper motor a specific number of steps in the given direction.

        :param steps: Number of steps to move.
        :param direction: True for clockwise (CW), False for counterclockwise (CCW).
        :param delay: Time delay between steps (default: 1ms), controls speed.
        """
        self.dir_pin.value(direction)  # Set direction
        for _ in range(steps):
            self.step_pin.value(1)
            sleep(delay)
            self.step_pin.value(0)
            sleep(delay)