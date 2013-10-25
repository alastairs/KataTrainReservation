import random
import unittest
from ticket_office import BookingService

class TestBookingService(unittest.TestCase):
  def setUp(self):
    pass

  def test_provides_reference(self):
    assert "booking_reference" in BookingService().reserve("test_train", "4")
  
  def test_provides_non_empty_reference_with_valid_reservation(self):
    bs = BookingService()
    train_data = {
      "seats": { 
        "1A" : {
          "booking_reference": "",
          "coach": "A",
          "seat_number":"1"
        }
      }
    }
    assert bs.reserve_on_train(train_data, 1)["booking_reference"]

  def test_does_not_provide_reference_with_invalid_reservation(self):
    bs = BookingService()
    train_data = {
      "seats": { 
        "1A" : {
          "booking_reference": "",
          "coach": "A",
          "seat_number":"1"
        }
      }
    }
    assert not bs.reserve_on_train(train_data, 2)["booking_reference"]

if __name__ == '__main__':
    unittest.main()
