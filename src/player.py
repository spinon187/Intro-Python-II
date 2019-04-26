# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
  def __init__(self, current_room):
    self.current_room = current_room
    self.items = []
  def take_item(self, item):
    self.items.append(item)
    self.current_room.remove_item(item)
  def view_inventory(self):
    for i in self.items:
      print(i.name)
  def drop_item(self, item):
    self.items.remove(item)
    self.current_room.items.append(item)
  def change_room(self, new_room):
    self.current_room = new_room
    print('\nLocation: ' + self.current_room.name)
    print(self.current_room.description)
  def item_check(self, item):
    for i in self.items:
      if i.name == item:
        return i