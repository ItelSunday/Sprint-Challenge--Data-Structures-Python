class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    #relace element to current index with item
    self.current += 1 
    #set it back to the beginning
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    return [i for i in self.storage if i !=None]