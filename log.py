"""
-> Logging
Log files help us to find problems and to get information about the state of our systems.
They are an essential tool for avoiding and understanding errors.
"""

"""
~ Security Levels

>> 1) DEBUG - used for tests, experiments or in order to check something (troubleshooting).
>> 2) INFO  - when we want to log all the important events that inform us about what is happening.
>> 3) WARNING - inform us about irregularities and things that might go wrong and become a problem.
>> 4) ERROR - when something didn't go according to the plan or when we get an exception.
>> 5) CRITICAL - when a crucial component fails and we have to immediately stop all operations.
"""

#~Creating Logggers

import logging

#! Root Logger

logging.info("Informational Message")
logging.critical("Critical Message")

#! Custom Logger

logger = logging.getLogger()  # By method
logger = logging.Logger("MyLogger")  # By Constructor

logger.info("Logger Created Successfully")
logger.log(logging.INFO, "Successful")

logger.critical("Critical Message")
logger.log(logging.CRITICAL, "Critical")

"""
? NOTE: 
The above script will only print the critical messages.
This has two reasons-  
>> We need to adjust the level of the logger.
>> We need to remove all of the handlers from the default root logger.
"""

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

logging.basicConfig(level= logging.INFO)

logger = logging.getLogger()

logger.log(logging.INFO, "Successfully Logged")



#~ Logging into files

#>> We need to create a FIle Handler for this

import logging

logger  = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logfile.log")
handler.setLevel(logging.INFO)

logger.addHandler(handler)

logger.info("This is a Informational Message")
logger.critical("Critical Message!")

#~ Formatting Logs

#>> We can use formatter for this

import logging

logger = logging.Logger("MyLogger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logfile.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Debug Message!")
logger.info("Informational Message!")
logger.warning("Warning Message!")
logger.error("Error Message!")
logger.critical("Critical Message!")


