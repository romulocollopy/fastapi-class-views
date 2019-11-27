from lib.views import View


class EchoView(View):

    def get(self, message: str, q: str = None):
        response =  {'get': message}
        if q:
            response['q'] = q
        return response


    def post(self, message: str):
        return {'post': message}


router = EchoView.handles_path("/echo/{message}", tags=["echo"])
