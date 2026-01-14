import redis

redis_client = redis.Redis(
    host="redis-18018.c44.us-east-1-2.ec2.cloud.redislabs.com",
    port= 18018,
    password= "8WOPf1mmHS5kJEeS4ecLJJ2Sg2ACFyQ9",
)

try:
    connection_status = redis_client.ping()
    if connection_status:
        print("Connected to redis")
    else:
        print("The connection to Redis was unsuccesfull")
except redis.ConnectionError as ex:
    print("An error ocurred while conencting to Redis", ex)


#***Funciones para almacenar datos****
# def store_data(key,value,time_to_live=None):
#     try:
#         if time_to_live is None:
#             redis_client.set(key,value)
#             print(f"Key '{key}' created with value '{value}' .")
#         else:
#             redis_client.setex(key,time_to_live,value)
#             print(f"Key '{key}' created with value '{value}' and a ttl of {time_to_live}.")
#     except redis.RedisError as error:
#         print(f"An error ocurred while storing data in Redis : {error}")

# #ejemplo de uso:

# store_data("full_name", "John Doe")
# store_data("important_key", "Important Value!", time_to_live=100)


#****Funciones para revisar keys****
# redis_client.exists("important_key")  # Revisar si un key existe
# redis_client.ttl("important_key")  # Revisar el time to live de un key

# def check_key(key):
#     try:
#         key_exists = redis_client.exists(key)
#         if key_exists:
#             ttl = redis_client.ttl(key)
#             print("key:",key)
#         if ttl:
#             print("ttl : ",ttl)

#         return True, ttl


#     except redis.RedisError as error:
#         print(f"An error ocurred while showing data in Redis : {error}")

# key_exists,ttl = check_key("important_key")
# print("Key exists:", key_exists)
# print("TTL:", ttl)

#****Función para obtener datos****
# value = redis_client.get("important_key")
# print(value.decode('utf-8'))

# def get_data(key):
#     try:
#         output = redis_client.get(key)
#         if output is not None:
#             result = output.decode('utf-8')
#             print(f"Value '{result}' found for key '{key}'.")
#             return result
#         else:
#             print(f"No value found for key {key}.")
#             return None
#     except redis.RedisError as e:
#         print(f"An error ocurred while retrieving data from Redis: {e}")

# value = get_data("full_name")
# print("Value:", value)

# ***Funciones para eliminar datos***
# redis_client.delete("important_key") # Para eliminar un key  Redis NO devuelve True/False, devuelve un numero entero 1 si La key existía y fue eliminada  y  0 La key no existía, no se eliminó nada
# redis_client.flushdb() # Para eliminar TODOS los keys de la base de datos

def delete_data(key):
    try:
        output = redis_client.delete(key)
        if output > 0:
            print(f"Key '{key}' and its value have been deleted.")
        else:
            print(f"Key '{key}' not found.")
        
        return output == 1 # devuelve el boolean de la comparacion osea true o false

    except redis.RedisError as e:
        print(f"An error ocurred while deleting data from Redis: {e}")
        return False
    
# result = delete_data("full_name")
# print("Result:", result)


# ***Funciones para eliminar datos keys que tengan un patrón específico en su nombre***
# for key in redis_client.scan_iter("getUsers:*"):
#     redis_client.delete(key)

def delete_data_with_pattern(pattern):

    try:
        for key in redis_client.scan_iter(pattern):
            delete_data(key)
    except redis.RedisError as e:
        print(f"An error ocurred while deleting data from Redis: {e}")


delete_data_with_pattern("getUsers:*")


#Falta seccion de limpiar el codigo


