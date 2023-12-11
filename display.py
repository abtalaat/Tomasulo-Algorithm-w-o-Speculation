class SystemStatus:
    def __init__(self):
        self.clock_cycle = None
        self.stall = False
        self.instruction_queue = None
        self.adder_reservation_station = []
        self.multiplier_reservation_station = []
        # ... other attributes for adder and multiplier operations ...

    def generate_system_status(self, system_instance, instruction_queue_instance, reservation_station_instance, adder_instance, multiplier_instance):
        self.clock_cycle = system_instance.clock

        if system_instance.stall["general"] == 1:
            self.stall = True

        self.instruction_queue = {
            "operand": instruction_queue_instance.operand,
            "dest": instruction_queue_instance.dest,
            "vj": instruction_queue_instance.vj,
            "vk": instruction_queue_instance.vk
        }

        # Adder reservation station
        for i in range(system_instance.add_number):
            self.adder_reservation_station.append({
                "index": i,
                "busy": adder_instance.busy_add[i],
                "dest": reservation_station_instance.dest_add[i],
                "operand": reservation_station_instance.op_res_add[i],
                "v1": reservation_station_instance.v1_add[i],
                "v2": reservation_station_instance.v2_add[i]
            })

        # Multiplier reservation station
        for i in range(system_instance.mul_number):
            self.multiplier_reservation_station.append({
                "index": i,
                "busy": multiplier_instance.busy_mul[i],
                "dest": reservation_station_instance.dest_mul[i],
                "operand": reservation_station_instance.op_res_mul[i],
                "v1": reservation_station_instance.v1_mul[i],
                "v2": reservation_station_instance.v2_mul[i]
            })

        # Logic for adder and multiplier operations...
        # ...

        # Register status (you can store registers similarly)

        return self
