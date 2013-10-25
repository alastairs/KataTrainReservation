import json

class BookingService(object):
  def reserve_on_train(self, train_data, seat_count):
    if seat_count > 1:
      return {"booking_reference": ""}
    return {
      "booking_reference": "75bcd15"
    }
  def reserve(self, train_id, seat_count):
    return {
      "train_id": train_id,
      "seats": ["1A", "2A", "3A", "4A"],
      "booking_reference": "75bcd15"
    }

class TicketOffice(object):
    def __init__(self):
      self.bookingService = BookingService()
    def reserve(self, train_id, seat_count):
        return json.dumps(self.bookingService.reserve(train_id,seat_count))

if __name__ == "__main__":
    """Deploy this class as a web service using CherryPy"""
    import cherrypy
    TicketOffice.reserve.exposed = True
    cherrypy.config.update({"server.socket_port" : 8083})
    cherrypy.quickstart(TicketOffice())
