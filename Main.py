from BattleGround import *
from Minion import *
from Player import *

if __name__ == "__main__":
  player1 = Player("Alice")
  player2 = Player("Bob")

  player1.minions = [Imprisoner(deathrattle_order=0)]
  player2.minions = [Harmless_Bonehead(deathrattle_order=1), Harmless_Bonehead(deathrattle_order=1), Harmless_Bonehead(deathrattle_order=1), Harmless_Bonehead(deathrattle_order=1), Harmless_Bonehead(deathrattle_order=1)]

  battleground = BattleGround(player1, player2)
  battleground.battle()
  winner = battleground.get_winner()
  print(f"The winner is {winner}")
