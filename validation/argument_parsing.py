import argparse

#initializer
parser = argparse.ArgumentParser()

#Add argument - when values are required
parser.add_argument("-p","--prefix",required=True,help="Specify prefix with which the key start.")
parser.add_argument("-b","--bootstrap_server",required=True,help="Specify the path to serverlist file")

#Add argument - when values are not required
    # here, action="store_true" means default is set False
parser.add_argument("-r","--restart",action="store_true")
parser.add_argument("-s","--start",action="store_true")
parser.add_argument("-p","--pause",action="store_true")

#Get args
args = parser.parse_args()

auth=args.auth
servers=args.bootstrap_server
prefix=args.prefix
mode=args.mode
usecase=args.usecase




args=parser.parse_args()