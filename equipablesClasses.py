import random

class Weapon:

    #base values up to change
    critMultiplierBase = 1.5 #multiplier for crit damage (extra damage on crit)
    critChanceBase = 0.1 #crit chance decreases longer it takes for player to move
    damageConsistencyBase = 0.05 #represents deviation in damage from attack to attack from base damage
    swapSpeedBase = 1 #how fast player can swap away this weapon --> affects vulnerability to counter attack and success chance of swap+attack move (lower = faster = less vulnerable)
    blockChanceBase = 0.9 #how likely you are to succeed at blocking incomming attack. Multiplied by "bypassBlockChance" of opponent weapon for actual chance
    bypassBlockChanceBase = 1 #how much more/less likely you are to break through opponent block. See above for affects
    counterAttackChanceBase = 0.5 #how likely a counter attack is to succeed with this weapon
    avoidCounterAttackChanceBase = 1 #how resistant you are to counter attacks with this weapon. Same affects as "bypassBlockChanceBase" on "blockChanceBase" (during swap, stat comes from weapon being swapped out)

    rarityAttackMulti = {"common" : 1, "uncommon" : 1.1, "rare" : 1.3, "epic" : 1.5, "legendary" : 1.75} #multiplier for damage with weapons at different rarities. May be revisited in future for balancing
    levelMulti = 7 #multiplier for damage of weapon based on level (ie base damage * levelMulti * level). Up to change

    def __init__(self, name, rarity, level, attributes, baseDamage, critMulti, critChance, damageConsistency, swapSpeed, blockChance, bypassBlockChance, counterAttackChance, avoidCounterAttackChance): #variables: [critMulti, critChance, damageConsistency, swapSpeed, blockChance, bypassBlockChance, counterAttackChance] represent scalers for differences between weapon classes
        self.name = name #weapon name
        self.rarity = rarity #how rare weapon is. Also affects attributes (number and quality) and damage
        self.level = level #what level the weapon is. Affects damage. Player can only use weapons at or below their level
        self.attributes = attributes #special affects the weapon has on the player. 
        self.baseDamage = baseDamage #damage with "level 0," no rarity, no other modifiers. Scaled up for high levels and rarity, as well as weapon class. 
        self.critMulti = self.critMultiplierBase * critMulti
        self.critChance = self.critChanceBase * critChance
        self.damageConsistency = self.damageConsistencyBase * damageConsistency
        self.swapSpeed = self.swapSpeedBase * swapSpeed
        self.blockChance = self.blockChanceBase * blockChance
        self.bypassBlockChance = self.bypassBlockChanceBase * bypassBlockChance
        self.counterAttackChance = self.counterAttackChanceBase * counterAttackChance
        self.avoidCounterAttackChance = self.avoidCounterAttackChanceBase * avoidCounterAttackChance
    
    def _base_damage(self):
        return(self.baseDamage * self.rarityAttackMulti[self.rarity]) #return scaled damage of weapon

    def calculate_damage(self, crit=False):
        damageDeltaMulti = random.random() * self.damageConsistency + 1 #calculate random multiplier for damage within damage inconsistancy range 
        if random.randint(1,2) == 2: 
            damageDeltaMulti *= -1 #flip half of these multipliers to negative (loss in damage)

        damage = self._base_damage() * damageDeltaMulti
        