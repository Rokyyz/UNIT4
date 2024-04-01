# Quiz055


# 1. UML Diagram

![CommSci 48](https://github.com/Rokyyz/UNIT4/assets/134658259/01a71171-a542-45e6-b389-be1be9564521)


# 2. solutions

```.py
class Darts():
    def __init__(self, outer, middle, inner):
        self.outer = outer
        self.middle = middle
        self.inner = inner
    def calculate(self, x, y):
        coordinate = (y**2 + x**2)**0.5
        if coordinate <= self.inner:
            return 10
        elif coordinate <= self.middle:
            return 5
        elif coordinate <= self.outer:
            return 1
        else:
            return 0

test = Darts(1,5,10)
print(test.calculate(0,0))

```

# 3. proof of work

<img width="1440" alt="Screenshot 2024-04-01 at 14 31 05" src="https://github.com/Rokyyz/UNIT4/assets/134658259/6c69227e-5809-4150-8315-7b3edbc26c7e">
