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


def autonomous_defense1():
    drivetrain.drive_for(FORWARD, 1200, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(LEFT, 90)
    drivetrain.drive_for(FORWARD, 500, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(RIGHT, 90)


def autonomous_offense1():
    """ Offense 1: Goes left side for the goal """
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100,
                         )
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 350, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )


def autonomous_offense2():
    """Offense 2: Goes right side for the goal """
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100,
                         )
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 350, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )


def driver_controll3r():
    """Challenge Made The Driver Control"""

    def axis1():
        right_group.spin(FORWARD, controller.axis1.position(), PERCENT,
                         VelocityPercentUnits=VelocityUnits)
    controller.axis1.changed(axis1)

    def axis3():
        left_group.spin(FORWARD, controller.axis3.position(), PERCENT,
                        VelocityPercentUnits=VelocityUnits)
    controller.axis3.changed(axis3)

    def buttonRight():

        if controller.buttonRight.pressed:
            left_group.spin_to_position(90, DEGREES)
        if controller.buttonRight.released:
            left_group.stop


wait(30, MSEC)


driver_control()
