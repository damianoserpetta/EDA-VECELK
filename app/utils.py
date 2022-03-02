import os
import json


def convert_json_to_dicts(paths):
    dicts = []
    for filename in paths:
        fpath = os.path.join(filename.parent, filename.name)
        if(not(os.path.isfile(fpath))):
            quit()

        with open(fpath) as json_file:
            dicts.append(json.load(json_file))
    return dicts
