import random

import requests
import re


class MovieManager:

    def __init__(self):
        self.session = requests.session()
        self._home_page_url = 'http://localhost:8080/moviemanager'
        self._login_url = 'http://localhost:8080/moviemanager/index_login.action'
        self._movie_list_url = 'http://localhost:8080/moviemanager/movie_list.action'
        self._query_movie_url = 'http://localhost:8080/moviemanager/movie_query.action'
        self._query_movie_detail_url = 'http://localhost:8080/moviemanager/movie_detail.action'
        self._login_out_url = 'http://localhost:8080/moviemanager/index_loginOut.action'
        self._movie_list = []
        self._movie_id = 0

    def home(self, filename=0):
        response = self.session.get(self._home_page_url)
        code, text = self._getResult(response, filename)
        return code, text

    def login(self, uname, pwd, filename=0):
        # noinspection SpellCheckingInspection
        param = {'usermanage.usercode': uname, 'usermanage.userpassword': pwd}
        response = self.session.post(url=self._login_url, data=param)
        code, text = self._getResult(response, filename)
        return code, text

    def movie_list(self, filename=0):
        response = self.session.get(self._movie_list_url)
        code, text = self._getResult(response, filename)
        response.encoding = 'utf-8'
        self._movie_list = re.findall('<td height="28" class="table_border2 padding_center"><input '
                                      r'type="checkbox" value="(.+?)" class="item"></td>\s+?<td '
                                      'class="table_border2 padding_center">(.+?)&nbsp;</td>',
                                      response.text)
        # print('list = ', self._movie_list)
        return code, text

    def query_movie(self, filename=0, movie_name=0):
        if movie_name != 0:
            movie_name = movie_name
        else:
            r_tuple = random.sample(self._movie_list, 1)
            movie_name = r_tuple[0][1]
            self._movie_id = r_tuple[0][0]
        param = {'movie.movieName': movie_name,
                 'query': 'query',
                 'x': '0',
                 'y': '0'
                 }
        response = self.session.post(url=self._query_movie_url, data=param)
        code, text = self._getResult(response, filename)
        return code, text

    def query_detail(self, filename=0):
        param = {'movie.id': self._movie_id}
        response = self.session.post(url=self._query_movie_detail_url, data=param)
        code, text = self._getResult(response, filename)
        return code, text

    def login_out(self, filename=0):
        response = self.session.get(self._login_out_url)
        code, text = self._getResult(response, filename)
        return code, text

    @staticmethod
    def _getCode(response):
        code = response.status_code
        return code

    @staticmethod
    def _getText(response, filename=0):
        filename = str(filename)
        content = response.content
        if filename != '0':
            with open(file=filename + ".html", mode='wb+') as f:
                f.write(content)
        response.encoding = 'utf-8'
        text = response.text
        return text

    @staticmethod
    def find(text, method):
        # print('text+',text)
        if method == 'home' and '用户名或密码错误' in text:
            return 1
        elif method == 'login' and '影院信息管理' in text:
            return 1
        elif method == 'movie_list' and '上映时间' in text:
            return 1
        elif method == 'query_movie' and 'movie.id' in text:
            return 1
        elif method == 'query_detail' and '电影海报路径' in text:
            return 1
        elif method == 'login_out' and '江西联通沃电影平台-登录' in text:
            return 1
        return 0

    def _getResult(self, response, filename=0):
        code = self._getCode(response)
        text = self._getText(response, filename)
        return code, text

    ...


if __name__ == "__main__":
    print('start')
    run = MovieManager()
    run.home()
    run.login('admin', '123456', )
    run.movie_list()
    run.query_movie(filename='movieQuery')
    code1, text1 = run.query_detail("details")
    a = run.find(text1, 'query_detail')
    print(a)

    print("success")
