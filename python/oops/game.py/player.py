
class fozi():

    def __init__(self,name):
        self.name= name
        self._lives=3
        self.level=1
        self.score=0


    def _get_lives(self):
        return self._lives
    

    def _set_lives(self,lives):

        if lives >= 0:
            self._lives = lives

        else:
            print('live cant below zero')
            self._lives = 0
            
    lives = property(_set_lives,_get_lives)


    def __str__(self):
        return f'Nmae:{self.name}, lives:{self._lives},Score:{self.score},Level:{self.level}'




# class Player():

#     def __init__(self,name):
#         self.name=name
#         self._lives=3
#         self._level=1
#         self.score=0

#     def _get_lives(self):
#         return self._lives
    
#     def _set_lives(self,lives):
#          if lives >=0 :
#              self._lives =lives
#          else:
#             print('lives cant be below zero')
#             self._lives = 0
    
            
#     lives = property(_set_lives,_get_lives)

#     def __str__(self):
#          return f'Name : {self.name},Lives:{self.lives},Level:{self._level},Score:{self.score}'
    




    
