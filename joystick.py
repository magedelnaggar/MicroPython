import machine
import time

class Joystick:
    def __init__(self, vertical_pin, horizontal_pin, button_pin, mode="polling"):
        self.v_pin = machine.ADC(machine.Pin(vertical_pin))
        self.h_pin = machine.ADC(machine.Pin(horizontal_pin))
        self.button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        
        self.v_pin.atten(machine.ADC.ATTN_11DB)  # Set attenuation for wider range
        self.h_pin.atten(machine.ADC.ATTN_11DB)

        self.mode = mode
        self.last_state = {'V': 0, 'H': 0}
        
        if self.mode == "interrupt":
            self.timer = machine.Timer(-1)
            self.timer.init(period=100, mode=machine.Timer.PERIODIC, callback=self._read_callback)

    def _read_callback(self, timer):
        self.last_state['V'] = self.v_pin.read()
        self.last_state['H'] = self.h_pin.read()

    def read(self):
        if self.mode == "polling":
            vertical = self.v_pin.read()
            horizontal = self.h_pin.read()
        else:
            vertical = self.last_state['V']
            horizontal = self.last_state['H']

        button_pressed = not self.button.value()

        direction = "M"  # Default to Middle
        if vertical < 2000:
            direction = "D"
        elif vertical > 2096:
            direction = "U"
        elif horizontal < 2000:
            direction = "R"
        elif horizontal > 2096:
            direction = "L"

        return direction, button_pressed