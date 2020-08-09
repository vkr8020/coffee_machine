import os
import json
from coffee_machine.apputils.exceptions import FileHandlingException


def read_jsonfile(inpfile):
    if not os.path.exists(inpfile):
        raise FileNotFoundError("couldn\'t find the {0} file".format(inpfile))
    try:
        with open(inpfile) as f:
            json_data = json.load(f)
    except:
        raise FileHandlingException("Couldn\'t read the json file[{0}]".format(inpfile))

    return json_data
