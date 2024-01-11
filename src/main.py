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

inertia_sensor = Inertial(Ports.PORT1)

controller = Controller()

drivetrain = SmartDrive(left_group, right_group, inertia_sensor, 255)

panels = Pneumatics(brain.three_wire_port.a)

salute = Pneumatics(brain.three_wire_port.e)


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
            if panels.value():
                panels.close()
            else:
                panels.open()
        last_pressed_p = controller.buttonL1.pressing()


def autonomous_defense1():
    drivetrain.drive_for(FORWARD, 1200, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(LEFT, 90)
    drivetrain.drive_for(FORWARD, 500, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(RIGHT, 90)


def autonomous_offense1():
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100,
                         )
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 500, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT, velocity=100
                         )


driver_control()
