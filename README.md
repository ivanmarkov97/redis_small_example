## Redis small project

Steps:

- pip install -r requirements.txt
- python app.py

### Adding users to redis:

Every user identified by login & password
- hset user:{username} password {password} // OK
- hget user:{username} password // {password}
- ttl user:{username} // -1
- keys user:* // {username}

read more about redis: https://redislabs.com/
