__competition__ = False

# Library imports - hello there!
from vex import *

# Brain should be defined by default
brain = Brain()

motor_left_1 = Motor(Ports.PORT4, True)
motor_left_2 = Motor(Ports.PORT3, True)
motor_left_3 = Motor(Ports.PORT2, True)
motor_left_4 = Motor(Ports.PORT1, True)
motor_right_1 = Motor(Ports.PORT10)
motor_right_2 = Motor(Ports.PORT9)
motor_right_3 = Motor(Ports.PORT8)
motor_right_4 = Motor(Ports.PORT7)

left_group = MotorGroup(motor_left_1, motor_left_2, motor_left_3, motor_left_3)
right_group = MotorGroup(motor_right_1, motor_right_2,
                         motor_right_3, motor_right_4)

gyro = Gyro(brain.three_wire_port.f)

gyro.calibrate()

while gyro.is_calibrating():
    wait(50)

controller = Controller()

drivetrain = SmartDrive(left_group, right_group, gyro, 255)

panels = Pneumatics(brain.three_wire_port.e)

salute = Pneumatics(brain.three_wire_port.a)


def driver_control():
    last_pressed_s = False
    last_pressed_p = False
    while True:
        # Spin the left and right groups based on the controller
        left_group.spin(
            DirectionType.FORWARD,
            controller.axis3.position() + controller.axis1.position(),
            VelocityUnits.PERCENT)

        right_group.spin(
            DirectionType.FORWARD,
            controller.axis3.position() - controller.axis1.position(),
            VelocityUnits.PERCENT)
        wait(20)

        if controller.buttonR1.pressing() and not last_pressed_s:
            if panels.value():
                panels.close()
            else:
                panels.open()
        last_pressed_s = controller.buttonR1.pressing()

        if controller.buttonL1.pressing() and not last_pressed_p:
            if salute.value():
                salute.close()
            else:
                salute.open()
        last_pressed_p = controller.buttonL1.pressing()


def run(distance):
    drivetrain.drive_for(FORWARD, distance, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=30)


def autonomous_offense_1():
    """scores 1 triball"""
    run(-270)
    drivetrain.turn_for(LEFT, 25, DEGREES)
    run(-180)
    panels.open()
    run(-370)
    drivetrain.turn_for(RIGHT, 120, DEGREES)
    run(-410)
    run(140)
    # drivetrain.turn_for(LEFT, 90, DEGREES)
    # run(800)
    # drivetrain.turn_for(RIGHT, 90, DEGREES)
    # run(300)


def autonomous_defense_1():
    """Move a ball from corner and touch the bar"""
    salute.open()
    wait(1)
    run(-50)
    drivetrain.turn_for(LEFT, 180)
  # Arm up
    salute.close()
    drivetrain.turn_for(LEFT, 180)
    run(50)
    drivetrain.turn_for(LEFT, 90)
    run(50)
    drivetrain.turn_for(LEFT, 20)
    # Going back
    run(30)


def autonomous_skills():
    run(-1300)
    drivetrain.turn_for(LEFT, 30, DEGREES)
    panels.open
    run(-700)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    run(-500)
    run(100)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    run(700)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    run(-300)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    run(300)
    drivetrain.turn_for(LEFT, 30, DEGREES)
    run(-300)
    run(300)


wait(30, MSEC)


def noop():
    pass
