from datetime import date
import sqlite3


class Shipment:

    def __init__(self, id: str, date: date, cargo_weight: int, distance_naut: float, duration_hours: float,
                 average_speed: float, origin: str, destination: str, vessel: int) -> None:
        self.id = id
        self.date = date
        self.cargo_weight = cargo_weight
        self.distance_naut = distance_naut
        self.duration_hours = duration_hours
        self.average_speed = average_speed
        self.origin = origin
        self.destination = destination
        self.vessel = vessel

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    def get_ports(self) -> dict:
        # Import the port class
        from port import Port

        # Retrieve the ID of the Origin and Destination of the shipment
        id_origin = self.origin
        id_destination = self.destination

        # Connect to the database
        db_conn = sqlite3.connect('shipments.db')

        # Make a query for getting the port information
        query = "SELECT * FROM ports WHERE id = ?"

        # Execute the query for the Origin
        cur_origin = db_conn.execute(query, [id_origin])

        # Get the information for the origin port and put it into a variable
        origin_port_info = cur_origin.fetchone()

        # Split all the information into the correct variables
        id_origin_port_db = origin_port_info[0]
        code_origin_port_db = origin_port_info[1]
        name_origin_port_db = origin_port_info[2]
        city_origin_port_db = origin_port_info[3]
        province_origin_port_db = origin_port_info[4]
        country_origin_port_db = origin_port_info[5]

        # Create an instance of the class port for the origin with the just collected data
        port_origin = Port(id_origin_port_db, code_origin_port_db, name_origin_port_db, city_origin_port_db,
                           province_origin_port_db, country_origin_port_db)

        # Execute the query for the Destination
        cur_destination = db_conn.execute(query, [id_destination])

        # Get the information for the destination port and put that into a Port instance
        destination_port_info = cur_destination.fetchone()

        # Split all the information into the correct variables
        id_destination_port_db = destination_port_info[0]
        code_destination_port_db = destination_port_info[1]
        name_destination_port_db = destination_port_info[2]
        city_destination_port_db = destination_port_info[3]
        province_destination_port_db = destination_port_info[4]
        country_destination_port_db = destination_port_info[5]

        # Create an instance of the class port for the origin with the just collected data
        port_destination = Port(id_destination_port_db, code_destination_port_db, name_destination_port_db,
                                city_destination_port_db, province_destination_port_db, country_destination_port_db)

        # Close the connection to the database
        db_conn.close()

        # Return a dict with our information
        return {id_origin: port_origin, id_destination: port_destination}

    def get_vessel(self):
        # Import the class
        from vessel import Vessel

        # Get the imo of the vessel from our shipment
        imo_vessel = self.vessel

        # Connect to the database
        db_conn = sqlite3.connect('shipments.db')

        # Make a query for getting the vessel information
        query = "SELECT * FROM vessels WHERE imo = ?"

        # Execute the query for the vessel
        cur_vessel = db_conn.execute(query, [imo_vessel])

        # Get the information for the vessel and put it into a variable
        vessel_info = cur_vessel.fetchone()

        # Split all the information into the correct variables
        imo_vessel_db = vessel_info[0]
        mmsi_vessel_db = vessel_info[1]
        name_vessel_db = vessel_info[2]
        country_vessel_db = vessel_info[3]
        type_vessel_db = vessel_info[4]
        build_vessel_db = vessel_info[5]
        gross_vessel_db = vessel_info[6]
        netto_vessel_db = vessel_info[7]
        length_vessel_db = vessel_info[8]
        beam_vessel_db = vessel_info[9]

        # Create an instance of the class Vessel for the vessel with the just collected data
        vessel = Vessel(imo_vessel_db, mmsi_vessel_db, name_vessel_db, country_vessel_db, type_vessel_db,
                        build_vessel_db, gross_vessel_db, netto_vessel_db, length_vessel_db, beam_vessel_db)

        # Close the connection to the database
        db_conn.close()

        # Return the Vessel instance
        return vessel

    def calculate_fuel_costs(self, price_per_liter: float, vessel) -> float:
        # Get the fuel consumption for this Vessel based on the distance of this shipment
        fuel_needed = vessel.get_fuel_consumption(self.distance_naut)
        # Calculate how much money it would cost per liter
        result_calc = price_per_liter * fuel_needed
        # Return the result
        return result_calc

    def convert_speed(self, to_format: str) -> float:
        # Check to see if the to_format has a valid format, If not then raise an ValueError
        if to_format == "Knts":
            # For calculating knots we need 2 variables, The average speed and the duration
            shipment_vessel_average_speed = self.average_speed
            shipment_vessel_duration_hours = self.duration_hours

            # The formula for converting nautical miles to knots is as followed:
            # 1 kn = 1 nmi × 1 h
            # kn = knots
            # nmi = nautical miles
            # h is time in hours

            # now we perform the calculation and put it into our return (result) variable
            step1_calc = shipment_vessel_average_speed * shipment_vessel_duration_hours

            # Round down the result and put it into our result
            result = round(step1_calc, 6)

        elif to_format == "Mph":
            # For calculating m/h, we need 2 variables, The average speed and the duration
            shipment_vessel_average_speed = self.average_speed
            shipment_vessel_duration_hours = self.duration_hours

            # The formula for converting nautical miles to km is as followed:
            # 1.15078 km = 1 nmi x 1.15078 m
            # m = miles
            # nmi = nautical miles

            # First, we convert the nautical miles to miles
            step1_calc = shipment_vessel_average_speed * 1.15078

            # The formula for turning m to m/hr is as followed:
            # m/hr = m / hr
            # hr = hour
            # m = miles
            # m/hr = miles per hour

            # Second, we calculate the m/hr based on our kms and the duration of our voyage
            step2_calc = step1_calc * shipment_vessel_duration_hours

            # Round down the result and put it into our result
            result = round(step2_calc, 6)

        elif to_format == "Kmph":
            # For calculating km/h, we need 2 variables, The average speed and the duration
            shipment_vessel_average_speed = self.average_speed
            shipment_vessel_duration_hours = self.duration_hours

            # The formula for converting nautical miles to km is as followed:
            # 1.852 km = 1 nmi x 1.852 km
            # km = kilometer
            # nmi = nautical miles

            # First, we convert the nautical miles to kilometers
            step1_calc = shipment_vessel_average_speed * 1.852

            # The formula for turning km to km/hr is as followed:
            # km/hr = km / hr
            # hr = hour
            # km = kilometer
            # km/hr = kilometer per hour

            # Second, we calculate the km/hr based on our kms and the duration of our voyage
            step2_calc = step1_calc * shipment_vessel_duration_hours

            # Round down the result and put it into our result
            result = round(step2_calc, 6)

        else:
            raise ValueError

        # Return the result
        return result

    def convert_distance(self, to_format: str) -> float:
        if to_format == "NM":
            return round(self.distance_naut * 1, 6)
        elif to_format == "M":
            return round(self.distance_naut * 1852, 6)
        elif to_format == "KM":
            return round(self.distance_naut * 1.852, 6)
        elif to_format == "MI":
            return round(self.distance_naut * 1.15078, 6)
        elif to_format == "YD":
            return round(self.distance_naut * 2025.37183, 6)
        else:
            raise ValueError

    def convert_duration(self, to_format: str) -> str:
        # convert the duration of the shipment into multiple parts (Days, Hours and Minutes)
        days = self.duration_hours / 24
        hours = self.duration_hours // 3600
        minutes = self.duration_hours * 60

        # Use the inputted format and insert our days, hours and minutes
        step1 = to_format.replace("%D", str(days))
        step2 = step1.replace("%H", str(hours))
        step3 = step2.replace("%M", str(minutes))

        # Return the format
        return step3
