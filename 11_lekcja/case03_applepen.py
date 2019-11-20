class Pen:
    def __init__(self):
        print("I have a pen!")

    def what_pen(self):
        return "pen"


class Apple:
    def __init__(self):
        print("I have an apple!")
    def what_apple(self):
        return "apple"


class ApplePen(Pen, Apple):
    def __init__(self):
        print("Ooh")

    def wut(self):
        x = super().what_apple() + super().what_pen()
        return x

    def more_wut(self):
        Apple.__init__(self)
        Pen.__init__(self)
        x = super().what_apple() + super().what_pen()
        print("Oooooh", x)



no_logic = ApplePen()
print(no_logic.wut())
ApplePen().more_wut()
