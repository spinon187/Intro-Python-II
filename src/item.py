class Item():
  def __init__(self, name, description, display_name):
    self.name = name
    self.description = description
    self.display_name = display_name
  def inspect(self):
    print(self.description)