"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def printMan():
    for i in range(3):
        print(man[i][0] + man[i][1] + man[i][2])

def turn():
    replace = {
        "(" : ")",
        ")" : "(",
        "<" : ">",
        ">" : "<",
        "/" : "\\",
        "\\" : "/",
        " " : " " 
    }
    
    temp_1 = man[0][0]
    temp_2 = man[1][0]
    temp_3 = man[2][0]
    
    man[0][0] = replace[man[0][2]]
    man[1][0] = replace[man[1][2]]
    man[2][0] = replace[man[2][2]]
    man[0][2] = replace[temp_1]
    man[1][2] = replace[temp_2]
    man[2][2] = replace[temp_3]


for i in range(int(input())):
    num_commands = int(input())
    
    man = [[" ", "o", " "], ["/", "|", "\\"], ["/", " ", "\\"]]
    
    turned = False
    
    for j in range(num_commands):
        command = input()
        
        if command == "turn":
            turn()
            printMan()
            turned = not turned
            
        elif command[:3] == "say":
            print(command[4:])  
            
        else:
            command = command.split()
            
            side = command[0]
            body_part = command[1]
            position = command[-1]
            
            if turned:
                if side == "left":
                    side = "right"
                else:
                    side = "left"
                    
            if position == "head":
                if side == "left":
                    man[0][2] = ")"
                    man[1][2] = " "
                else:
                    man[0][0] = "("
                    man[1][0] = " "
            
            elif position == "hip":
                if side == "left":
                    man[0][2] = " "
                    man[1][2] = ">"
                else:
                    man[0][0] = " "
                    man[1][0] = "<"
                    
            elif position == "start":
                if side == "left":
                    man[0][2] = " "
                    man[1][2] = "\\"
                else:
                    man[0][0] = " "
                    man[1][0] = "/"
                    
            elif position == "in":
                if side == "left":
                    man[2][2] = ">"
                else:
                    man[2][0] = "<"
                    
            elif position == "out":
                if side == "left":
                    man[2][2] = "\\"
                else:
                    man[2][0] = "/"
                    
            printMan()
