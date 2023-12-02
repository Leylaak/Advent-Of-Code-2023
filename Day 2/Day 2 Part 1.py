red = 12
green = 13
blue = 14
game_id_sum = 0 

with open("Input day 2") as file:
    for line in file:
        game_id, draws = line.strip().split(":")
        breakout = False
        for draw in draws.strip().split(";"):
            if breakout:
                break
            cubes = draw.split(",")
            for element in cubes:
                number,colour  = element.strip().split(" ")
                number = int(number)
                if (colour == 'red' and number > 12) or (colour == 'green' and number > 13) or (colour == 'blue' and number > 14):
                    breakout = True
                    break
        if breakout == False:
            game_id_sum += int(game_id.split(" ")[1])

print(game_id_sum)
                


        
