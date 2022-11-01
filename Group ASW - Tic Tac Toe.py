from engi1020.arduino.api import *
from time import sleep

# This function takes the player's name and assigned key (X or O) as the arguments
# Within the function, we take an input from the player
# First we check if the player wishes to leave the game
# We use a while try except loop to prompt the user again and again for the proper input
# The function checks the following:
#      - The input has a length of 2
#      - The numbers entered are between 1 and 3
#      - The row-column spot is not already taken
# At the end of the function, since no exceptions were raised, the Row-Column will be updated

def Inputter(Player1, A):
    global Row_Col_List
    global Quit_List
    while True:
        try:
            bruh = input(f"{Player1}, Please enter the row column number. Row first, column next: ")
            
            for i in Quit_List:
                if bruh == i:
                    return "lose"

            if len(bruh) != 2:
                oled_print("Sorry, your input should have a length of 2")
                raise Exception()
            elif int(bruh[0]) != 1 and int(bruh[0]) != 2 and int(bruh[0]) != 3:
                oled_print("Sorry, your 1st number does not lie within the range of 1 - 3")
                raise Exception()
            elif int(bruh[1]) != 1 and int(bruh[1]) != 2 and int(bruh[1]) != 3:
                oled_print("Sorry, your 2nd number does not lie within the range of 1 - 3")
                raise Exception()
            elif Row_Col_List[int(bruh[0])-1][int(bruh[1])-1] == "X" or Row_Col_List[int(bruh[0])-1][int(bruh[1])-1] == "O":
                oled_print("Sorry, this spot is already taken. Kindly enter again.")
                raise Exception()
            break
        except: pass
        
    Row_Col_List[int(bruh[0])-1][int(bruh[1])-1] = A

# This function checks for the winner
# We check all 8 variations through which one can win the game (3 Cols, 3 Rows and 2 Diagonals)
# Since we want a special formatting, we need to manually print each.
#       - \033[4m gives us a bold formatting
#       - \033[3m gives us an italic formatting
#       - \033[0m is the stop formatting - it stops formatting beyong this point
# If the conditions were met, we print the winning grid and return the name of the player
# Otherwise, we print the normal grid

