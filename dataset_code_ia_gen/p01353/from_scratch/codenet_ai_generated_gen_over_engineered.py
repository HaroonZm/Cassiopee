class Character:
    def __init__(self, hp: int, atk: int, defense: int, speed: int, is_hero: bool = False):
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.speed = speed
        self.is_hero = is_hero
    
    def damage_to(self, other: 'Character') -> int:
        return max(self.atk - other.defense, 0)
    
    def receive_damage(self, dmg: int) -> None:
        self.hp -= dmg
    
    def is_alive(self) -> bool:
        return self.hp > 0

class Battle:
    def __init__(self, hero: Character, enemies: list[Character]):
        self.hero = hero
        self.enemies = enemies
        self.characters = [hero] + enemies
        # Sort by speed descending for turn order
        self.characters.sort(key=lambda c: c.speed, reverse=True)
    
    def alive_enemies(self):
        return [e for e in self.enemies if e.is_alive()]
    
    def simulate_attack(self, attacker: Character, target: Character):
        damage = attacker.damage_to(target)
        target.receive_damage(damage)
        return damage
    
    def is_hero_alive(self) -> bool:
        return self.hero.is_alive()
    
    def are_all_enemies_dead(self) -> bool:
        return all(not e.is_alive() for e in self.enemies)
    
    def total_damage_to_hero(self) -> int:
        return self.hero.max_hp - self.hero.hp
    
    def run_with_strategy(self, target_selector) -> int:
        """Run the battle simulation with a strategy for hero target selection.
        target_selector: function(List[Character]) -> Character: receives alive enemies, returns one to attack.
        Returns total damage received by hero if hero survives, else -1."""
        # Reset HP
        for c in self.characters:
            c.hp = c.max_hp
        
        while self.is_hero_alive() and not self.are_all_enemies_dead():
            for c in self.characters:
                if not c.is_alive():
                    continue
                if c.is_hero:
                    # Hero selects enemy to attack this turn using given strategy
                    alive = self.alive_enemies()
                    if not alive:
                        break
                    target = target_selector(alive, self.hero)
                    self.simulate_attack(c, target)
                else:
                    # Enemy attacks hero
                    if not self.hero.is_alive():
                        break
                    self.simulate_attack(c, self.hero)
            # Exit conditions checked again at loop start
        
        return self.total_damage_to_hero() if self.is_hero_alive() else -1

class Strategy:
    def __init__(self, hero: Character, enemies: list[Character]):
        self.hero = hero
        self.enemies = enemies
    
    def heuristic(self, enemy: Character) -> float:
        # Define a heuristic to prioritize which enemy to attack
        # Prioritize enemies that deal highest damage to hero normalized by speed and hp
        dmg = enemy.damage_to(self.hero)
        # Weight by speed and hp to balance survivability
        return dmg / (enemy.hp * enemy.speed)
    
    def choose_target(self, alive_enemies: list[Character], hero: Character) -> Character:
        # For the problem, choose enemy with maximum damage-to-hero / (hp * speed)
        # The idea is to reduce the most dangerous enemies fastest to reduce damage intake
        return max(alive_enemies, key=self.heuristic)

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    hero_stats = list(map(int, input().split()))
    hero = Character(*hero_stats, is_hero=True)
    enemies = []
    for _ in range(n):
        e_stats = list(map(int, input().split()))
        enemies.append(Character(*e_stats))
    
    battle = Battle(hero, enemies)
    strategy = Strategy(hero, enemies)
    
    # Run a simulation with the heuristic strategy and get minimal damage hero takes
    result = battle.run_with_strategy(strategy.choose_target)
    print(result)

if __name__ == "__main__":
    main()