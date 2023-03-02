import random


# defines class tank and variables
class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tank_direction = "North"
        self.shot_direction = {"North": 0, "South": 0, "West": 0, "East": 0}
        self.points = 100
        self.successful_shots = 0
        self.target_x = random.randint(-5, 5)
        self.target_y = random.randint(-5, 5)

# four methods that are used when tank moves in one of four directions
    def move_up(self):
        self.y += 1
        self.tank_direction = "North"
        self.points -= 10

    def move_down(self):
        self.y -= 1
        self.tank_direction = "South"
        self.points -= 10

    def move_left(self):
        self.x -= 1
        self.tank_direction = "West"
        self.points -= 10

    def move_right(self):
        self.x += 1
        self.tank_direction = "East"
        self.points -= 10

    def target(self):
        return (
                (self.x == self.target_x and self.tank_direction == 'North' and self.target_y > self.y) or
                (self.x == self.target_x and self.tank_direction == 'South' and self.target_y < self.y) or
                (self.y == self.target_y and self.tank_direction == 'West' and self.target_x < self.x) or
                (self.y == self.target_y and self.tank_direction == 'East' and self.target_x > self.x)
        )

    def shot(self):
        self.shot_direction[self.tank_direction] += 1
        if self.target():
            print("Target hit")
            self.points += 10
            self.successful_shots += 1
            self.target_x = random.randint(-5, 5)
            self.target_y = random.randint(-5, 5)
        else:
            print("missed")

    def info(self):
        print(f"Tank direction: {self.tank_direction}\nTank coordinates: x: {self.x} y: {self.y}")
        print(f"Shot directions: north- {self.shot_direction['North']}, south - {self.shot_direction['South']},"
              f"west- {self.shot_direction['West']}, east- {self.shot_direction['East']}")
        print(f"Current points: {self.points}")
        # print(f"Hidden target position: x: {self.target_x} y: {self.target_y}")
        print(f"Successful shots: {self.successful_shots} ")
