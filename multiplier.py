class MultiplierALU:
    def __init__(self, system):
        self.start_clock_mul = [0] * system.mul_number
        self.mul1 = [0] * system.mul_number
        self.mul2 = [0] * system.mul_number
        self.op_mul = [0] * system.mul_number
        self.busy_mul = [0] * system.mul_number
        self.start_mul = [0] * system.mul_number
        self.dest_mul = ['0'] * system.mul_number

    def exe(self, number, op, v1, v2, dest, system):
        if op == "MUL" or op == "DIV":  # Check if it's a MUL or DIV operation and start the clock
            self.op_mul[number] = op
            self.mul1[number] = v1
            self.mul2[number] = v2
            self.dest_mul[number] = dest
            self.start_clock_mul[number] = system.clock
            self.start_mul[number] = 1

        elif op == 0 and system.clock == self.start_clock_mul[number] + system.mul_time and self.start_clock_mul[number] != 0:  # Send the result on CDB after the "computing" time
            if self.op_mul[number] == "MUL":
                system.result_queue.append([self.dest_mul[number], self.mul1[number] * self.mul2[number]])
            elif self.op_mul[number] == "DIV":
                system.result_queue.append([self.dest_mul[number], self.mul1[number] / self.mul2[number]])

            self.busy_mul[number] = 0  # Multiplier isn't busy anymore
            self.start_mul[number] = 0
