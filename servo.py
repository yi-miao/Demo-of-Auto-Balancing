from robot_hat import pwm, utils

class Servo(pwm.PWM):
    PERIOD = 4095
    CLOCK = 72000000
    FREQ = 50
    MAX_PW = 2500
    MIN_PW = 500
    MAX_AG = 90
    MIN_AG = -90
    def __init__(self, channel):
        super().__init__(channel)
        self.period(self.PERIOD)
        self.prescaler(int(self.CLOCK/self.FREQ/self.PERIOD))

    def angle(self, angle):
        High_level_time = utils.mapping(angle, self.MIN_AG, self.MAX_AG, self.MIN_PW, self.MAX_PW)    # defined in _Basic_class
        value = int(High_level_time*self.PERIOD/20000)
        self.pulse_width(value)

def servo():
    from time import sleep

    s = Servo("P1")
    sleep(0.2)    
    for x in range(-45, 46, 5):
        print(x)
        s.angle(x)    
        sleep(1)
    s.angle(0)    
    sleep(0.2)
    
if __name__ == "__main__":
    servo()
