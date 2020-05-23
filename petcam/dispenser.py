import os

if os.environ.get('MOCK'):
    import petcam.mocks.stepper_motor as sm
else:
    import petcam.drivers.stepper_motor as sm


class Dispenser:
    DELAY_MS = 5
    STEPS_PER_ANGLE = 51

    def __init__(self):
        # Need to add extra step since one angle is actually 51.5 degrees
        self._add_extra_step = False

    def move(self):
        steps = self.STEPS_PER_ANGLE

        if self._add_extra_step:
            steps += 1

        self._add_extra_step = not self._add_extra_step

        sm.forward(self.DELAY_MS/1000.0, steps)
        sm.off()


if __name__ == "__main__":
    dispenser = Dispenser()

    while True:
        input("Press ENTER to move")
        dispenser.move()
