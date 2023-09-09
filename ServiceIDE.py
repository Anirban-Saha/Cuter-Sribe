import os
import tempfile
from Utilities import *

basedir = "leetcode_clone/ide/starters/"


def sendStarter(language):
    starter = open(basedir + language, 'r')
    return starter.read()


def run(language, source, inputs):
    response = {}
    with tempfile.TemporaryDirectory() as tempdir:
        sourcefile = tempdir + "/Main." + extensions[language]
        inputfile = tempdir + "/inputs"
        outputfile = tempdir + "/outputs"
        errorfile = tempdir + "/errors"
        os.system("touch {}; echo '{}' > {}".format(sourcefile, source, sourcefile))
        os.system("touch {}; echo '{}' > {}".format(inputfile, inputs, inputfile))
        run = "cd {}; ".format(tempdir) + runstring[language]
        error = os.system(run)
        output = open(outputfile, 'r')
        error = open(errorfile, 'r')
        response['output'] = output.read()
        response['errors'] = error.read()
        output.close()
        error.close()

    return response
