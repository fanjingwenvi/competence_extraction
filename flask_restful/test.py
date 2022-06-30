import os

## os.environ['DATABASE_USERNAME'] = 'neo4j'

env_var = 'DATABASE_USERNAME'
def check_env_var(env_var):
    env_value = os.environ.get('env_var')
    print(env_value)
check_env_var(env_var)