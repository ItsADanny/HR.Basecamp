from vessel import Vessel
from shipment import Shipment


# Test to check if duration is converted correctly based on the given arguments
# 1) %D:%H:%M
# 2) %H:%M
def test_convert_duration():
    test_shipment = Shipment("78067E7F-D833-4312-A805-C1355F51F065", "01-01-2023", 15649,
                             5879249, 864595, 6.8, "MYTPP", "TRGEM", 9913547)
    assert test_shipment.convert_duration("%D:%H:%M") == "36024:595:51875700"
    assert test_shipment.convert_duration("%H:%M") == "595:51875700"


# Test to check if distance is converted correctly based on the given arguments
# 1) NM = Nautical Meters
# 2) M = Meters
# 3) KM = Kilometers
# 4) MI = Miles
# 5) YD = Yards
# 6) ValueError check
def test_convert_distance():
    test_shipment = Shipment("78067E7F-D833-4312-A805-C1355F51F065", "01-01-2023", 15649,
                             5879249, 864595, 6.8, "MYTPP", "TRGEM", 9913547)
    assert test_shipment.convert_distance("NM") == 5879249
    assert test_shipment.convert_distance("M") == 10888369148
    assert test_shipment.convert_distance("KM") == 10888369.148
    assert test_shipment.convert_distance("MI") == 6765722.16422
    assert test_shipment.convert_distance("YD") == 11907665306.15567
    assert test_shipment.convert_distance("Q") == ValueError


# Test to check if speed is converted correctly based on the given arguments
# 1) Knts = Knots
# 2) Mph = Miles per hour
# 3) Kph = Kilometers per hour
# 4) ValueError check
def test_convert_speed():
    test_shipment = Shipment("78067E7F-D833-4312-A805-C1355F51F065", "01-01-2023", 15649,
                             5879249, 864595, 6.8, "MYTPP", "TRGEM", 9913547)
    assert test_shipment.convert_speed("Knts") == 5879246
    assert test_shipment.convert_speed("Mph") == 7.825304
    assert test_shipment.convert_speed("Kph") == 10888369.148
    assert test_shipment.convert_speed("Km") == ValueError


# Test to check if the fuel consumption is calculated correctly based on the distance
def test_get_fuel_consupmtion():
    test_vessel = Vessel(9913547, 477736400, "TIGER LONGKOU", "Hong Kong", "Deck Cargo Ship", 2022,
                         23040, 26200, 192, 37)
    assert test_vessel.get_fuel_consumption(750) == 351.75572


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
