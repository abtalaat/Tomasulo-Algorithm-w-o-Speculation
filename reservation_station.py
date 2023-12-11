class ReservationStation:
    def __init__(self, system, adder, multiplier):
        self.op_res_add = [0] * system.add_number
        self.v1_add = [0] * system.add_number
        self.v2_add = [0] * system.add_number
        self.dest_add = [0] * system.add_number
        self.op_res_mul = [0] * system.mul_number
        self.v1_mul = [0] * system.mul_number
        self.v2_mul = [0] * system.mul_number
        self.dest_mul = [0] * system.mul_number
        self.adder = adder
        self.multiplier = multiplier

    def add_exe(self, number, instruction, system):
        if self.adder.busy_add[number] == 1 and self.adder.start_add[number] == 0:
            if isinstance(self.v1_add[number], int) and isinstance(self.v2_add[number], int):
                self.adder.execute(system, number, self.op_res_add[number], self.v1_add[number], self.v2_add[number], self.dest_add[number])

        if self.adder.busy_add[number] == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB") and system.instruction_issued == 0:
            self.adder.busy_add[number] = 1
            self.op_res_add[number] = instruction[0]
            self.dest_add[number] = instruction[1]
            system.busy_reg[int(self.dest_add[number][1])] = 1
            self.v1_add[number] = instruction[2]
            self.v2_add[number] = instruction[3]

            if self.v1_add[number][0] != 'R':
                self.v1_add[number] = int(self.v1_add[number])
            else:
                reg_number = int(self.v1_add[number][1])
                if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
                    self.v1_add[number] = system.register[reg_number]

            if self.v2_add[number][0] != 'R':
                self.v2_add[number] = int(self.v2_add[number])
            else:
                reg_number = int(self.v2_add[number][1])
                if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
                    self.v2_add[number] = system.register[reg_number]

            system.instruction_issued = 1
            system.stall["add"] = 0
            print("instruction", instruction, "issued to reservation station", number)

        if number == system.add_number - 1 and system.instruction_issued == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB"):
            system.stall["add"] = 1
        else:
            system.stall["add"] = 0

    def mul_exe(self, number, instruction, system):
        if self.multiplier.busy_mul[number] == 1 and self.multiplier.start_mul[number] == 0:
            if isinstance(self.v1_mul[number], int) and isinstance(self.v2_mul[number], int):
                self.multiplier.exe(number, self.op_res_mul[number], self.v1_mul[number], self.v2_mul[number], self.dest_mul[number])

        if self.multiplier.busy_mul[number] == 0 and (instruction[0] == "MUL" or instruction[0] == "DIV") and system.instruction_issued == 0:
            self.multiplier.busy_mul[number] = 1
            self.op_res_mul[number] = instruction[0]
            self.dest_mul[number] = instruction[1]
            system.busy_reg[int(self.dest_mul[number][1])] = 1
            self.v1_mul[number] = instruction[2]
            self.v2_mul[number] = instruction[3]

            if self.v1_mul[number][0] != 'R':
                self.v1_mul[number] = int(self.v1_mul[number])
            else:
                reg_number = int(self.v1_mul[number][1])
                if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
                    self.v1_mul[number] = system.register[reg_number]

            if self.v2_mul[number][0] != 'R':
                self.v2_mul[number] = int(self.v2_mul[number])
            else:
                reg_number = int(self.v2_mul[number][1])
                if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
                    self.v2_mul[number] = system.register[reg_number]

            system.instruction_issued = 1
            system.stall["mul"] = 0
            print("instruction", instruction, "issued to reservation station", number)

        if number == system.add_number - 1 and system.instruction_issued == 0 and (instruction[0] == "MUL" or instruction[0] == "DIV"):
            system.stall["mul"] = 1
