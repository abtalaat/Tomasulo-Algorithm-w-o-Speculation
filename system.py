class System:
    def __init__(self):
        self.add_number = 3
        self.mul_number = 2
        self.clock = 1
        self.max_time = 30
        self.sleep_duration = 1
        self.register = [0, 0, 0, 0, 0]
        self.busy_reg = [0, 0, 0, 0, 0]
        self.empty_reg = [1, 1, 1, 1, 1]
        self.mem = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.inst_queue = [ "LD R1 1","ADD R0 1 2", "LD R2 4"]
        self.load_time = 2
        self.result_queue = [[] for _ in range(10)]
        self.result_queue.clear()
        self.add_time = 2
        self.mul_time = 10
        self.instruction_issued = 0
        self.stall = {
            "general": 0,
            "issue": 0,
            "mem": 0,
            "add": 0,
            "mul": 0
        }
