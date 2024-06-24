from vessel import Vessel
from shipment import Shipment


# Test to check if duration is converted correctly based on the given arguments
# 1) %D:%H:%M
# 2) %H:%M
def test_convert_duration():
    test_shipment = Shipment("11FD3D5D-C403-403D-B33A-2E17C1893AA4", "01-01-2023", 54311,
                             4555597, 813499, 5.6, "JPYOS", "BDCHL", 9934838)
    assert test_shipment.convert_duration("%D:%H:%M") == "33895:226:48809"
    assert test_shipment.convert_duration("%H:%M") == "226:48809"


# Test to check if distance is converted correctly based on the given arguments
# 1) NM = Nautical Meters
# 2) M = Meters
# 3) KM = Kilometers
# 4) MI = Miles
# 5) YD = Yards
# 6) ValueError check
def test_convert_distance():
    test_shipment = Shipment("11FD3D5D-C403-403D-B33A-2E17C1893AA4", "01-01-2023", 54311,
                             4555597, 813499, 5.6, "JPYOS", "BDCHL", 9934838)
    pass


# Test to check if speed is converted correctly based on the given arguments
# 1) Knts = Knots
# 2) Mph = Miles per hour
# 3) Kph = Kilometers per hour
# 4) ValueError check
def test_convert_speed():
    test_shipment = Shipment("11FD3D5D-C403-403D-B33A-2E17C1893AA4", "01-01-2023", 54311,
                             4555597, 813499, 5.6, "JPYOS", "BDCHL", 9934838)
    pass


# Test to check if the fuel consumption is calculated correctly based on the distance
def test_get_fuel_consupmtion():
    test_vessel = Vessel(9934838, 352001435, "AQUARUBY", "Panama", "Bulk Carrier", 2022,
                         44175, 82015, 229, 32)
    pass


# Test to check if the fuel costs are calculated correctly based on the price per liter
def test_calculate_fuel_costs():
    pass


# Test to check if the returned ports are correct
# 1) amount check
# 2) keys check
# 3) values check
def test_get_ports():
    pass


# Test if the returned shipments contain the required shipment(s)
def test_get_shipments():
    pass
