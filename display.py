class SystemStatus:
    def __init__(self, system_module, instruction_queue_module, reservation_station_module, adder_module, multiplier_module, cdb_module):
        self.system = system_module
        self.instruction_queue = instruction_queue_module
        self.reservation_station = reservation_station_module
        self.adder = adder_module
        self.multiplier = multiplier_module
        self.cdb = cdb_module
    
    def show(self):
        print("clock cycle: ", self.system.clock)
        self.show_stall_status()
        self.show_instruction_queue()
        self.show_reservation_stations()
        self.show_adder_operations()
        self.show_multiplier_operations()
        self.show_registers()
        print()
    
    def show_stall_status(self):
        if self.system.stall["general"] == 1:
            print("stall")
    
    def show_instruction_queue(self):
        print("Instruction queue:", self.instruction_queue.operand, self.instruction_queue.dest, self.instruction_queue.vj, self.instruction_queue.vk)
    
    def show_reservation_stations(self):
        for i in range(self.system.add_number):
            print("reservation_station_adder", i, "busy", self.adder.busy_add[i], "dest", self.reservation_station.dest_add[i], "operand", self.reservation_station.op_res_add[i], "v1", self.reservation_station.v1_add[i], "v2", self.reservation_station.v2_add[i])
        
        for i in range(self.system.mul_number):
            print("reservation_station_mul", i, "busy", self.multiplier.busy_mul[i], "dest", self.reservation_station.dest_mul[i], "operand", self.reservation_station.op_res_mul[i], "v1", self.reservation_station.v1_mul[i], "v2", self.reservation_station.v2_mul[i])
    
    def show_adder_operations(self):
        for i in range(self.system.add_number):
            if self.adder.start_add[i] == 1 and self.system.clock == self.adder.start_clock_add[i]:
                print("Adder", i, " has started operation", self.adder.op_add[i], self.adder.add1[i], self.adder.add2[i], " - dest", self.adder.dest_add[i], "sent on CDB")
        
            if self.adder.start_clock_add[i] != 0 and self.system.clock == (self.adder.start_clock_add[i] + self.system.add_time):
                print("Adder", i, " has finished operation", self.adder.op_add[i], self.adder.add1[i], self.adder.add2[i], " - dest", self.adder.dest_add[i], "sent on CDB")
    
    def show_multiplier_operations(self):
        for i in range(self.system.mul_number):
            if self.multiplier.start_mul[i] == 1 and self.system.clock == self.multiplier.start_clock_mul[i]:
                print("Multiplier", i, " has started operation", self.multiplier.op_mul[i], self.multiplier.mul1[i], self.multiplier.mul2[i], " - dest", self.multiplier.dest_mul[i], "sent on CDB")
            
            if self.multiplier.start_clock_mul[i] != 0 and self.system.clock == (self.multiplier.start_clock_mul[i] + self.system.mul_time):
                print("multiplier", i, " has finished operation", self.multiplier.op_mul[i], self.multiplier.mul1[i], self.multiplier.mul2[i], " - dest", self.multiplier.dest_mul[i], "sent on CDB")
    
    def show_registers(self):
        for i in range(len(self.system.register)):
            print("R", i, ": ", self.system.register[i], sep='')
        
        for i in range(len(self.system.register)):
            print("Busy R", i, ": ", self.system.busy_reg[i], sep='')
