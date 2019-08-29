#encoding: utf-8
import RPi.GPIO as GPIO
import time



def A1():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

def get_GPIO():
    pin=[16,20,21,26,19,13,11,9]
    GPIO.setup(pin,GPIO.OUT)

def one():
    one=[9,13]
    clean()
    GPIO.output(one,True)


def two():
    two=[11,9,20,21,19]
    clean()
    GPIO.output(two,True)
    
    
def three():
    three=[11,9,20,13,19]
    clean()
    GPIO.output(three,True)

def four():
    four=[26,20,9,13]
    clean()
    GPIO.output(four,True)
    
def five():
    five=[11,26,20,13,19]
    clean()
    GPIO.output(five,True)
    
def six():
    six[11,26,20,21,19,13]
    clean()
    GPIO.output(six,True)

def seven():
    seven=[11,9,13]
    clean()
    GPIO.output(seven,True)
    
def eight():
    eight=[20,21,26,19,13,11,9]
    clean()
    GPIO.output(eight,True)
    
def nine():
    nine=[11,9,20,26,13,19]
    clean()
    GPIO.output(nine,True)
    
def clean():
    pin=[16,20,21,26,19,13,11,9]
    GPIO.output(pin,False)
 
    
def text():

    GPIO.output(16,True)
    time.sleep(1)
    GPIO.output(20,True)
    time.sleep(1)
    GPIO.output(21,True)
    time.sleep(1)
    GPIO.output(26,True)
    time.sleep(1)
    GPIO.output(19,True)
    time.sleep(1) 
    GPIO.output(13,True)
    time.sleep(1)
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(9,True)
    time.sleep(1)
    '''
    i=1
    while i<8:
        GPIO.output(pin[:i],True)
        i+=i
        '''

