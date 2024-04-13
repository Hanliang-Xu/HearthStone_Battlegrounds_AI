class Player:
  def __init__(self, name):
    self.name = name
    self.minions = []
    self.death_rattle_order = []

  def is_all_dead(self):
    return all(minion.blood <= 0 for minion in self.minions)

  def is_all_no_attack(self):
    return all(minion.attack <= 0 for minion in self.minions)

  def add_minion(self, minion, position=None):
    """Add a minion at a specified position. If no position is specified, add to the end."""
    if position is None or position >= len(self.minions):
      self.minions.append(minion)
    else:
      self.minions.insert(position, minion)
    print(f"Added {minion.name} at position {position if position is not None else 'end'}")

  def remove_minion_at(self, position):
    """Remove a minion at a specified position, if the position is valid."""
    if 0 <= position < len(self.minions):
      removed_minion = self.minions.pop(position)
      print(f"Removed {removed_minion.name} from position {position}")
      return removed_minion
    else:
      print(f"No minion at position {position} to remove")
      return None

  def display_minions(self):
    """Utility method to display current state of minions."""
    if not self.minions:
      print(f"{self.name} has no minions.")
    else:
      print(f"{self.name}'s minions: {[minion.name for minion in self.minions]}")
