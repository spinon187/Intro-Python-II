# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
  def __init__(self, room):
    self.room = room
    self.items = []
  def take_item(self, item):
    self.items.append(item)
  def view_inventory(self):
    for i in self.items:
      print(i)
  def drop_item(self, item):
    self.items.remove(item)