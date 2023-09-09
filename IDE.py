from ServiceIDE import sendStarter, run


class IDE(object):

    def on_get(self, request, response, language):
        response.media = sendStarter(language)

    def on_post(self, request, response, language):
        source = request.media['source']
        inputs = request.media['inputs']
        response.media = run(language, source, inputs)