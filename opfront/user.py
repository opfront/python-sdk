from opfront.resource import OpfrontResource


class UserResource(OpfrontResource):

    def update(self, res):
        if hasattr(res, 'password') and not res.password:
            del res.password
        return super().update(res)

    def me(self):
        res_url = '{0}/me'.format(self._endpoint)
        body = self._client.do_request(res_url, 'GET')

        return self._make_model(**body)
