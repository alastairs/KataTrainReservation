import random
import unittest
from ticket_office import BookingService, BookingReferenceServiceClient




class TestBookingService(unittest.TestCase):
  def setUp(self):
    self.booking_service = BookingService(BookingReferenceServiceClient())
    pass

  def test_provides_booking_reference(self):
    assert "booking_reference" in self.booking_service.reserve("test_train", "4")
  
  def test_provides_non_empty_booking_reference_with_valid_reservation(self):
    train_data = TrainDataBuilder().with_seats(
      { "1A" : SeatBuilder()
                .with_coach("A")
                .with_seat_number("1").build() }
    ).build()
    
    assert self.booking_service.reserve_on_train(train_data, 1)["booking_reference"]

  def test_does_not_provide_booking_reference_with_invalid_reservation(self):
    train_data = TrainDataBuilder().with_seats(
      { "1A" : SeatBuilder()
                .with_coach("A")
                .with_seat_number("1").build() }
    ).build();
    
    assert not self.booking_service.reserve_on_train(train_data, 2)["booking_reference"]
  


class SeatBuilder(object):
  def __init__(self):
    self.booking_reference = ""
    self.coach = ""
    self.seat_number = ""

  def with_coach(self, new_coach):
    self.coach = new_coach
    return self

  def with_seat_number(self, new_seat_number):
    self.seat_number = new_seat_number
    return self

  def build(self):
    return {
      "booking_reference": self.booking_reference,
      "coach": self.coach,
      "seat_number": self.seat_number
    }

class TrainDataBuilder(object):
 
  def with_seats(self, seats):
    self.seats = seats
    return self

  def build(self):
    return {
      "seats": self.seats 
    }

if __name__ == '__main__':
    unittest.main()
