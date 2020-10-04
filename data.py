import libs
class Data:
    """A class used to manage the words and their display
    
    Attributes
    ----------
    word: str
        The word that needs to be guessed during a game
    isGuessed: bool
        A Boolean indicating if the world has been guessed during a game or not (Not really used for now)
    revealed: [str]
        List containing the letters that have been guessed
    mistakes: [str]
        List containing the letters that I have been wrongly proposed
    size: int
        Length of the word

    Methods
    ----------
    display(self)
        Prints the world with '_' for the hidden letters while displaying the revealed letters
    update(self,guess)
        Updates revealed and mistakes depending on if the guess is correct or not
    reveal_word(self)
        Displays the full word
    get_word(index)
        Retrieves a word in the dictionary
     """

    def __init__(self,word,isGuessed=False):
        """
        Parameters
        ----------
        word: str
            The word to be guessed
        isGuessed:Bool
            Boolean indicating if the word has been guessed or not (default is False)
        """
        self.word=word
        self.isGuessed=isGuessed
        self.revealed=[]
        self.mistakes=[]
        self.size=len(word)
    
    def __len__(self):
        return len(self.word)

    def display(self):
        """
        Display the world in the console

        Prints the world with '_' for the hidden letters while displaying the revealed letters
        """

        hidden_word='-'*self.size
        for i,letter in enumerate(self.word):
            if letter in self.revealed:
                temp=list(hidden_word)
                temp[i]=letter
                hidden_word=''.join(temp)
        print(hidden_word)

    def update(self,guess):
        """
        Updates revealed and mistakes depending on if the guess is correct or not

        Parameters
        ----------
        guess: str
        Tentative guess from the user
        """

        #print('Update') #For debug purposes
        if guess in self.word:
            self.revealed.append(guess)
            return True
        else:
            self.mistakes.append(guess)
            return False
    
    def reveal_word(self):
        """
        Displays the full word
        """

        print(self.word)

    def get_word(index):
        """
        Retrieves a word in the dictionary

        Parameters
        ----------
        index: int
        Position of the word to be retrieved in the dictionary
        """
        with open('dictionary.txt','r') as dictionary_file:
            dictionary =dictionary_file.readlines()
            return dictionary[index][:len(dictionary[index])-1] #the output string of readlines contain /n that needs to be removed
    get_word=staticmethod(get_word)



