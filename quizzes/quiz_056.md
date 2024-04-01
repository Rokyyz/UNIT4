# Quiz056


# 1. UML Diagram

Does not require one

# 2. solutions

```.py
def secret_handshake(number):
    actions = []
    binary_str = format(number, '05b')
    if binary_str[-1] == '1':
        actions.append("wink")
    if binary_str[-2] == '1':
        actions.append("double blink")
    if binary_str[-3] == '1':
        actions.append("close your eyes")
    if binary_str[-4] == '1':
        actions.append("jump")
    if binary_str[-5] == '1':
        actions.reverse()

    return actions

number = 77
handshake = secret_handshake(number)
print("Secret Handshake for number", number, ":", handshake)

```

# 3. proof of work
<img width="1440" alt="Screenshot 2024-04-01 at 14 35 34" src="https://github.com/Rokyyz/UNIT4/assets/134658259/6f6ede34-6c17-4104-ab9b-8f91dc22fbc9">