def winner(A, Player1):
    if Row_Col_List[0][0] == A and Row_Col_List[0][1] == A and Row_Col_List[0][2] == A:
        oled_clear()
        print(f"""
            \033[4m\033[1m{A}\033[0m|\033[4m\033[1m{A}\033[0m|\033[4m\033[1m{A}\033[0m
            -+-+-
            \033[3m{Row_Col_List[1][0]}\033[0m|\033[3m{Row_Col_List[1][1]}\033[0m|\033[3m{Row_Col_List[1][2]}\033[0m
            -+-+- 
            \033[3m{Row_Col_List[2][0]}\033[0m|\033[3m{Row_Col_List[2][1]}\033[0m|\033[3m{Row_Col_List[2][2]}\033[0m
                """)
        return Player1
    elif Row_Col_List[1][0] == A and Row_Col_List[1][1] == A and Row_Col_List[1][2] == A:
        oled_clear()
        print(f"""
            \033[3m{Row_Col_List[0][0]}\033[0m|\033[3m{Row_Col_List[0][1]}\033[0m|\033[3m{Row_Col_List[0][2]}\033[0m
            -+-+-
            \033[4m\033[1m{A}\033[0m|\033[4m\033[1m{A}\033[0m|\033[4m\033[1m{A}\033[0m
            -+-+- 
            \033[3m{Row_Col_List[2][0]}\033[0m|\033[3m{Row_Col_List[2][1]}\033[0m|\033[3m{Row_Col_List[2][2]}\033[0m
                """)
        return Player1
        
    elif Row_Col_List[2][0] == A and Row_Col_List[2][1] == A and Row_Col_List[2][2] == A:
        oled_clear()
        print(f"""
            \033[3m{Row_Col_List[0][0]}\033[0m|\033[3m{Row_Col_List[0][1]}\033[0m|\033[3m{Row_Col_List[0][2]}\033[0m
            -+-+-
            \033[3m{Row_Col_List[1][0]}\033[0m|\033[3m{Row_Col_List[1][1]}\033[0m|\033[3m{Row_Col_List[1][2]}\033[0m
            -+-+- 
            \033[4m\033[1m{A}\033[0m|\033[4m\033[1m{A}\033[0m|\033[4m\033[1m{A}\033[0m
                """)
        return Player1
        
    elif Row_Col_List[0][0] == A and Row_Col_List[1][0] == A and Row_Col_List[2][0] == A:
        oled_clear()
        print(f"""
            \033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[0][1]}\033[0m|\033[3m{Row_Col_List[0][2]}\033[0m
            -+-+-
            \033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[1][1]}\033[0m|\033[3m{Row_Col_List[1][2]}\033[0m
            -+-+- 
            \033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[2][1]}\033[0m|\033[3m{Row_Col_List[2][2]}\033[0m
                """)
        return Player1
        
    elif Row_Col_List[0][1] == A and Row_Col_List[1][1] == A and Row_Col_List[2][1] == A:
        oled_clear()
        print(f"""
            \033[3m{Row_Col_List[0][0]}\033[0m|\033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[0][2]}\033[0m
            -+-+-
            \033[3m{Row_Col_List[1][0]}\033[0m|\033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[1][2]}\033[0m
            -+-+- 
            \033[3m{Row_Col_List[2][0]}\033[0m|\033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[2][2]}\033[0m
                """)
        return Player1
        
    elif Row_Col_List[0][2] == A and Row_Col_List[1][2] == A and Row_Col_List[2][2] == A:
        oled_clear()
        print(f"""
            \033[3m{Row_Col_List[0][0]}\033[0m|\033[3m{Row_Col_List[0][1]}\033[0m|\033[4m\033[1m{A}\033[0m
            -+-+-
            \033[3m{Row_Col_List[1][0]}\033[0m|\033[3m{Row_Col_List[1][1]}\033[0m|\033[4m\033[1m{A}\033[0m
            -+-+- 
            \033[3m{Row_Col_List[2][0]}\033[0m|\033[3m{Row_Col_List[2][1]}\033[0m|\033[4m\033[1m{A}\033[0m
                """)
        return Player1
        
    elif Row_Col_List[0][0] == A and Row_Col_List[1][1] == A and Row_Col_List[2][2] == A:
        oled_clear()
        print(f"""
            \033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[0][1]}\033[0m|\033[3m{Row_Col_List[0][2]}\033[0m
            -+-+-
            \033[3m{Row_Col_List[1][0]}\033[0m|\033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[1][2]}\033[0m
            -+-+- 
            \033[3m{Row_Col_List[2][0]}\033[0m|\033[3m{Row_Col_List[2][1]}\033[0m|\033[4m\033[1m{A}\033[0m
                """)
        return Player1
        
    elif Row_Col_List[2][0] == A and Row_Col_List[1][1] == A and Row_Col_List[0][2] == A:
        oled_clear()
        print(f"""
                \033[3m{Row_Col_List[0][0]}\033[0m|\033[3m{Row_Col_List[0][1]}\033[0m|\033[4m\033[1m{A}\033[0m
                -+-+-
                \033[3m{Row_Col_List[1][0]}\033[0m|\033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[1][2]}\033[0m
                -+-+- 
                \033[4m\033[1m{A}\033[0m|\033[3m{Row_Col_List[2][1]}\033[0m|\033[3m{Row_Col_List[2][2]}\033[0m
                    """)
        return Player1
    
    oled_clear()
    print(f"""
        {Row_Col_List[0][0]}|{Row_Col_List[0][1]}|{Row_Col_List[0][2]}
        -+-+-
        {Row_Col_List[1][0]}|{Row_Col_List[1][1]}|{Row_Col_List[1][2]}
        -+-+- 
        {Row_Col_List[2][0]}|{Row_Col_List[2][1]}|{Row_Col_List[2][2]}
            """)

# This function defines the Game Rules, at the start of each game
# This helps the player read through and understand what numbers to input
# It also introduces the player to the "Quit List" - a list of inputs which will allow them to exit

