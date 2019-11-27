from lib.views import View


class HomeView(View):

    async def get(self):
        return {'message': 'home'}


router = HomeView.handles_path("/", tags=["home"])
