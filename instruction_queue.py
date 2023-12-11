class InstructionExecution:
    def __init__(self):
        self.issue_stall = 0
        self.dest , self.operand, self.vj, self.vk = [0,0,0,0]

    def exe(self, system_instance):
        if system_instance.stall["general"] == 0 and system_instance.clock != 1 and len(system_instance.inst_queue) != 0:
            instruction = system_instance.inst_queue[0].split()
            self.operand = instruction[0]
            self.dest = instruction[1]
            self.vj = instruction[2]
            if self.operand == 'LD' or self.operand == 'STR':
                self.vk = 0
            else:
                self.vk = instruction[3]

            if system_instance.busy_reg[int(self.dest[1])] == 1:
                system_instance.stall["issue"] = 1
                self.operand = 0
                self.dest = 0
                self.vj = 0
                self.vk = 0
            else:
                system_instance.stall["issue"] = 0

            if system_instance.stall["issue"] == 1 or system_instance.stall["mem"] == 1 or system_instance.stall["add"] == 1 or system_instance.stall["mul"] == 1:
                system_instance.stall["general"] = 1
            else:
                system_instance.instruction_issued = 0

            return self.operand, self.dest, self.vj, self.vk
        else:
            return 0, 0, 0, 0
