from fireREST import FMC
from decouple import config

fmc = FMC(hostname=config("HOSTNAME"), username=config("USERNAME"), password=config("PASSWORD"), domain='Global')
print(fmc.object.network.get())