from cache import CacheManager

cache_manager = CacheManager(
    host="redis-18018.c44.us-east-1-2.ec2.cloud.redislabs.com",
    port= 18018,
    password= "8WOPf1mmHS5kJEeS4ecLJJ2Sg2ACFyQ9",
)

cache_manager.store_data("full_name", "John Doe")
cache_manager.store_data("important_key", "Important Value!", time_to_live=100)