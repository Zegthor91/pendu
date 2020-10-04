import player
import data
import libs
class Game:
    def __init__(self,player,data,score=8):
        self.player=player
        self.data=data
        self.game_score=score
        self.endgame=0
        print('Game Started')
        print('='*20)

    def get_guess(self): 
        sanity=False
        while(not(sanity)):
            print('What\'s your guess ?')
            guess=input().lower() 
            sanity=self.guess_sanitycheck(guess)
        return guess

    def guess_sanitycheck(self,guess):
        sanity=True
        if (not(guess.isalpha())):
            print('You have entered a bad characther')
            sanity=False
        if guess in self.data.revealed:
            print('You have already guessed that letter')
            sanity=False
        if guess in self.data.mistakes:
            print('You have already made that mistake')
            sanity=False
        return sanity
  
    def check_guess(self, guess):
        if(self.data.update(guess)):
            guessed=True
        else:
            self.game_score-=1
            guessed=False
        self.data.display()
        self.check_endgame(guessed)

    def check_endgame(self,guessed): 
        if(guessed):#Check is different depending on if the last coup was winning or not
            if(len(set(self.data.revealed))==len(set(self.data.word))):
                self.endgame=1
                # self.player.games+=1
                # self.player.player_score+=self.game_score
                self.player.update(self.endgame,self.game_score) #Update player statistics
                self.update_gamesTable() #Update games dabatabase
                print('Congratulations you won with a score of ', self.game_score, ' !')
        else:
            if(self.game_score==0):
                self.endgame=-1
                #self.player.games+=1
                self.player.update(self.endgame,self.game_score) #Update player statistics
                self.update_gamesTable() #Update games table
                print('Sorry you lost !')
                print('The word was : ') # Make optional eventually
                self.data.reveal_word()
        #self.player.update(self.endgame,self.game_score) #Update player statistics
        return self.endgame

    def update_gamesTable(self):
        games=libs.pd.read_csv('database/games.csv', index_col=0)
        newGame=libs.pd.DataFrame([[
            self.player.username,
            self.data.word,
            self.endgame,
            self.game_score
        ]])
        newGame.columns=games.columns
        games=games.append(newGame, ignore_index=True)
        games.index.name='gameID'
        games.to_csv('database/games.csv')

