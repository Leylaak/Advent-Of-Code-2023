numeric_val = []

with open("Input") as file:
    for value in file: #output: individual strings of calibration values
        temp_val = []
        for code in value: #go through each line and pick out code
            if code.isnumeric():
                temp_val.append(code)
        #select only the 1st and last digit (if only one digit show it twice)
        digit = temp_val[0]+temp_val[-1]
        numeric_val.append(int(digit))
       
print(sum(numeric_val))

#Part 2
