import redis

class CacheManager:
    def __init__(self, host, port,password, *args, **kwargs):
        self.redis_client = redis.Redis(
        host = host,
        port = port,
        password = password,
        *args,
        **kwargs,
        )

        connection_status = self.redis_client.pin()
        if connection_status:
            print("Connected to redis")
        else:
            print("The connection to Redis was unsuccesfull")

    def store_data(self,key,value,time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key,value)
            else:
                self.redis_client.setex(key,time_to_live,value)
        except redis.RedisError as e:
            print(f"An error ocurred while storing data in Redis : {e}")

    def check_key(self, key):
        try:
            key_exists = self.redis_client.exists(key)
            if key_exists:
                ttl = self.redis_client.ttl(key)
            if ttl:
                print(ttl)

            return True, ttl
        except redis.RedisError as e:
            print(f"An error ocurred while showing data in Redis : {e}")

    def get_data(self,key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                result = output.decode('utf-8')
                return result
            else:
                print(f"No value found for key {key}.")
                return None
        except redis.RedisError as e:
            print(f"An error ocurred while getting data in Redis : {e}")

    def delete_data(key):
        try:
            output = self.redis_client.delete(key)
            if output > 0:
                print(f"Key '{key}' and its value have been deleted.")
            else:
                print(f"Key '{key}' not found.")
            return output == 1
        except redis.RedisError as e:
            print(f"An error ocurred while deleting data from Redis: {e}")
        return False
        
    
    def delete_data_with_pattern(self, pattern):
        try:
            for key in self.redis_client.scan_iter(match=pattern):
                self.delete_data(key)
        except redis.RedisError as e:
            print(f"An error ocurred while deleting data from Redis: {e}")
