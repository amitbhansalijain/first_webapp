
import random

class Enemy():



    def __init__(self,name='Enemy',lives=1,hit_point=0):
        self.name=name
        self.hit_point=hit_point
        self.lives=True


    def take_damge(self,damage):
        remaining_point=self.hit_point - damage
        if remaining_point > 0:
            self.hit_point = remaining_point
            print(f'i took bullet {damage} damage ,my remaining point is {remaining_point}')
        
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f'{self.name} is lost life')

            else:
                print('arggrrr i diesd')
                self.lives = False



    def __str__(self): return f'enemy name is {self.name} enemy lives is {self.lives} remaining hitpoint is {self.hit_point}'


class Blood_Drinker(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_point=24)



    def snatch(self):
        return f'i {self.name} just snatch your bone'
    

class Bone_snacher(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_point=50)



    def ducked(self):
        if random.randint(1,5)==5:
            print(f'****.{self.name} i ducked and save')
            return True
        

        else:
            return False
        

    def take_damge(self, damage):
        if not self.ducked():
            super().take_damge(damage=damage)



class King_enemy(Bone_snacher):

    def __init__(self, name):
        super().__init__(name)
        self.hit_point=150

    def take_damge(self, damage):
        return super().take_damge(damage//4)

          

    

        



