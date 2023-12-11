from system import System
from display import SystemStatus
from reservation_station import ReservationStation
from databus import ExecutionManager
from adder import AdderManager
from memory import MemoryManagement
from instruction_queue import InstructionExecution
from multiplier import MultiplierALU

# Instantiate the components
system_instance = System()
multiplier_alu = MultiplierALU(system_instance) 
adder_manager = AdderManager(system_instance)
reservation_station = ReservationStation(system_instance, adder_manager, multiplier_alu)
execution_manager = ExecutionManager(system_instance, reservation_station)
memory_manager = MemoryManagement()
instruction_executor = InstructionExecution()
system_status = SystemStatus(system_instance, instruction_executor, reservation_station, adder_manager, multiplier_alu, execution_manager)
multiplier_alu = MultiplierALU(system_instance) 

# Simulation loop
while system_instance.clock <= system_instance.max_time:
    # Execute instructions using the InstructionExecution class
    execution_result = instruction_executor.exe(system_instance)
    
    if execution_result is None:
        # Handle the case where no instructions are available or some condition is not met
        # For example, you might want to break out of the simulation loop or perform other actions
        print("error")
        break
    
    operand, dest, vj, vk = execution_result

    # Execute addition/subtraction operations
    for i in range(system_instance.add_number):
        reservation_station.add_exe(i, [operand, dest, vj, vk], system_instance)
        adder_manager.execute(system_instance, i, 0,0,0,0)

    # Execute multiplication/division operations
    for i in range(system_instance.mul_number):
        reservation_station.mul_exe(i, [operand, dest, vj, vk], system_instance)
        multiplier_alu.exe(i, 0, 0, 0, 0)
   
    # Execute memory operations using MemoryManagement class
    memory_manager.exe([operand, dest, vj, vk], system_instance)

    # Execute the execution manager
    execution_manager.execute()

    # Display system status
    system_status.show()

    # Increment clock cycle
    system_instance.clock += 1
