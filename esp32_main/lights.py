from machine import Pin, PWM
import utime


# This is still in BETA testing. 
# The below light() function transtions between start value and stop values by increments as stated in the increase_X = variable. 
# Still need to develop all of the various transitions and write the MQTT stuff. 


r = PWM(Pin(16))
b = PWM(Pin(17))
ww = PWM(Pin(18)) 
cw = PWM(Pin(19))

def dark_sunrise():
    red = 0
    blue = 0
    cool = 0
    warm = 0

    increase_r = 1
    increase_b = 2
    increase_cw = 3
    increase_ww = 4
    
    while True:
        utime.sleep_ms(30)
        while r.duty(red) != (1000):
            if red > 300:
                print(str(r.duty()) + ' r.duty') # print() statements are for testing
                print(str(red) + ' red lights')
                break
            else:
                print(str(r.duty()) + ' r.duty') 
                print(str(red) + ' red lights') 
                red += increase_r
            break
        while b.duty(blue) != (1000):
            if blue > 300:
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
            else:    
                print(str(b.duty()) + ' b.duty')
                print(str(blue) + ' blue lights')
                blue += increase_b
            break
        while cw.duty(cool) != (1000):
            if cool > 300:
                print(str(cw.duty()) + ' cw.duty') # print() statements are for testing
                print(str(cool) + ' Cool White')
                break
            else:
                print(str(cw.duty()) + ' cw.duty') 
                print(str(cool) + ' Cool White') 
                cool += increase_cw
            break
        while ww.duty(warm) != (1000):
            if warm > 600:
                print(str(ww.duty()) + ' ww.duty') # print() statements are for testing
                print(str(warm) + ' Warm White')
                break
            else:
                print(str(ww.duty()) + ' ww.duty') 
                print(str(warm) + ' Warm White') 
                warm += increase_ww
            break
        if red > 300 and blue > 300 and cool > 300 and warm > 600:
            break
def dark_sunrise():
def sunrise_morning():
def morning_highnoon():
def highnoon_sunset():
def sunset_dusk():
def dusk_dark():

def starrynight():
    # This may need to be a seperate idea - maybe using WS2812b RGB LED's. 