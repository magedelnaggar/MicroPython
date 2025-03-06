from machine import PWM, Pin

class Servo:
    def __init__(self, pin, min_duty=40, max_duty=115):
        self.servo = PWM(Pin(pin), freq=50)
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.current_angle = 90
        self.goto(90)  # Start at the middle position

    def angle_to_duty(self, angle):
        return self.min_duty + (self.max_duty - self.min_duty) * angle / 180

    def goto(self, angle):
        self.current_angle = max(0, min(180, angle))
        duty = int(self.angle_to_duty(self.current_angle))
        self.servo.duty(duty)

    def left(self, angle):
        self.goto(self.current_angle - angle)

    def right(self, angle):
        self.goto(self.current_angle + angle)
