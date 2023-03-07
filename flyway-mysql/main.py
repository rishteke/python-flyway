
from argparse import ArgumentParser
from .config import construct_params
import subprocess

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


    args = parser.parse_args()

    env_vars = construct_params(args)
    command_list = ["docker", "run", "--rm", "-v", "/home/ubuntu/flyway-test/MYSQL:/flyway/sql", "-v", "/home/ubuntu/flyway-test/jars:/flyway/drivers", "flyway/flyway", "-url=jdbc:mysql://172.18.96.1:3306/?db=flywaydbtest", "-schemas=test1", "-user=root", "-password=root","migrate"
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

    

    