import logging

from aiohttp import ClientSession, ClientResponseError, ClientError


class Database:
    # DELIVERY_COST = "10000"

    def __init__(self, base_url):
        self.base_url = base_url

    async def make_request(self, method, endpoint, data=None):
        url = self.base_url + endpoint

        try:
            async with ClientSession() as session:
                async with session.request(method, url, json=data) as resp:
                    # r = await resp.json()
                    # logging.info(r)
                    if resp.status in [200, 201]:
                        return await resp.json(), resp.status
                    else:
                        raise ClientResponseError(resp.request_info,
                                                  resp.history,
                                                  status=resp.status,
                                                  message=resp.reason)
        except ClientError as e:
            raise e
        finally:
            await session.close()

    async def send_token_to_server(self, user_id, token):
        return await self.make_request("POST", "/create-chat/",
                                       {'token': token, 'chat_id': user_id})
