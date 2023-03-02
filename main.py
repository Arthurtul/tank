from tank import Tank

tank = Tank()

while True:
    action = input("w - up, s- down, a - left, d - right, f - shoot, i - info, q - quit game\n")
    match action:
        case "w":
            tank.move_up()
        case "s":
            tank.move_down()
        case "a":
            tank.move_left()
        case "d":
            tank.move_right()
        case "f":
            tank.shot()
        case "i":
            tank.info()
        case "q":
            break
    if tank.points <= 0:
        print("you lose")
        break
