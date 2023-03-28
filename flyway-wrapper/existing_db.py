# https://flywaydb.org/documentation/learnmore/existing
# https://arctype.com/blog/sql-python/
# https://thorben-janssen.com/flyway-migration-existing-database/
 

def extract_ddl(env):
    command_list =  ["mysqldump","-d ","-u"," root", "-h"," 172.30.240.1", "adventureworks","--password='root'",">","V1_baseline.sql" ]

    proc = subprocess.Popen(command_list)
    try:
        outs, errs = proc.communicate(timeout=1500)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    finally:
        print(f"errs {errs}")
        print(f"outs {outs}")
        print(f"args file {env_vars}")
