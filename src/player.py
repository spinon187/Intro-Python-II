# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
  def __init__(self, current_room):
    self.current_room = current_room
    self.items = []
  def take_item(self, item):
    self.items.append(item)
  def view_inventory(self):
    for i in self.items:
      print(i)
  def drop_item(self, item):
    self.items.remove(item)
  def change_room(self, new_room):
    self.current_room = new_room
    print('\nLocation: ' + self.current_room.name)
    print(self.current_room.description)