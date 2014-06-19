#!/usr/bin/env python
import sys
import re
import os

class ChatServer():

    def __init__(self):        
        pass
        
    def action(self, args):
        #sys.stdout.write(result)
        pass

        
def main():       
    try:
        chatServer = ChatServer()
        while (chatServer is not None):
            chatline = sys.stdin.readline()
            chatServer.action(chatline)
        
    except:
        print "Unexpected error"
    return 0
    
if __name__ == "__main__":
    try:
        e = main() #sys.exit(main(*sys.argv))
    except:
        print "Exiting with error: ", e
