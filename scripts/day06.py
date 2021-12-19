
# plan
# itertools cycle (call next()) for lifecycle
# factory method

class LanternFish:
    
    mature_lifespan = [6, 5, 4, 3, 2, 1, 0]

    def __init__(self, timer):
        self.timer = timer if timer else 8
        self.is_mature = True if timer else False

    def increment_timer(self):
        if not self.is_mature():
            self.timer - 1
            if self.timer == 0:
                self.is_mature = True
        else:
            pass

    @classmethod
    def from_mature(cls, timer):
        pass

def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        if element <= 6:
            saved.append(element)
    while saved:
        for element in saved:
              yield element

def test_cycle(start):
    nums = list(range(start, -1, -1))
    for i,num in enumerate(cycle(nums)):
        print(num) 
        if i > 10: 
            break

if __name__ == '__main__':
    test_cycle(8)
