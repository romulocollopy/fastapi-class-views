from lib.views import View


class HomeView(View):

    def get(self):
        return {'message': 'home'}


router = HomeView.handles_path("/", tags=["home"])
