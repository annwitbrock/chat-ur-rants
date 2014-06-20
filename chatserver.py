#!/usr/bin/env python
import sys
import re
import os

class ChatServer():

    def __init__(self):        
        self.chatroom = {}
        
    def action(self, args):
        args = args.strip()
        line = args.split(' ')
        user = line[0]
        if user not in self.chatroom:
            self.chatroom[user] = []

        result = ""
        if len(line) == 1:
            for message in self.chatroom[user]:
                result += user + ' - ' + message[0] + os.linesep
            return result
        
        if '->' in args:
            self.chatroom[user].append((' '.join(line[2:]),))
            return result
                
        return result


        
def main():       
    try:
        chatServer = ChatServer()
        while (chatServer is not None):
            chatline = sys.stdin.readline()
            messages = chatServer.action(chatline)
            sys.stdout.write(messages)
        
    except:
        print "Unexpected error"
    return 0
    
if __name__ == "__main__":
    try:
        e = main() #sys.exit(main(*sys.argv))
    except:
        print "Exiting with error: ", e
