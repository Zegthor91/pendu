import libs
class Data:

    def __init__(self,word,isGuessed=False):
        self.word=word
        self.isGuessed=isGuessed
        self.revealed=[]
        self.mistakes=[]
        self.size=len(word)
    
    def __len__(self):
        return len(self.word)

    def display(self):
        hidden_word='-'*self.size
        for i,letter in enumerate(self.word):
            if letter in self.revealed:
                temp=list(hidden_word)
                temp[i]=letter
                hidden_word=''.join(temp)
        print(hidden_word)

    def update(self,guess):
        #print('Update') #For debug purposes
        if guess in self.word:
            self.revealed.append(guess)
            return True
        else:
            self.mistakes.append(guess)
            return False
    
    def reveal_word(self):
        print(self.word)

    def get_word(index):
        with open('dictionary.txt','r') as dictionary_file:
            dictionary =dictionary_file.readlines()
            return dictionary[index][:len(dictionary[index])-1] #the output string of readlines contain /n that needs to be removed
    get_word=staticmethod(get_word)



