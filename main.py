from marsr.plateau import Plateau
from marsr.position import Position
from marsr.rover import Rover


def main():
    # inst = input ("Provide the string")
    inst = "5 5\n1 2 N LMLMLMLMM\n3 3 E MMRMMRMRRM"
    inst = inst.split('\n')
    max_x = inst[0].split()[0]
    max_y = inst[0].split()[1]
    inst.pop(0)
    plateau = Plateau(max_x, max_y)
    while inst:
        x_cord = int(inst[0].split()[0])
        y_cord = int(inst[0].split()[1])
        position = Position(x_cord, y_cord)
        dirctn = inst[0].split()[2]
        rover = Rover(plateau, position, dirctn)
        movement = inst[0].split()[3]
        rover.process(movement)
        print(rover)
        inst.pop(0)



if __name__ == "__main__":
    main()
