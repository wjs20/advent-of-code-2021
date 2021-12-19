
# plan
# itertools cycle (call next()) for lifecycle
# factory method

class LanternFish:

    def __init__(self, stage):
        self.stage = stage

    def __iter__(self):
        return self

    def __next__(self):
        if self.stage > 0:
            self.stage -= 1
        else:
            self.stage = 6

    def can_reproduce(self):
        return True if self.stage == 0 else False

if __name__ == '__main__':

    fish = [LanternFish(n) for n in [4,1,9]]

    iterations = 10
    for i in range(iterations):
        
        for f in fish:


