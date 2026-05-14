import turtle

class Countdown:
    def __init__(self, screen, minutes=10):
        self.screen = screen
        self.time_left = minutes * 60  # convert to seconds

        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(0, 260)  # top of screen
        self.writer.color("black")

    def update(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.writer.clear()
        self.writer.write(f"Time Left: {minutes:02d}:{seconds:02d}",
                          align="center", font=("Arial", 16, "bold"))

        if self.time_left > 0:
            self.time_left -= 1
            self.screen.ontimer(self.update, 1000)
        else:
            self.writer.clear()
            self.writer.write("TIME'S UP!", align="center",
                              font=("Arial", 24, "bold"))