def Game_Rules():
    global Player1
    global Player2
    global Quit_List
    print(f"""{Player1} and {Player2}, please go through the game rules below:""")
    {sleep(0.5)}
    print(f"""
    The TicTacToe game is a 3x3 grid, which players have to fill with their characters, X or O.
    The Game will prompt you for a 'row column number' which is assigned to each key in the grid.""")
    {sleep(0.5)}
    print(f"""
    {"11"}|{"12"}|{"13"}
    --+--+--
    {"21"}|{"22"}|{"23"}
    --+--+-- 
    {"31"}|{"32"}|{"33"}""")
    {sleep(0.5)}

    print(f"""
    Also note that you can leave the game whenever you want, by simply inputting any one of the following phrases:
    {Quit_List}

    Enjoy! :)
        """)

# Here, we define our Quit List first
# Then, we take the names of the players
# After that, we execute the Game Rules Function

Quit_List = ["e", "E", "exit", "Exit", "q", "Q", "quit", "Quit", "l", "L", "Leave", "leave"]
Player1, Player_1, Player2, Player_2 = input("Please enter the name of Player 1: "), 0, input("Please enter the name of Player 2: "), 0
Game_Rules()

Game_Runs = 0

while True:
    
    oled_print("GAME STARTED")

    # Our Row_Col_List is an array (List within a List) which represents our 2 Dimensional Grid
    # n is the number of total moves. If n is 9, that means that no other moves can be played, and the loop breaks
    # if there is no winner defined, which is the 'winners' variable, then the match is a tie

    Row_Col_List, n, winners = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]], 0, ""

    while True:
        oled_clear()
        
        # We check which Game Run we're on
        # If its an even number game, starting from 0, then Player 1 starts First
        # Otherwise, Player 2 starts First

        # Note that we check if the Input variable returns a "lose" value
        # If it does, then the other player is automatically the winner
        
        if Game_Runs%2 == 0:
            if Inputter(Player1, "X") == "lose":
                winners = Player2
                break
            else:
                if winner("X", Player1) == Player1: 
                    winners = Player1
                    break
            n += 1
            if n == 9: break

            if Inputter(Player2, "O") == "lose":
                winners = Player1
                break
            else:
                if winner("O", Player2) == Player2: 
                    winners = Player2
                    break
            n += 1
            if n == 9: break

        # We repeat the above for if Player 2 starts first

        else:
            if Inputter(Player2, "O") == "lose":
                winners = Player1
                break
            else:
                if winner("O", Player2) == Player2: 
                    winners = Player2
                    break
            n += 1
            if n == 9: break

            if Inputter(Player1, "X") == "lose":
                winners = Player2
                break
            else:
                if winner("X", Player1) == Player1: 
                    winners = Player1
                    break
            n += 1
            if n == 9: break

    # We see that if winners is defined, and declare the winner
    # If Player 1 is the winner, we play the Buzzer
    # If Player 2 is the winner, we light up the Bulb

    if winners != "":
        oled_print(f"{winners} is the Winner!")
        if winners == Player1: 
            buzzer_frequency(5, 100) #Buzzer
            Player_1 += 1
        else:
            digital_write(4, True) # Bulb
            Player_2 += 1

    # Otherwise, the match is a tie

    else: oled_print("Match is a tie")

    # The Game Run increases by one

    Game_Runs += 1
    
    sleep(3)

    # We ask the players if they wish to play again
    # After their input, the Buzzer or Bulb stop

    x = input("Would you like to play again? Enter 'y' to continue, and any other key to exit: ")
    buzzer_stop(5)
    digital_write(4, False)

    # We check if input was NOT y
    # If it was, then we give the grand total wins
    
    if x != "y":
        oled_clear()
        oled_print(f"{Player1} won {Player_1} matches, and {Player2} won {Player_2} matches")
        sleep(5)
        oled_clear()
        if Player_1 > Player_2: oled_print(f"{Player1} won {Player_1 - Player_2} matches more than {Player2}, with a grand total of {Player_1} matches")
        elif Player_1 < Player_2: oled_print(f"{Player2} won {Player_2 - Player_1} matches more than {Player1}, with a grand total of {Player_2} matches")
        else: oled_print(f"Both players have a grand tie, with {Player_1} wins")
        sleep(5)
        oled_clear()
        oled_print("Game Exiting...")
        sleep(1)
        oled_clear()
        break