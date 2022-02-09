#############################################################################################################
# Prerequisites
# pip install pystemd
# 
# This allows you to programmatically start/stop/restart/kill and verify services status 
# from systemd point of view, avoiding executing "subprocess.Popen(["systemctl",...]" 
#############################################################################################################
import os
import argparse
from pystemd.systemd1 import Unit

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


       