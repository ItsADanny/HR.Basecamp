from carparking import *
from datetime import datetime, timedelta

# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    # Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    # Test for checking the correct parking fees
def test_parking_fee():
    # Assert that parking time 2h10m, gives correct parking fee
    # Assert that parking time 24h, gives correct parking fee
    # Assert that parking time 30h == 24h max, gives correct parking fee

# Test for validating check-out behaviour
def test_check_out():
    # Assert that {license_plate} is in parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    # Aseert that {license_plate} is no longer in parked_cars