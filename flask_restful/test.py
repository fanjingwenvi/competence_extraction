
## os.environ['FLASK_APP'] = 'api.py'
env_var = 'FLASK_APP'
def check_env_var(env_var):
    env_value = os.environ.get(env_var)
    print(env_value)
## check_env_var(env_var)




