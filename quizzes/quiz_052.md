# Quiz052


# 1. UML Diagram

![CommSci 46](https://github.com/Rokyyz/UNIT4/assets/134658259/0ab03ec3-39b8-4966-9c44-838c89df3c33)


# 2. solutions


```.py
class Bycycle():
    def __init__(self, material:str,size:int):
        self.material = material
        self.my_wheels = Wheel(size)

    def ride(self):
        output = f"The bike is made out of {self.material}, and the wheel size is {self.my_wheels.size}in"
        return output
class Wheel():
    def __init__(self,size:int):
        self.size = size
    def get_size(self):
        return self.size
    def get_parameter(self):
        parameter = self.size * 2.54 * 3.14
        return parameter
    def get_rotation(self):
        output = round(100000/self.get_parameter())
        message = f"The wheel does {output} rotations per km"
        return message

create = Bycycle(material='Carbon',size=26 )
test = Wheel(size=26)
print(create.ride())
print(test.get_rotation())
```

# 3. proof of work

<img width="1440" alt="Screenshot 2024-04-01 at 13 47 23" src="https://github.com/Rokyyz/UNIT4/assets/134658259/989ec557-48f4-472f-a0b6-19583697ff2d">
