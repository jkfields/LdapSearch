#!/usr/bin/env python

import platform
from subprocess import Popen, PIPE

# TODO:  push these to config file
LINUX_CMD = ""
SOL_CMD = ""

class InvalidLdapSearchCommandException(Exception):
    pass
    

class LdapSearch:
    def __init__(self, url):
        self.__url = url
        
        if platform.system().lower() == "linux":
            self.__cmd = LINUX_CMD
        else
            self.__cmd = SOL_CMD
            
    def search(self, basedn, filter, attrs):
        pass
        
    @static
    def dtToIso(dt):
        
