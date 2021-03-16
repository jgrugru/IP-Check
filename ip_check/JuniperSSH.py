import paramiko
from decouple import AutoConfig

ENV_DIR_PATH = "/home/jgruenbaum/Desktop/programming_projects/IP-Check/env"
config = AutoConfig(ENV_DIR_PATH)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    config("JUNIPER_HOSTNAME"),
    username=config("JUNIPER_USERNAME"),
    password=config("JUNIPER_PASSWORD"))

print(vars(ssh))

ssh.close()