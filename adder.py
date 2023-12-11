class AdderManager:
    def __init__(self, system):
        self.start_clock_add = [0] * system.add_number
        self.add1 = [0] * system.add_number
        self.add2 = [0] * system.add_number
        self.op_add = [0] * system.add_number
        self.busy_add = [0] * system.add_number
        self.start_add = [0] * system.add_number
        self.dest_add = ['0'] * system.add_number

    def execute(self, system_instance, number, op, v1, v2, dest):
        if op == "ADD" or op == "SUB":  # Start the clock when adder gets a new instruction
            self.op_add[number] = op
            self.add1[number] = v1
            self.add2[number] = v2
            self.dest_add[number] = dest
            self.start_clock_add[number] = system_instance.clock
            self.start_add[number] = 1
            # print("start", op, "on adder", number)

        elif op == 0 and system_instance.clock == self.start_clock_add[number] + system_instance.add_time and self.start_clock_add[number] != 0:  # Send the result on CDB when the "calculation" is done
            if self.op_add[number] == "ADD":
                system_instance.result_queue.append([self.dest_add[number], self.add1[number] + self.add2[number]])
                # print("operation finished, send result", self.add1[number] + self.add2[number], "on result_queue from adder", number)
            elif self.op_add[number] == "SUB":
                system_instance.result_queue.append([self.dest_add[number], self.add1[number] - self.add2[number]])
                # print("operation finished, send result", self.add1[number] - self.add2[number], "on result_queue from adder", number)

            self.busy_add[number] = 0  # Adder isn't busy anymore
            self.start_add[number] = 0
