NONE_TYPE = 0
MECH_TYPE = 1
UNDEAD_TYPE = 2
DRAGON_TYPE = 3
DEMON_TYPE = 4


class Minion:
  def __init__(self, name, type, taunt, divine_shield, deathrattle, deathrattle_order, battlecry,
               reborn, turn_start_event, turn_end_event, sell_event, in_turn_event, blood, attack):
    self.name = name
    self.type = type
    self.taunt = taunt
    self.divine_shield = divine_shield
    self.deathrattle = deathrattle
    self.deathrattle_order = deathrattle_order
    self.battlecry = battlecry
    self.reborn = reborn
    self.turn_start_event = turn_start_event
    self.turn_end_event = turn_end_event
    self.sell_event = sell_event
    self.in_turn_event = in_turn_event
    self.attack = attack
    self.blood = blood

  def __repr__(self):
    return f"{self.name} (Attack: {self.attack}, Blood: {self.blood})"


class Annoy_o_Tron(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Annoy_o_Tron", type=MECH_TYPE, taunt=True, divine_shield=True,
                     deathrattle=None, battlecry=None, reborn=False, turn_start_event=None,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=1, blood=2,
                     deathrattle_order=deathrattle_order)


class Beleaguered_Battler(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Beleaguered_Battler", type=NONE_TYPE, taunt=False,
                     divine_shield=False,
                     deathrattle=None, battlecry=None, reborn=False,
                     turn_start_event=self.start_of_turn,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=4, blood=5,
                     deathrattle_order=deathrattle_order)

  def start_of_turn(self):
    if self.attack > 0:
      self.attack -= 1
      print(f"{self.name} has lost 1 attack, new attack value: {self.attack}")
    else:
      print(f"{self.name} cannot lose more attack, attack is already at {self.attack}")


class Harmless_Bonehead(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Harmless_Bonehead", type=UNDEAD_TYPE, taunt=False,
                     divine_shield=False,
                     deathrattle=[self.harmless_bonehead], battlecry=None, reborn=False,
                     turn_start_event=None,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=0, blood=2,
                     deathrattle_order=deathrattle_order)

  def harmless_bonehead(self, player, position, death_list):
    if len(player.minions) <= 5 + len(death_list):
      sk1 = Skeleton()
      sk2 = Skeleton()
      player.add_minion(sk1, position)
      player.add_minion(sk2, position + 1)
    elif len(player.minions) == 6 + len(death_list):
      sk = Skeleton()
      player.add_minion(sk, position)


class Skeleton(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Skeleton", type=UNDEAD_TYPE, taunt=False,
                     divine_shield=False,
                     deathrattle=[], battlecry=None, reborn=False,
                     turn_start_event=None,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=1, blood=1,
                     deathrattle_order=deathrattle_order)


class Emrald_Proto_Whelp(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Emrald_Proto_Whelp", type=DRAGON_TYPE, taunt=False,
                     divine_shield=False,
                     deathrattle=[], battlecry=None, reborn=False,
                     turn_start_event=None,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=0, blood=4,
                     deathrattle_order=deathrattle_order)


class Imprisoner(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Imprisoner", type=DEMON_TYPE, taunt=True,
                     divine_shield=False,
                     deathrattle=[self.imprisoner], battlecry=None, reborn=False,
                     turn_start_event=None,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=3, blood=2,
                     deathrattle_order=deathrattle_order)

  def imprisoner(self, player, position, death_list):
    if len(player.minions) <= 6 + len(death_list):
      player.add_minion(Imp(), position)


class Imp(Minion):
  def __init__(self, deathrattle_order=0):
    super().__init__(name="Imp", type=DEMON_TYPE, taunt=False,
                     divine_shield=False,
                     deathrattle=[], battlecry=None, reborn=False,
                     turn_start_event=None,
                     turn_end_event=None, sell_event=None, in_turn_event=None, attack=1, blood=1,
                     deathrattle_order=deathrattle_order)

