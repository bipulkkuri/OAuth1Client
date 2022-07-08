
# pip3 install requests_oauthlib

#########################################################################
# install pip3 install requests_oauthlib
# python3 oa1p.py --h                                                                  
# usage: oa1p.py [-h] --k K --s S --u U [--f F]

# optional arguments:
#   -h, --help  show this help message and exit
#   --k K       ConsumerKey
#   --s S       ConsumerSecret
#   --u U       url
#   --f F       optional path to json payload file does a Post call to URL
###########################################################################

from requests_oauthlib import OAuth1Session
import sys 
import argparse


def readFile(f):
    file = open(f,mode='r')
    all_of_it = file.read()
    file.close()
    return all_of_it

def run(k,s,u,f):
    print("Found ",k,s,u,f)
    test = OAuth1Session(k,client_secret=s)
    r=""
    if(f):
        myjson=readFile(f)
        r = test.post(u,json=myjson)
    else:
        r = test.get(u)
    print ("Response: ",r.content)

def main(argv):

    # Create the parser
    parser = argparse.ArgumentParser()# Add an argument
    # Parse the argument
    parser.add_argument('--k', type=str, required=True,help='ConsumerKey')
    parser.add_argument('--s', type=str, required=True,help='ConsumerSecret') 
    parser.add_argument('--u', type=str, required=True,help='url') 
    parser.add_argument('--f', type=str, required=False,help='optional path to json payload file does a Post call to URL')
    args = parser.parse_args()

    run(args.k,args.s,args.u,args.f)
if __name__ == "__main__":
   main(sys.argv[1:])
 
