import sqlite3


class Port:

    def __init__(self, id: str, code: int, name: str, city: str, province: str, country: str) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.city = city
        self.province = province
        self.country = country

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in
                                                               self.__dict__.items()]))

    def get_shipments(self) -> tuple:
        from shipment import Shipment
        # Create an empty tuple to which we will use to add all the shipment instances
        # Connect to the database
        db_conn = sqlite3.connect("../HR.Basecamp/Master assignment/shipments.db")

        # Create a list in which we will store all the shipments for this port.
        # We will later turn this list into a Tuple as required by the documentation for this assignment
        list_shipments = list()

        # Prepare the select query
        query = "SELECT * FROM shipments WHERE origin = ? OR destination = ?"

        # Execute the query and get the cursor
        cur = db_conn.execute(query, [self.id, self.id])

        # Loop through the results and create Shipment instances with the data and
        for shipment in cur:

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
