import player
import data
class Game:

    def __init__(self,player,data,score=8):
        self.player=player
        self.data=data
        self.game_score=score
        self.endgame=0
        print('Game Started')
        print('='*20)

    def get_guess(self):
        print('What\'s your guess ?')
        guess=input() #Create a function to check quality
                        #To prevent bad inputs
                        #But also to check that same is not entered twice to protect self.revealed
        self.data.update(guess)
        return guess
    
    def check_guess(self, guess):
        if(self.data.update(guess)):
            guessed=True
        else:
            self.game_score-=1
            guessed=False
        self.data.display()
        self.check_endgame(guessed)

    def check_endgame(self,guessed): #Check is different depending on if the last coup was winning or not
        if(guessed):
            if(len(self.data.revealed)==len(set(self.data.word))):
                self.endgame=1
                print('Congratulations you won with a score of ', self.game_score, ' !')
        else:
            if(self.game_score==0):
                self.endgame=-1
                print('Sorry you lost !')

