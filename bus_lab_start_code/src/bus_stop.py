class BusStop:
  def __init__(self, name):
    self.name = name
    self.queue_count = []


  def queue_length(self):
    return len(self.queue_count)

  def add_to_queue(self, person):
    self.queue_count.append(person)

  def clear(self):
    self.queue_count = []