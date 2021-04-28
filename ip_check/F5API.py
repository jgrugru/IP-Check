from decouple import AutoConfig
from f5.bigip import ManagementRoot
# config("FIREPOWER_HOSTNAME"),

ENV_DIR_PATH = "/home/jgruenbaum/Desktop/programming_projects/IP-Check/env"
config = AutoConfig(search_path=ENV_DIR_PATH)

mgmt = ManagementRoot(
  'mcq-acilb701.teleflora.org',
  config('FIREPOWER_USERNAME'),
  config('FIREPOWER_PASSWORD'))


def showDatagroups():
    print("\n\n**** Showing Datagroups")
    dgs = mgmt.tm.ltm.data_group.externals.get_collection()
    for idx, dg in enumerate(dgs):
        print("\n{}: {}".format(idx, dg.raw))
        print("\n{}: {}".format(idx, dg.name))
        if hasattr(dg, 'records'):
            print("\n{}: {}".format(idx, dg.records))
            for record in dg.records:
                print("\nrec: {}".format(record))
        else:
            print("\nObject {} has no records".format(dg.name))


def showDatagroupFiles():
    print("\n\n**** Showing DatagroupFiles")
    dgFiles = mgmt.tm.sys.file.data_groups.get_collection()
    for idx, f in enumerate(dgFiles):
        print('\n{}: {}'.format(idx, f.raw))


showDatagroupFiles()
