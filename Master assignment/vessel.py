import sqlite3


class Vessel:

    def __init__(self, imo: int, mmsi: int, name: str, country: str, type: str, build: int, gross: int, netto: int,
                 length: int, beam: int) -> None:
        self.imo = imo
        self.mmsi = mmsi
        self.name = name
        self.country = country
        self.type = type
        self.build = build
        self.gross = gross
        self.netto = netto
        self.length = length
        self.beam = beam

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for
                                                               key, value in self.__dict__.items()]))

    # This function will return a float with the fuel consumption of this vessel per a certain inputted distance
    def get_fuel_consumption(self, distance: float) -> float:
        # Create a dict in which we will store the efficiency of the ship type per type
        dict_ship_type_efficiency = {
            "Aggregates Carrier": 0.4,
            "Bulk Carrier": 0.35,
            "Bulk/Oil Carrier": 0.35,
            "Cement Carrier": 0.4,
            "Container Ship": 0.3,
            "Deck Cargo Ship": 0.4,
            "General Cargo Ship": 0.4,
            "Heavy Load Carrier": 0.4,
            "Landing Craft": 0.4,
            "Nuclear Fuel Carrier": 0.35,
            "Palletised Cargo Ship": 0.4,
            "Passenger/Container Ship": 0.3,
            "Ro-Ro Cargo Ship": 0.4,
            "Self Discharging Bulk Carrier": 0.35,
            "Vehicles Carrier": 0.35,
            "Wood Chips Carrier": 0.4
        }

        # Get the efficiency that matches the ship type from our current ship
        float_efficiency = dict_ship_type_efficiency[self.type]

        # Perform the calculation
        float_calc = float_efficiency * (self.gross / self.netto) * distance

        # Round the number to a maximum of 5 decimals
        result = round(float_calc, 5)

        # Return the results
        return result

    # This function will return a tuple with the shipments for this vessel
    def get_shipments(self):
        from shipment import Shipment

        # Get the imo of the vessel from our shipment
        imo_vessel = self.imo

        # Create a list in which we will store all the shipments for this vessel.
        # We will later turn this list into a Tuple as required by the documentation for this assignment
        list_shipments = list()

        # Connect to the database
        db_conn = sqlite3.connect('shipments.db')

        # Make a query for getting the vessel information
        query = "SELECT * FROM shipments WHERE vessel = ?"

        # Execute the query for the vessel
        cur_shipments = db_conn.execute(query, [imo_vessel])

        # Iterate through the results
        for shipment in cur_shipments:

            # Split all the information into the correct variables
            db_shipment_id = shipment[0]
            db_shipment_date = shipment[1]
            db_shipment_cargo_weight = shipment[2]
            db_shipment_distance_naut = shipment[3]
            db_shipment_duration_hours = shipment[4]
            db_shipment_average_speed = shipment[5]
            db_shipment_origin = shipment[6]
            db_shipment_destination = shipment[7]
            db_shipment_vessel = shipment[8]

            # Create an instance of the class shipment with the just collected data
            shipment_instance = Shipment(db_shipment_id, db_shipment_date, db_shipment_cargo_weight,
                                         db_shipment_distance_naut, db_shipment_duration_hours,
                                         db_shipment_average_speed, db_shipment_origin, db_shipment_destination,
                                         db_shipment_vessel)

            # Append the instance to our list_shipments
            list_shipments.append(shipment_instance)

        # Close the connection to the database
        db_conn.close()

        # Turn the list into a tuple
        tuple_shipments = tuple(list_shipments)

        # Return the tuple as our result
        return tuple_shipments
