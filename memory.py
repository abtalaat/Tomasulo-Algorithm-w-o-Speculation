

class MemoryManagement:
    def __init__(self):
        self.start_clock = 0
        self.inst = 0
        self.dest = 0
        self.address = 0
        self.data = 0
        self.start = 0

    def exe(self, instruction, system):
        if (instruction[0] == "LD" or instruction[0] == "STR") and self.start == 1:  # Stall if the memory block is already being used
            system.stall["mem"] = 1

        if (instruction[0] == "LD" or instruction[0] == "STR") and self.start == 0:  # Start the clock when memory gets a load/store instruction
            self.start_clock = system.clock
            self.inst = instruction[0]
            self.dest = instruction[1]
            system.busy_reg[int(self.dest[1])] = 1
            self.address = instruction[2]
            self.data = instruction[3]
            self.start = 1
            system.stall["mem"] = 0

        elif system.clock == self.start_clock + system.load_time and self.start == 1:  # When "memory wait time" is done
            if self.inst == "LD":
                system.result_queue.append([self.dest, system.mem[int(self.address)]])  # Send the result on CDB if it was a LOAD instruction
            if self.inst == "STR":  # Store in memory
                if self.dest != "0":  # Store register data in memory
                    system.mem[int(self.address)] = system.register[int(self.dest[1])]
                    system.busy_reg[int(self.dest[1])] = 0
                else:  # Directly store data in memory
                    system.mem[int(self.address)] = int(self.data)

            self.start = 0
