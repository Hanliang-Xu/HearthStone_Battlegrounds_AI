import copy
import random


class BattleGround:
  def __init__(self, player1, player2):
    self.original_players = [player1, player2]
    self.players = copy.deepcopy([player1, player2])  # Deep copy players for the battle simulation
    if len(self.players[0].minions) > len(self.players[1].minions):
      self.current_attacker = 0
      self.current_defender = 1
    elif len(self.players[0].minions) < len(self.players[1].minions):
      self.current_attacker = 1
      self.current_defender = 0
    else:
      self.current_attacker = random.randint(0, 1)
      self.current_defender = 1 - self.current_attacker

  def battle(self):
    while not ((any(player.is_all_dead() for player in self.players)) or (all(player.is_all_no_attack() for player in self.players))):
      attack_minion = 0  # First minion in the list attacks
      defend_minion = self.determine_defend_minion()
      print(
        f"Attacking minion (Player {self.current_attacker + 1}) attacks defending minion (Player {self.current_defender + 1}) at index {defend_minion}")
      if (self.players[self.current_attacker].minions[attack_minion].attack > 0):
        self.single_attack(attack_minion, defend_minion)
        self.update_death()
      self.switch_turns()

  def determine_defend_minion(self):
    taunt_minions = [minion for minion in self.players[self.current_defender].minions if
                     minion.taunt]
    if taunt_minions:
      chosen_minion = random.choice(taunt_minions)
      return self.players[self.current_defender].minions.index(chosen_minion)
    else:
      chosen_minion = random.choice(self.players[self.current_defender].minions)
      return self.players[self.current_defender].minions.index(chosen_minion)

  def single_attack(self, attack_minion_index, defend_minion_index):
    attacker = self.players[self.current_attacker].minions[attack_minion_index]
    defender = self.players[self.current_defender].minions[defend_minion_index]

    print(f"Minion {attacker.name} attacks {defender.name}")

    if attacker.divine_shield and defender.divine_shield:
      if defender.attack > 0:
        attacker.divine_shield = False
      defender.divine_shield = False
      print("Both divine shields are removed.")
    elif attacker.divine_shield:
      if defender.attack > 0:
        attacker.divine_shield = False
      defender.blood -= attacker.attack
      print(f"{defender.name} takes {attacker.attack} damage, remaining blood: {defender.blood}")
    elif defender.divine_shield:
      defender.divine_shield = False
      attacker.blood -= defender.attack
      print(
          f"{attacker.name} attacks but {defender.name} has divine shield. {attacker.name} takes {defender.attack} damage, remaining blood: {attacker.blood}")
    else:
      attacker.blood -= defender.attack
      defender.blood -= attacker.attack
      print(
          f"{attacker.name} and {defender.name} both take damage. Remaining blood: {attacker.name}: {attacker.blood}, {defender.name}: {defender.blood}")

  def update_death(self):
    # Collect dead minions along with their indices for both attacker and defender
    attacker_deaths = [(index, minion) for index, minion in
                       enumerate(self.players[self.current_attacker].minions) if
                       minion.blood <= 0]
    defender_deaths = [(index, minion) for index, minion in
                       enumerate(self.players[self.current_defender].minions) if
                       minion.blood <= 0]

    # Handle deathrattles in order specified in deathrattle_order
    self.handle_deathrattles(attacker_deaths, self.players[self.current_attacker])
    self.handle_deathrattles(defender_deaths, self.players[self.current_defender])

  def handle_deathrattles(self, death_list, player):
    # Sort the dead minions by the player's deathrattle_order
    death_list.sort(key=lambda x: player.death_rattle_order.index(x[1]) if x[
                                                                             1] in player.death_rattle_order else len(
      player.death_rattle_order))

    # Iterate through the sorted list of dead minions
    for index, minion in death_list:
      if minion.deathrattle:
        # Call the deathrattle function - assuming it's a callable attached to the minion
        print(f"Processing deathrattle for {minion.name} at index {index}")
        for deathrattle_function in minion.deathrattle:
          deathrattle_function(player, index + 1, death_list)  # Execute the callable function
          print(f"Executed {deathrattle_function.__name__} for {minion.name}")

      # Remove the minion after processing deathrattle
      player.remove_minion_at(index)

  def switch_turns(self):
    self.current_attacker, self.current_defender = self.current_defender, self.current_attacker

  def get_winner(self):
    if self.players[0].is_all_dead():
      return self.players[1].name
    if self.players[1].is_all_dead():
      return self.players[0].name
    return "No winner yet"
