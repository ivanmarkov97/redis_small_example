from redis import Redis


class RedisConnection:

    def __init__(self, host, port, db, password=None):
        self._redis = Redis(host=host, port=port, db=db, password=password)

    def add_item(self, user, value):
        self._redis.set(user, value)

    def get_item(self, user):
        item = self._redis.get(user)
        if item is not None:
            return item.decode('utf-8')
        return item

    def set_ttl(self, key, seconds):
        self._redis.expire(key, seconds)

    def get_ttl(self, key):
        return self._redis.ttl(key).decode('utf-8')

    def get_user_auth(self, username):
        user_auth_key = f'user_auth:{username}'
        if not self.get_item(user_auth_key):
            return False
        return True

    def auth(self, username, password):
        user_key = f'user:{username}'
        if not self._redis.hgetall(user_key):
            return False
        user_password = self._redis.hget(user_key, 'password').decode('utf-8')
        if user_password == password:
            user_auth_key = f'user_auth:{username}'
            self.add_item(user_auth_key, True)
            self.set_ttl(user_auth_key, 60)
            return True
        else:
            return False
