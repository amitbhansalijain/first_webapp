

import random



class Enemy():


    def __init__(self,name='Enemy',hit_point=0,lives=2):
        self.name=name
        self.hit_point=hit_point
        self.lives=True
    
    def take_damage(self,damage):
        remaining_point= self.hit_point - damage
        if remaining_point >= 0 :
            self.hit_point = remaining_point
            print(f' i took  bullet  {damage} point damage , my reamainng point is {remaining_point}')
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f'{self.name} lost lifa')
            
            else:
                print('aoooo aoooo i died')
                self.lives=False
    

    def __str__(self):return f'Enemy name:{self.name} Enemy lives:{self.lives} Enemy hit_point: {self.hit_point} '
    

class Bone_snacher(Enemy):
    
    def __init__(self, name):
        super().__init__(name=name,lives=1,hit_point=23)


    def snatch(self):
        return f' i am {self.name}, i just snatch your bone'
    
    



class Blod_drinker(Enemy):
    
    def __init__(self, name):
        super().__init__(name=name,lives=3,hit_point=24)

    def skipped(self):
        if random.randint(1,5)==5:
            print(f'******{self.name} i duked ,and saved')
            return True
        
        else:
            return False
        


        
    def take_damage(self,damage):
        if not self.skipped():
            super().take_damage(damage=damage)


class kingBlooddrinker(Blod_drinker):

    def __init__(self, name):
        super().__init__(name)
        self.hit_point=150


    def take_damage(self, damage):
        super().take_damage(damage//4)


