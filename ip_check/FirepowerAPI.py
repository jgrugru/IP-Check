from fireREST import FMC
from decouple import AutoConfig

ENV_DIR_PATH = "/home/jgruenbaum/Desktop/programming_projects/IP-Check/env"
config = AutoConfig(search_path=ENV_DIR_PATH)

fmc = FMC(
    hostname=config("FIREPOWER_HOSTNAME"),
    username=config("FIREPOWER_USERNAME"),
    password=config("FIREPOWER_PASSWORD"),
    domain='Global')
    
print(fmc.object.network.get())
