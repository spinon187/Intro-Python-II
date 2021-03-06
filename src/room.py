# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []
    self.n_to = None
    self.w_to = None
    self.s_to = None
    self.e_to = None
  def add_item(self, item):
    self.items.append(item)
  def view_items(self):
    for i in self.items:
      print('You see ' + i.display_name)
  def remove_item(self, item):
    self.items.remove(item)
  def item_check(self, item):
    for i in self.items:
      if i.name == item:
        return i
      

