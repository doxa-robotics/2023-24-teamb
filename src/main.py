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


def run(distance, velocity=40):
    drivetrain.drive_for(FORWARD, distance, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=velocity)


def autonomous_offense_1():
    """scores 1 triball"""
    run(-160, 60)
    run(-60)
    drivetrain.turn_for(LEFT, 25, DEGREES)
    run(-170)
    panels.open()
    run(-360)
    drivetrain.turn_for(RIGHT, 125, DEGREES, velocity=20, units_v=RPM)
    run(-410, 60)
    run(180, 60)
    panels.close()
    drivetrain.turn_for(LEFT, 115, DEGREES)
    run(750, 85)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    run(320, 70)
    run(90, 10)


def autonomous_defense_1():
    """Move a ball from corner and touch the bar"""
    salute.open()
    wait(1000)
    run(-424.25)
    drivetrain.turn_for(LEFT, 180)
    # Arm up
    salute.close()
    drivetrain.turn_for(LEFT, 180)
    drivetrain.turn_for(LEFT, 45)
    run(600)
    drivetrain.turn_for(LEFT, 90)
    # Going back
    run(550)


def autonomous_defense_2():
    """ (Zachary wrote) Moves a ball from the corner and touches the bar."""
    run(260)
    run(100, 10)
    # drivetrain.turn_for(LEFT, 45)
    salute.open()  # down
    wait(1000)  # in ms, so that's one second
    run(-300, 20)
    salute.close()  # up
    drivetrain.turn_for(LEFT, 65)
    run(350)
    drivetrain.turn_for(LEFT, 90)
    run(310)


def auton_o2():
    """ taipei asked for this """
    run(700)
    run(-700)
    drivetrain.turn_for(LEFT, 90)
    run(1200)
    drivetrain.turn_for(RIGHT, 45)
    panels.open()
    run(600)
    drivetrain.turn_for(RIGHT, 90)
    run(1000)


def autonomous_d():
    """If didn't work: Go touching a bar from defence start without touching triball"""
    drivetrain.turn_for(RIGHT, 90)
    run(580)


def autonomous_skills():
    """drivetrain.turn_for(RIGHT, 35, DEGREES)
    run(-400)
    panels.open()
    wait(3000, MSEC)
    panels.close()
    drivetrain.turn_for(LEFT, 180, DEGREES)
    run(-300)
    drivetrain.turn_for(LEFT, 35, DEGREES)
    run(-1050)
    panels.open()"""
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


Competition(driver_control, auton_o2)
