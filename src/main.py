__competition__ = False

# Library imports - hello there!
from vex import *

# Brain should be defined by default
brain = Brain()

motor_left_1 = Motor(Ports.PORT4, True)
motor_left_2 = Motor(Ports.PORT3, True)
motor_left_3 = Motor(Ports.PORT2, True)
motor_left_4 = Motor(Ports.PORT1, True)
motor_right_1 = Motor(Ports.PORT6)
motor_right_2 = Motor(Ports.PORT9)
motor_right_3 = Motor(Ports.PORT8)
motor_right_4 = Motor(Ports.PORT7)

left_group = MotorGroup(motor_left_1, motor_left_2, motor_left_3, motor_left_3)
right_group = MotorGroup(motor_right_1, motor_right_2,
                         motor_right_3, motor_right_4)

gyro = Gyro(brain.three_wire_port.f)

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
                         units_v=VelocityUnits.PERCENT, velocity=50)


def autonomous_offense_1():
    """scores 1 triball"""
    run(600)
    drivetrain.turn_for(LEFT, 15, DEGREES)
    run(200)
    drivetrain.turn_for(RIGHT, 105, DEGREES)
    run(350)
    run(-150)


def autonomous_defense_1():
    drivetrain.drive_for(FORWARD, 1200, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(LEFT, 90)
    drivetrain.drive_for(FORWARD, 500, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(RIGHT, 90)


def autonomous_defense():
    """Offense 2: Goes right side for the goal """
    drivetrain.drive_for(FORWARD, 500, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100,
                         )
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 600, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 900, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    """Going to the bar at last"""
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1400, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 900, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )


def autonomous_skills():

    drivetrain.drive_for(FORWARD, 900, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100)


wait(30, MSEC)


def noop():
    pass


# Competition(autonomous_offense_1, driver_control)
autonomous_offense_1()
