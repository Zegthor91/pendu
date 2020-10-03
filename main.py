import player
import data
import game
import libs

print('Welcome to the Pendu Game !')
print('What \'s your username ?')
username=input()

player1=player.Player(username)
print('Do you want to start playing ?')
play=int(input())
libs.random.seed()
nb_games=0
while(play!=0):
    index=libs.random.randint(0,15) #Size of dictionary hardcoded. Should evolve
    revealed=[]
    hidden_word=data.Data(data.Data.get_word(index),revealed)
    #print('Debug: ', hidden_word.word)
    current_game=game.Game(player,hidden_word)
    current_game.data.display()
    while(current_game.endgame==0):
        guess=current_game.get_guess()
        current_game.check_guess(guess)
    print('Do you want to keep playing ?')
    play=int(input())
    nb_games+=1
print('Game Over')