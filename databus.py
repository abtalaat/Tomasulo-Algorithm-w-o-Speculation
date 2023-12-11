class ExecutionManager:
    def __init__(self, system, reservation_station):
        self.system = system
        self.reservation_station = reservation_station

    def execute(self):
        # Fetch the results on the result_queue and send them back to the registers as well as the reservation stations
        for i in range(len(self.system.result_queue)):
            result = self.system.result_queue[0]
            register_number = int(result[0][1])
            self.system.register[register_number] = result[1]  # Store the result in the register
            self.system.busy_reg[register_number] = 0
            self.system.empty_reg[register_number] = 0

            # Access reservation station variables using the instance reference
            for j in range(self.system.add_number):
                if self.reservation_station.v1_add[j] == result[0]:
                    self.reservation_station.v1_add[j] = result[1]

                if self.reservation_station.v2_add[j] == result[0]:
                    self.reservation_station.v2_add[j] = result[1]

            for j in range(self.system.mul_number):
                if self.reservation_station.v1_mul[j] == result[0]:
                    self.reservation_station.v1_mul[j] = result[1]

                if self.reservation_station.v2_mul[j] == result[0]:
                    self.reservation_station.v2_mul[j] = result[1]

            self.system.result_queue.pop(0)
