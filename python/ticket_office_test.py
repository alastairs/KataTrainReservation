import random
import unittest
from ticket_office import BookingService

class TestBookingService(unittest.TestCase):
  def setUp(self):
    pass

  def test_provides_reference(self):
    self.assertTrue("booking_reference" in BookingService().reserve("test_train", "4"))
    

if __name__ == '__main__':
    unittest.main()
