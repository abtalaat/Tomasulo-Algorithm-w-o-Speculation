class InstructionExecution:
    def __init__(self):
        self.issue_stall = 0

    def exe(self, system_instance):
        if system_instance.stall["issue"] == 0 and system_instance.stall["mem"] == 0 and system_instance.stall["add"] == 0 and system_instance.stall["mul"] == 0 and system_instance.clock != 1 and len(system_instance.inst_queue) != 0:
            #global instruction, operand, dest, vj, vk, issue_stall

            if system_instance.stall["issue"] == 0 and system_instance.stall["mem"] == 0 and system_instance.stall["add"] == 0 and system_instance.stall["mul"] == 0 and system_instance.clock != 1 and len(system_instance.inst_queue) != 0:
                system_instance.inst_queue.pop(0)
                system_instance.stall["general"] = 0

            if len(system_instance.inst_queue) == 0:
                return 0, 0, 0, 0

            instruction = system_instance.inst_queue[0].split()
            operand = instruction[0]
            dest = instruction[1]
            vj = instruction[2]
            if operand == 'LD' or operand == 'STR':
                vk = 0
            else:
                vk = instruction[3]

            if system_instance.busy_reg[int(dest[1])] == 1:
                system_instance.stall["issue"] = 1
                operand = 0
                dest = 0
                vj = 0
                vk = 0
            else:
                system_instance.stall["issue"] = 0

            if system_instance.stall["issue"] == 1 or system_instance.stall["mem"] == 1 or system_instance.stall["add"] == 1 or system_instance.stall["mul"] == 1:
                system_instance.stall["general"] = 1
            else:
                system_instance.instruction_issued = 0

            return operand, dest, vj, vk
