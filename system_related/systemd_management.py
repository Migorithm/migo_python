#############################################################################################################
# Prerequisites
# pip install pystemd
# 
# This allows you to programmatically start/stop/restart/kill and verify services status 
# from systemd point of view, avoiding executing "subprocess.Popen(["systemctl",...]" 
#############################################################################################################
import os
import argparse
from pystemd.systemd1 import Unit #1 is not typo..

parser = argparse.ArgumentParser()
parser.add_argument("-s","--service",required=True)
parser.add_argument("-r","--restart",action="store_true")
parser.add_argument("-s","--start",action="store_true")
parser.add_argument("-p","--pause",action="store_true")

args=parser.parse_args()
service_name=args.service #should be, for example, "redis@6379.service"


def full_example():
    with Unit('{service_name}'.encode()) as sd_unit:
        #Check activeness
        if sd_unit.Unit.ActiveState == b"active":
            print("{service_name} is active Now")

            print("ConditionTimestamp", sd_unit.Unit.ConditionTimestamp)
            print("StopWhenUnneeded", sd_unit.Unit.StopWhenUnneeded)
            print("StartLimitAction", sd_unit.Unit.StartLimitAction)
            print("StartLimitBurst", sd_unit.Unit.StartLimitBurst)
            print("StartupBlockIOWeight", sd_unit.Service.StartupBlockIOWeight)
            print("SyslogPriority", sd_unit.Service.SyslogPriority)
            print("SyslogFacility", sd_unit.Service.SyslogFacility)
            print("SyslogLevelPrefix", sd_unit.Service.SyslogLevelPrefix)
            print("After", sd_unit.Unit.After)
            print("Conditions", sd_unit.Unit.Conditions)
            print("Job", sd_unit.Unit.Job)
            print("InvocationID", sd_unit.Unit.InvocationID)
            print("ExecStart", sd_unit.Service.ExecStart)

            # next one require sudo powers!
            if os.geteuid() == 0: #If it's root
                print(".GetProcesses", sd_unit.Service.GetProcesses())
                print(".Start(b'replace')", sd_unit.Unit.Start(b"replace"))
                print(".Stop(b'replace')",sd_unit.Unit.Stop('replace')) # require privilege account
                print(".Restart(b'replace')",sd_unit.Unit.Restart('replace'))
            else:
                print("no root user, no complex method for you!")
        else:
            if os.geteuid() ==0 :
                print(f"{service_name} is inactive! Reboot...") 
                print(".Start(b'replace')", sd_unit.Unit.Start(b"replace"))
            else:
                print(f"{service_name} is inactive! But you're not permitted to spin it up.") 


def find_service(service):
    from pystemd.systemd1 import manager
    manager = manager.Manager()
    manager.load()
    list_of_service= list(filter(lambda x:f"{service}".encode() in x[0] , manager.Manager.ListUnits()))

    
    
class AgentUtils:
    logging.basicConfig(filename="/var/log/vertica-agent/agent.log",level=logging.DEBUG)
    
    AGENT_KEY=os.getenv("AGENT_KEY")
    #Service loading
    def __new__(cls):
        return cls

    @classmethod
    def load_service(cls):
        from pystemd.systemd1 import Unit,manager
        mng = manager.Manager()
        mng.load()
        regex = re.compile(r"redis.*service|elastic.*service|kafka.*service")
        services= list(filter(lambda x: regex.match(x[0].decode('utf-8')), mng.Manager.ListUnits()))
        cls.services={}
        
        for service in services:
            serv = service[0].decode('utf-8')
            service_name= re.sub(r"[@.]",r"_",serv).upper() 
            unit=Unit(service[0].decode("utf-8"))
            unit.load()
            unit=unit.Unit
            setattr(AgentUtils,service_name,unit)
            #Put unit first so you can get the state of unit synchronously.