from ServiceJudge import sendTemplate, submit
class Judge(object):

    def on_get(self, request, response, id, language):
        response.media = sendTemplate(id, language)

    def on_post(self, request, response, id, language):
        source = request.media
        response.media = submit(id, language, source)