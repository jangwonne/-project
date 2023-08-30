class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.speed = 0
        self.max_speed = max_speed

    def accelerate(self, amount):
        self.speed += amount
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed
