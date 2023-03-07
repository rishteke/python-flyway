import os
from dotenv import load_dotenv
from pathlib import Path



def read_env_file(filename):
     
    load_dotenv(dotenv_path=filename)
    env = {}

    env['DB_HOSTNAME']= os.getenv('DB_HOSTNAME')
    env['DB_USER']= os.getenv('DB_USER')
    env['DB_PASSWORD']= os.getenv('DB_PASSWORD')
    env['DB_PORT']= os.getenv('DB_PORT')

    return env

def construct_params(cmd_arguments):
    # dotenv_path = Path(filename)
    print(f"cmd_arguments {cmd_arguments}")
    env_var = {}
    file_name =  cmd_arguments.filename if cmd_arguments.filename else '.env'
    print(f"file_name {file_name}")
    
    dotenv_path = Path(file_name)
    if not dotenv_path.exists():
        raise "Unable to find credentials file."
 

    db_vars = read_env_file(dotenv_path)
    print(f"db_vars {db_vars}")

    env_var['schema'] = cmd_arguments.schema if cmd_arguments.schema else "public"
    # env_var['flyway_command'] = cmd_arguments.flyway_command if cmd_arguments.flyway_command else "migrate" 
    print(f"env_var {env_var}")

    return {**env_var, **db_vars} 
