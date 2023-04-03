# https://flywaydb.org/documentation/learnmore/existing
# https://arctype.com/blog/sql-python/
# https://thorben-janssen.com/flyway-migration-existing-database/
 
from pathlib import Path
import subprocess 

def extract_ddl(env_vars):
     
    path_obj = Path('scripts/'+env_vars['database'])
    if not path_obj.is_dir():
        print("dir is not present creating one ")
        path_obj.mkdir(mode=0o777, parents=False, exist_ok=False)
    
    sql_path = str(path_obj)+"/V1__baseline.sql"
    password =  env_vars['DB_PASSWORD']
    command_list =  [
        'mysqldump', '-d',
        '-u','root', 
        '-h',  env_vars['DB_HOSTNAME'] , 
         env_vars['database'] ,  
         '-p',  password  ]
    print(f" inside extract ddl : command_list {command_list}  ")
    proc = subprocess.Popen(command_list, stdout=sql_path, shell=True)
    try:
        outs, errs = proc.communicate(timeout=1500)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    finally:
        print(f"errs {errs}")
        print(f"outs {outs}")
        print(f"args file {env_vars}")
    # username = env_vars['DB_USER']
    
    # database = env_vars['database']
    # another_list = ['mysqldump','-d', '-h',env_vars['DB_HOSTNAME'], '-u',username,'-p%s'%password,database]
    # print(f" another command list {another_list}")

    # with open(sql_path,'w') as output:
    #     c = subprocess.Popen(another_list,
    #                         stdout=output, shell=True)