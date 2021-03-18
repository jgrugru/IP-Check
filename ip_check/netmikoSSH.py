
from netmiko import ConnectHandler
# from netmiko import juniper
from decouple import AutoConfig

ENV_DIR_PATH = "/home/jgruenbaum/Desktop/programming_projects/IP-Check/env"
config = AutoConfig(ENV_DIR_PATH)

lab_srx_junos = {
    'device_type': 'juniper_junos',
    'ip': config("JUNIPER_HOSTNAME"),
    'username': config("JUNIPER_USERNAME"),
    'password': config("JUNIPER_PASSWORD")
}

output = ''
net_connect = ConnectHandler(
    **lab_srx_junos,
    fast_cli=True,
    session_log=config("SESSION_LOG_PATH"))

# if net_connect.is_alive():
#     print("**********************\n"
#           "Connection is active, starting script.")
# else:
#     print("**********************\n"
#           "Connection is not active, exiting script.")

output += net_connect.send_command('show system users')
output += net_connect.config_mode()
print("config mode?", net_connect.check_config_mode())
output += net_connect.send_command(
    'set policy-options prefix-list '
    + 'ALLOW_ICMP_FROM_SOURCES 167.224.81.15/32')
output += net_connect.send_command('show | compare')
output += net_connect.commit(confirm_delay=1, confirm=True)
output += net_connect.exit_config_mode()
print("is alive? ", net_connect.is_alive())
print(output)
