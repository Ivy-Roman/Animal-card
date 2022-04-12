# # import turtle
# # tim = turtle.Turtle()
# # tim.color("red")
# # tim.width(4)
# # tim.forward(100)


# name = input("What's your name?")
# print("Hello,", name, "!")

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                return f"{x} * {y} == 512"   # does not do what we want!
