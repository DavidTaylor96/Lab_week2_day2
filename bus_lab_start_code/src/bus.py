class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passangers = []
      
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
      return len(self.passangers)

    def pick_up(self, person):
      self.passangers.append(person)
      
    def drop_off(self, person):
      self.passangers.remove(person)

    def empty(self):
      self.passangers = []

    # def max_capacity(self, bus_stop):
    #   for person in bus_stop.queue_count:
    #     if queue_count >= 10:
    #       return "Sorry, to many people"
    #     elif queue_count == 8:
    #       return queue_count

    def pick_up_from_stop(self, bus_stop):
      for person in bus_stop.queue_count:
        self.pick_up(person)
     # We nailed it :)
