class Tire:
    def __init__(self, tire_type: str, health: float, max_forwards_velocity: float, max_backwards_velocity: float, max_forwards_acceleration: float, max_backwards_acceleration: float, drag: float, max_rotation_speed: float):
        self.tire_type: str = tire_type
        self.health: float = health  # Soft 10000, Medium 15000, Hard 20000
        self.max_forwards_velocity: float = max_forwards_velocity
        self.max_backwards_velocity: float = max_backwards_velocity
        self.max_forwards_acceleration: float = max_forwards_acceleration  # Forwards acceleration
        self.max_backwards_acceleration: float = max_backwards_acceleration  # Backwards acceleration, also acts as braking force
        self.drag: float = drag  # Tire drag, causes slowdown when not holding accelerator
        self.max_rotation_speed: float = max_rotation_speed
