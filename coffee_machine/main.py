### Coffee Machine Simulation ###
import os
import logging
import sys

from coffee_machine.apputils import create_logger
from coffee_machine.data.process_input import get_machine_configuration
from coffee_machine.coffee_system import CoffeeMachine

def main():
    # create a log file
    logger = create_logger()

    # get user input
    if len(sys.argv) != 2:
        logger.info("correct usage is :: python3 main.py <user_input>.json\n exiting...")
        exit(0)
    # json file
    user_input_file = sys.argv[1]
    machine_config = get_machine_configuration(user_input_file)
    my_coffee_machine = CoffeeMachine(machine_config)
    my_coffee_machine.run()

if __name__ == '__main__':
    main()
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n ---- Keyboard Interrupt ----")
        exit(0)
    #finally:
        if logger is not None:
            logger.info('')
            logger.info("Log file for this is available at: ", os.path.realpath(logger.logfilename))
    """