""" How Does a single man change an entire country"""
#side note stop laughing when you see anyone it werid
import OPi.GPIO as GPIO
import time
class Motor_Control(object):
    """docstring for Motor_Control."""
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(12,GPIO.OUT)
        self.LeftPin = 1
        self.RightPin = 0
    def Forward(self):
        GPIO.setup(self.LeftPin, GPIO.OUT)
        GPIO.setup(self.RightPin, GPIO.OUT)

    def Left(self):
        GPIO.setup(self.LeftPin, GPIO.OUT)

    def Right(self):
        GPIO.setup(self.RightPin, GPIO.OUT)


    def Clean(self):
        GPIO.cleanup()

if __name__ == '__main__':
    m = Motor_Control()
    x = 0
    while x < 10:
        m.Forward()
        x = x + 1
