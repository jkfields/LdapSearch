"""
.. codeauthor:: Jeffrey Fields <jkfields@yahoo.com>
"""

import platform
from subprocess import Popen, PIPE

# TODO:  push these to config file
LINUX_CMD = "/bin/ldapsearch -LLL -o ldif-wrap=no -xH {url} -b {dn} {filter} {attrs}"
SOL_CMD = "/usr/bin/ldapsearch -T -x -h {url} -b {dn} {filter} {attrs}"

class InvalidLdapSearchCommandException(Exception):
    pass
    
class LdapSearch:
    def __init__(self, url):
        self.__url = url
        self.__system = platform.system().lower() 
        
        if self.__system == "sunos":
            self.__cmd = SOL_CMD
        else if
            self.__cmd = LINUX_CMD
            
    def search(self, dn, filter, attrs):
        __cmd = self.__cmd.format(url=self.__url,
                                  dn=dn,
                                  filter=filter,
                                  attrs=attrs)
        __proc = Popen(__cmd.split(), shell=False, stdout=PIPE, stderr=PIPE)
        __out, __err = __proc.communicate()
        __rtncode = __proc.returncode
        
        if __rtncode == 0:
            return __out
        else:
            raise InvalidLdapSeachCommandException("{rtncode}::{msg}".format(rtn_code=__rtncode,
                                                                             msg= __err)
