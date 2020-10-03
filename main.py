import player
import data
import game
import libs

print('Welcome to the Hangman !')
print('What \'s your username ?')
username=input()
user=player.Player.get_user(username)
if user is not None:
    player1=player.Player(user.username,user.score,user.nb_games,
    user.wins, user.losses)
else:
    player1=player.Player(username)
print('Do you want to start playing ?')
play=int(input())
libs.random.seed()
while(play!=0):
    index=libs.random.randint(0,29) #Size of dictionary hardcoded. Should evolve
    hidden_word=data.Data(data.Data.get_word(index))
    #print('Debug: ', hidden_word.word)
    current_game=game.Game(player1,hidden_word)
    current_game.data.display()
    while(current_game.endgame==0):
        guess=current_game.get_guess()
        current_game.check_guess(guess)
    print('Do you want to keep playing ?')
    play=int(input())
print('Game Over')