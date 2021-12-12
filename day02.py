from dataclasses import dataclass
from pathlib import Path

@dataclass
class Submarine:
    X: int = 0
    Y: int = 0
    aim: int = 0

    def reset_position(self):
        self.X = 0
        self.Y = 0
        self.aim = 0

def parse_command(command):
    direction, steps = command.split()
    
    if direction == 'up':
        steps = -int(steps)
    else:
        steps = int(steps)
    
    return direction, steps

def adjust_position(submarine, command):
    direction, steps = parse_command(command)

    if direction == 'forward':
        submarine.X += steps
    else:
        submarine.Y += steps 

def adjust_position_aim(submarine, command):
    direction, steps = parse_command(command)

    if not direction == 'forward': 
        submarine.aim += steps
    else:
        submarine.X += steps
        submarine.Y += submarine.aim * steps

def calculate_final_position(submarine, commands, adjust_func):
    submarine.reset_position()
    for command in commands.splitlines():
        adjust_func(submarine, command)
    return submarine.X * submarine.Y

if __name__ == '__main__':
    
    example = """forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2"""

    submarine = Submarine()

    assert calculate_final_position(submarine, example, adjust_func=adjust_position) == 150, 'adjust_position failed'
    assert calculate_final_position(submarine, example, adjust_func=adjust_position_aim) == 900, 'adjust_position_aim failed'
    
    handle = Path()/'input'/'day02-puzzle1.txt'
    commands = handle.read_text()
    print(calculate_final_position(submarine, commands, adjust_func=adjust_position_aim))
