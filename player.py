import libs
class Player:
    """A class used to manage the players and their statistics
    
    Attributes
    ----------
    username: str
        Name or surname of the user. Must be unique in the local database.
    player_score: int
        Total score of the player from all his games
    wins: int
        Number of wins from all his games
    losses: int
        Number of losses from all his games

    Methods
    ----------
    update(self,endgame,score)
        Updates the player statistics (in the object)
    get_user(username)
        Retrieves the user statistics in the local database. 
    create_user(cls,username)
        Creates a new user in the database
    update_usersTable(self)
        Stores the user statistics in the local database
    """
    
    def __init__(self,username="Not defined",score=0,games=0,wins=0,losses=0):
        """
        Parameters
        ----------
        username: str
            Name or surname of the user. Must be unique in the database.
        score: int
            Total score of the player from all his games
        wins: int
            Number of wins from all his games
        losses: int
            Number of losses from all his games
        """

        self.username=username
        self.player_score=score
        self.games=games
        self.wins=wins
        self.losses=losses
    
    def update(self,endgame,score):
        """
        Updates the player statistics (in the object)

        Parameters
        ----------
        endgame: int
            The result (win or loss) of the game.
        score: int
            The score of the game (remaining guesses).
        """

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
        """
            Retrieves the user statistics in the local database. 

        Static Method.
        Parameters
        ----------

        username: str
            Name or surname of the user
        """

        users=libs.pd.read_csv('database/users.csv', index_col=0)
        user=users[users['username']==username]  #To Do : Add mechanism to verify unicity of username
        if user.shape[0]==0:
            print('User not found !')
            Player.create_user(username)
            print('User has been created then.')
            return None
        else:
            user.drop
            return user #Be careful returns DataFrame !!!
    get_user=staticmethod(get_user)

    def create_user(cls,username):
        """
        Creates a new user in the database

        Parameters
        ----------
        username: str
        """

        users=libs.pd.read_csv('database/users.csv', index_col=0)
        newUser=libs.pd.DataFrame([[username,0,0,0,0]])
        newUser.columns=users.columns
        users=users.append(newUser, ignore_index=True)
        users.index.name='userID'
        users.to_csv('database/users.csv')
    create_user=classmethod(create_user)

    def update_usersTable(self):
        """
        Stores the user statistics in the local database
        """

        users=libs.pd.read_csv('database/users.csv', index_col=0)
        print('username:', self.username)
        print('username:', str(self.username))
        print(users)
        users.loc[users['username']==str(self.username),'score']=self.player_score
        users.loc[users['username']==str(self.username),'nb_games']=self.games
        users.loc[users['username']==str(self.username),'wins']=self.wins
        users.loc[users['username']==str(self.username),'losses']=self.losses
        users.index.name='userID'
        users.to_csv('database/users.csv')