# include the servo library
from servo import Servo
# include the time library
import time
# include the pin library
from machine import Pin

# ── SWITCH ─────────────────────────────────────────────────
# initialise the switch pin as an input with pull-down
push = Pin(14, Pin.IN, Pin.PULL_UP)

# ── SERVO SETUP ────────────────────────────────────────────
# initialise the pins to be outputs - Servo is an output device
servo_mid_pin  = Pin(13, Pin.OUT)   # middle finger
servo_ring_pin = Pin(12, Pin.OUT)   # ring finger

# initialise the servos for use
servo_mid  = Servo(servo_mid_pin)
servo_ring = Servo(servo_ring_pin)

# ── DC MOTOR SETUP ─────────────────────────────────────────
# initialise the DC motor pins as outputs
dc_index_in1  = Pin(18, Pin.OUT)   # index finger - forward
dc_index_in2  = Pin(4, Pin.OUT)   # index finger - keep LOW
dc_little_in3 = Pin(22, Pin.OUT)   # little finger - forward
dc_little_in4 = Pin(23, Pin.OUT)   # little finger - keep LOW

# ── WIGGLE ANGLES ──────────────────────────────────────────
# the servo will step between these angles to wiggle the finger
WIGGLE_ANGLES = [30, 90, 150, 90]
wiggle_index  = 0

# ── MOTOR CONTROL FUNCTIONS ────────────────────────────────
# turn both DC motors on (index and little finger move forward)
def dc_motors_on():
    dc_index_in1.value(1)
    dc_index_in2.value(0)
    dc_little_in3.value(1)
    dc_little_in4.value(0)

# turn both DC motors off
def dc_motors_off():
    dc_index_in1.value(0)
    dc_index_in2.value(0)
    dc_little_in3.value(0)
    dc_little_in4.value(0)

# stop both servos (write to neutral and release)
def servos_off():
    servo_mid.write_angle(90)
    servo_ring.write_angle(90)

# ── MAIN LOOP ──────────────────────────────────────────────
print("Walking Hand Ready. Waiting for switch...")

while True:
    if push.value() == 0:      # switch is PRESSED
        print("A")
        # DC motors run continuously while switch is held
        dc_motors_on()

        # servos wiggle through the angle list one step at a time
        servo_mid.write_angle(WIGGLE_ANGLES[wiggle_index])
        servo_ring.write_angle(WIGGLE_ANGLES[wiggle_index])

        # move to next angle in the wiggle sequence
        wiggle_index = (wiggle_index + 1) % len(WIGGLE_ANGLES)

        # small delay between each wiggle step
        time.sleep(0.3)

    else:                           # switch is NOT pressed
        dc_motors_off()
        servos_off()
        wiggle_index = 0            # reset wiggle for next press
        time.sleep(0.05)            # small idle delay