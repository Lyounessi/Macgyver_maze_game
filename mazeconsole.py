"""This python file contains a console's logic 
mode as prototype for our game"""

maze_map = ("WWWWWWWWWWWWWWW\n"
           "WW----M-------W\n"
           "W----WWWWW----W\n"
           "WW--WWWWWWWWWTW\n"
           "WW-----WWWWWWWW\n"
           "WWW----------WW\n"
           "WWWW---E--WWWWW\n"
           "WWW----W----WWW\n"
           "WW--WWWWW----WW\n"
           "WW--N-WWWWW---W\n"
           "WWW----------WW\n"
           "WWWW--WW----WWW\n"
           "WWWWWW----WWWWW\n"
           "WWWWWWWGWWWWWWW")

#Write the map in the file 'my-map.txt'
with open("my-map.txt","w") as file_w:
	file_w.write(maze_map)

#Read the map and put it in a 2D list
used_map = list(list())
with open("my-map.txt","r") as file_r:
    for line in file_r:
        used_map.append([char for char in line if char !="\n"])

#Print the map in console mode
for i, line in enumerate(used_map):
    for j, char in enumerate(line):
        print(used_map[i][j], end="")
    print("")

#Find the position of the letter "M" inour 2Dlist used_map
m_line = 0
m_col = 0
for i, line in enumerate(used_map):
    for j, char in enumerate(line):
        if char == "M":
            m_line = i
            m_col = j

#Launch the game with inputs to move the char "M"
test = True
while test:
    answer = input("Choisissez une lettre pour déplacer le joueur? (N,S,E,W) ou Q pour quitter")
    if answer == "Q":
        test = False
    elif answer == "N":
        if used_map[m_line - 1][m_col] == "-":
            used_map[m_line - 1][m_col] = "M"
            used_map[m_line][m_col] = "-"
            m_line -= 1
        else:
            print("Impossible de dépasser l'élément!")
    elif answer == "S":
        if used_map[m_line + 1][m_col] == "-":
            used_map[m_line + 1][m_col] = "M"
            used_map[m_line][m_col] = "-"
            m_line += 1
        else:
            print("Impossible de dépasser l'élément!")
    elif answer == "E":
        if used_map[m_line][m_col + 1] == "-":
            used_map[m_line][m_col + 1] = "M"
            used_map[m_line][m_col] = "-"
            m_col += 1
        else:
            print("Impossible de dépasser l'élément!")
    elif answer == "W":
        if used_map[m_line][m_col - 1] == "-":
            used_map[m_line][m_col - 1] = "M"
            used_map[m_line][m_col] = "-"
            m_col -= 1
        else:
            print("Impossible de dépasser l'élément!")
    else:
        print("Réponse non correcte")

    #Reprint the map
    for i, line in enumerate(used_map):
        for j, char in enumerate(line):
            print(used_map[i][j], end="")
        print("")        
