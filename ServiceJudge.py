import os
import tempfile
import filecmp
from Utilities import *

basedir = "leetcode_clone/judge/"


def sendTemplate(id, language):
    try:
        templatefile = basedir + id + "/" + language
        template = open(templatefile, 'r')
        return template.read()
    except Exception as exception:
        return str(exception)


def submit(id, language, source):
    response = {}
    with tempfile.TemporaryDirectory() as tempdir:
        sourcefile = tempdir + "/Main." + extensions[language]
        inputfile = tempdir + "/inputs"
        outputfile = tempdir + "/outputs"
        originaloutputfile = basedir+id+"/output_{}".format(language)
        errorfile = tempdir + "/errors"
        os.system("touch {}; echo '{}' > {}".format(sourcefile, source, sourcefile))
        os.system("cp {} {}".format(basedir + id + "/inputs", inputfile))
        run = "cd {}; ".format(tempdir) + runstring[language]
        os.system(run)
        if filecmp.cmp(originaloutputfile, outputfile, shallow=False):
            os.system("cd {}; echo 'ACCEPTED' > {}".format(tempdir, outputfile))
        else:
            os.system("cd {}; echo 'REJECTED' > {}".format(tempdir, outputfile))
        output = open(outputfile, 'r')
        error = open(errorfile, 'r')
        response['output'] = output.read()
        response['errors'] = error.read()
        output.close()
        error.close()

    return response
