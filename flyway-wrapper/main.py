
from argparse import ArgumentParser
from .config import construct_params
import subprocess
import sys

def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-f", "--env_file", 
        dest="filename",
        help="env file to read credentials", metavar="FILE")
    parser.add_argument(
        "-s", "--schema" ,
        dest="schema", 
        help="schema used in flyway commandline changes")
    parser.add_argument(
        "-db", "--database" ,
        dest="database", 
        help="database used in flyway commandline changes")
    parser.add_argument(
            "-fc", "--flyway_command" ,
            dest="flyway_command", 
            help="flyway_command used in flyway commandline changes")


    args = parser.parse_args()

    env_vars = construct_params(args)
    print(f"\n________________{env_vars}\n")
    print(f"\n________________{'-url=jdbc:mysql://'+env_vars['DB_HOSTNAME']+':3306/?db='+env_vars['database']}\n")

    if env_vars["flyway_command"] == 'baseline':
        print(" its not implemented yet ")
        sys.exit(0)
    
    
    command_list = [
        "docker", "run", "--rm", 
        "-v", "/home/ubuntu/python-flyway/scripts/"+env_vars['database']+":/flyway/sql",
        "-v", "/home/ubuntu/python-flyway/jars:/flyway/drivers", 
        "flyway/flyway", "-url=jdbc:mysql://"+env_vars['DB_HOSTNAME']+":3306/?db="+env_vars['database'] , 
        "-schemas="+env_vars['schema'],
        "-user=root", 
        "-password=root",env_vars["flyway_command"]
 ]

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


    # try:
    #     #         import shlex, subprocess
    #     # command_line = input()
    #     # /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
    #     # args = shlex.split(command_line)
    #     # print(args)
    #     # ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
    #     # p = subprocess.Popen(args) # Success!
    #     print("first line")
    #     print(f"args {args}")
    #     print(f"args file {env_vars}")
    # except e:
    #     raise e

    

    