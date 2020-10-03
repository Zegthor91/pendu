import libs
class Player:
    
    def __init__(self,username="Not defined",score=0,games=0,wins=0,losses=0):
        self.username=username
        self.player_score=score
        self.games=games
        self.wins=wins
        self.losses=losses
    
    def update(self,endgame,score):
        self.player_score+=score
        self.games+=1
        if endgame==-1:
            self.losses+=1
        elif endgame==1:
            self.wins+=1
        else:
            print('Something went wrong')
        self.update_usersTable() #To Do : 
                                 #Make update at end of session
                                 #Rather than after each game

    def get_user(username):
        users=libs.pd.read_csv('database/users.csv', index_col=0)
        user=users[users['username']==username]  #To Do : Add mechanism to verify unicity of username
        if user.shape[0]==0:
            print('User not found !')
            Player.create_user(username)
            print('User has been created then.')
            return None
        else:
            return user
    get_user=staticmethod(get_user)

    def create_user(cls,username):
        users=libs.pd.read_csv('database/users.csv', index_col=0)
        newUser=libs.pd.DataFrame([[username,0,0,0,0]])
        newUser.columns=users.columns
        users=users.append(newUser, ignore_index=True)
        users.index.name='userID'
        users.to_csv('database/users.csv')
    create_user=classmethod(create_user)

    def update_usersTable(self):
        users=libs.pd.read_csv('database/users.csv', index_col=0)
        users.loc[users.username==self.username,'score']=self.player_score
        users.loc[users.username==self.username,'nb_games']=self.games
        users.loc[users.username==self.username,'wins']=self.wins
        users.loc[users.username==self.username,'losses']=self.losses
        users.index.name='userID'
        users.to_csv('database/users.csv')