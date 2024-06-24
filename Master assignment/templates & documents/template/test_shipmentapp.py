from vessel import Vessel
from shipment import Shipment


# Test to check if duration is converted correctly based on the given arguments
# 1) %D:%H:%M
# 2) %H:%M
def test_convert_duration():
    raise NotImplemented()


# Test to check if distance is converted correctly based on the given arguments
# 1) NM = Nautical Meters
# 2) M = Meters
# 3) KM = Kilometers
# 4) MI = Miles
# 5) YD = Yards
# 6) ValueError check
def test_convert_distance():
    raise NotImplemented()


# Test to check if speed is converted correctly based on the given arguments
# 1) Knts = Knots
# 2) Mph = Miles per hour
# 3) Kph = Kilometers per hour
# 4) ValueError check
def test_convert_speed():
    raise NotImplemented()


# Test to check if the fuel consumption is calculated correctly based on the distance
def test_get_fuel_consupmtion():
    raise NotImplemented()


# Test to check if the fuel costs are calculated correctly based on the price per liter
def test_calculate_fuel_costs():
    raise NotImplemented()


# Test to check if the returned ports are correct
# 1) amount check
# 2) keys check
# 3) values check
def test_get_ports():
    raise NotImplemented()


# Test if the returned shipments contain the required shipment(s)
def test_get_shipments():
    raise NotImplemented()
