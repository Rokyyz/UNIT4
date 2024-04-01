# Quiz053


# 1. UML Diagram
![CommSci 43](https://github.com/Rokyyz/UNIT4/assets/134658259/68c2d27c-f033-4352-b879-cd263b13a46b)

# 2. solutions


```.py
class palNum():
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def reverse(self, x):
        empty = ''
        for a in str(x):
            empty = a + empty
        return empty

    def get_pal_list(self):
        list = []
        for pal in range(self.A, self.B+1):
            if str(pal) == self.reverse(pal):
                list.append(pal)
        return list

test1 = palNum(1, 9)
test2 = palNum(10, 199)
print(test1.get_pal_list())
print(test2.get_pal_list())
```

# 3. proof of work

<img width="1440" alt="Screenshot 2024-04-01 at 13 59 01" src="https://github.com/Rokyyz/UNIT4/assets/134658259/a7138ee2-145a-4752-aad7-04f8d9ce05f6">
