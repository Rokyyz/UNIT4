# Quiz054


# 1. UML Diagram

![CommSci 44](https://github.com/Rokyyz/UNIT4/assets/134658259/2916528b-f44e-4d38-b3f5-b38f7df62a5c)


# 2. solutions

```.py

class rainDrops():
    def pour(self, n:int):
        result = ""
        if n%3 == 0:
            result += "Pling"
        if n%5 == 0:
            result += "Plang"
        if n%7 == 0:
            result += "Plong"
        if n%7!=0 and n%3!=0 and n%5!=0:
            return str(n)

        return result

test1 = rainDrops()
print(test1.pour(28))
test2 = rainDrops()
print(test2.pour(30))
test3 = rainDrops()
print(test3.pour(34))

```

# 3. proof of work

<img width="1440" alt="Screenshot 2024-04-01 at 14 21 46" src="https://github.com/Rokyyz/UNIT4/assets/134658259/cfa9a0a3-d47c-40d5-ad97-9e65f8c51639">

