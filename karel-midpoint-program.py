from stanfordkarel import *

def main():
    # Helper function to move Karel to a specific avenue
    def move_to_avenue(target_avenue, current_avenue):
        while current_avenue != target_avenue:
            if current_avenue < target_avenue:
                while not facing_east():
                    turn_left()
                move()
                current_avenue += 1
            else:
                while not facing_west():
                    turn_left()
                move()
                current_avenue -= 1
        return current_avenue

    # 1. Determine the width and go to the last avenue
    width = 1
    current_avenue = 1
    while front_is_clear():
        move()
        width += 1
        current_avenue += 1
    put_beeper()  # Last avenue

    # 2. Go to the first avenue
    turn_around()
    current_avenue = move_to_avenue(1, current_avenue)
    put_beeper()  # First avenue

    # 3. Place beepers in the alternating sequence
    for i in range(1, (width + 1) // 2):
        # Go to the (width - i) avenue
        current_avenue = move_to_avenue(width - i, current_avenue)
        put_beeper()

        if width % 2 == 0 or i < width // 2:  # Avoid double placement in odd width center
            # Go to the (i + 1) avenue
            current_avenue = move_to_avenue(i + 1, current_avenue)
            put_beeper()

    # Optionally, face East
    while not facing_east():
        turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()