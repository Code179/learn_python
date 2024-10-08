import random

score = 0

def main():
    level = get_level()
    generate_exercises(level)
    print(score)

def get_level():
    while True: 
        level = input("Level: ")
        try:
            level = int(level)
            if level in [1,2,3]:
                return level
            else:
                print("EEE")
        except ValueError:
            print("EEE")

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return (x,y)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return (x,y)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return (x,y)

def generate_exercises(level):
    for _ in range(10):
        x, y = generate_integer(level)
        for i in range(3):
            answer = input(f"{x} + {y} = ")
            try:
                answer = int(answer)
                if answer == x + y:
                    add_score()
                    break
                elif answer != x + y and i !=2:
                    print("EEE")
                else:
                    print("EEE")
                    print(f"{x} + {y} = {x + y}")
            except ValueError:
                print("EEE")
                if answer != x + y and i == 2:
                    print(f"{x} + {y} = {x + y}")

def add_score():
    global score 
    score += 1

if __name__ == "__main__":
    main()