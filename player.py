
class Player:

    baseLevelXp = 100
    levelXpMulti = 5

    def __init__(self):
        self.health = 100 #not sure if health should be here or in different variable in a separate "fight" class/enviroment
        self.gold = 0 #currency name up to change, "gold" for now
        self.level = 1 
        self.xp = 0

    def xp_gain(self, amount):
        #control level-up logic
        self.xp += amount
        while self.xp >= self._xp_level_limit():
            self.xp -= self._xp_level_limit()
            self.level += 1
            self._on_level()

    def _on_level(self):
        #level reward, possibly game overlay
        pass

    def _xp_level_limit(self):
        #returns xp needed for next level (exponential scale)
        return(self.baseLevelXp * self.levelXpMulti**(self.level - 1))