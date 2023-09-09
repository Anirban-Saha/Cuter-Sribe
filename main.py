from IDE import IDE
from Judge import Judge
import falcon

app = application = falcon.App()

ide = IDE()
judge = Judge()

app.add_route('/ide/{language}', ide)
app.add_route('/judge/{id}/{language}', judge)
