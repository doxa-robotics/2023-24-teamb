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

drivetrain = SmartDrive(left_group, right_group, inertia_sensor, 255)


class PneumaticsGroup:
    children: list[Pneumatics]

    def __init__(self, *pneumatics: Pneumatics) -> None:
        self.children = list(pneumatics)

    def open(self):
        for child in self.children:
            child.open()

    def close(self):
        for child in self.children:
            child.close()

    def value(self):
        for child in self.children:
            if child.value():
                return True
        return False


pusher1 = Pneumatics(brain.three_wire_port.a)
pusher2 = Pneumatics(brain.three_wire_port.c)
pushers = PneumaticsGroup(pusher1, pusher2)

controller = Controller()


def R1_open():
    pushers.open()


controller.buttonR1.pressed(R1_open)


def driver_control():
    last_pressed = False
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

        if controller.buttonA.pressing() and not last_pressed:
            if pushers.value():
                pushers.close()
            else:
                pushers.open()
        last_pressed = controller.buttonA.pressing()


def autonomous_defense1():
    drivetrain.drive_for(FORWARD, 1200, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(LEFT, 90)
    drivetrain.drive_for(FORWARD, 500, DistanceUnits.MM,
                         units_v=VelocityUnits.PERCENT)
    drivetrain.turn_for(RIGHT, 90)*96

def autonomous_offense1():
    drivetrain.drive_for(FORWARD, 1000, DistanceUnits.MM,
    units_v=VelocityUnits.PERCENT,velocity=100,
    )
    drivetrain.turn_for(LEFT,90, DEGREES)

driver_control()
