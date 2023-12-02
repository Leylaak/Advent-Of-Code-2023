power = 0 

with open("Input day 2") as file:
    for line in file:
        max_red, max_blue, max_green = 0, 0, 0
        draws = line.strip().split(":")[1]
        for draw in draws.strip().split(";"):
            for element in draw.split(","):
                number,colour  = element.strip().split(" ")
                number = int(number)
                if colour == 'red' and number > max_red:
                    max_red = number
                elif colour == 'blue' and number > max_blue:
                    max_blue = number
                elif colour == 'green' and number > max_green:
                    max_green = number
        power += (max_red * max_blue * max_green)

print(power)
        




                

