import time
from display import SystemStatus
from system import System
from instruction_queue import InstructionQueue
from memory import Memory
from reservation_station import ReservationStation
from adder import AdderManager
from multiplier import MultiplierManager
from databus import ExecutionManager

# Initialize the system and components
system = System()
instruction_queue = InstructionQueue()
memory = Memory()
reservation_station = ReservationStation()
adder_manager = AdderManager()
multiplier_manager = MultiplierManager()
cdb = ExecutionManager()
display = SystemStatus()

system.initialize()

# Main loop
for system.clock in range(1, system.max_time):
    instruction = instruction_queue.exe()

    memory.exe(instruction)

    for i in range(system.add_number):
        reservation_station.add_exe(i, instruction)
        adder_manager.execute(system, i, 0, 0, 0, 0)

    for i in range(system.mul_number):
        reservation_station.mul_exe(i, instruction)
        multiplier_manager.exe(system, i, 0, 0, 0, 0)

    cdb.execute()

    system_status = display.generate_system_status(system, instruction_queue, reservation_station, adder_manager, multiplier_manager)
    display.generate_system_status(system_status)

    time.sleep(system.sleep_duration)

for i in range(len(system.mem)):
    print("Memory slot", i, ": ", system.mem[i], sep='')
