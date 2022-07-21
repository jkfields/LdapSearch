"""
.. codeauthor:: Jeffrey Fields <jkfields@yahoo.com>
"""

import platform
from subprocess import Popen, PIPE

# TODO:  push these to config file
DEFAULT_HOST = "ldap1"
DEFAULT_PORT = 389
DEFAULT_BASEDN = "ou=people,ou=systems,dc=dc1,dc=dc2,dc=dc3,dc=dc4"
DEFAULT_FILTER = "(objectClass=person)"
DEFAULT_ATTRS = "sn givenName middleName uid uidNumber gid gidNumber telephoneNumber email"

LINUX_CMD = "/bin/ldapsearch -LLL -o ldif-wrap=no -xH {url} -b {dn} {filter} {attrs}"
SOL_CMD = "/usr/bin/ldapsearch -T1h {url} -b {dn} {filter} {attrs}"


class LdapSearchError(Exception):
    """Raised when an error occues executing the ldapsearch"""
    pass
    

class ShellExecutionError(Exception):
    """Raised when an error occurs executing a shell command"
    pass


class LdapSearch:
    system = platform.system().lower()


    def __init__(self, host, port=389):
        self.host = host
        self.port = port 
        
        if self.system == "sunos":
            self.ldapssearch = SOL_CMD
        elif
            self.ldapsearch = LINUX_CMD
        else:
            msg = "{0} is not a supported system".format(self.system)
            raise LdapSearchError(msg)


    def __str__(self):
        # TODO
        pass


    def search(self, dn=DEFAULT_BASEDN, filter=DEFAULT_FILTER, attrs=DEFAULT_ATTRS):
       if self.system == "sunos":
           cmd = self.ldapsearch.format(host=self.host,
                                        dn=dn,
                                        filter=filter,
                                        attrs=attrs)
        else:
            cmd = self.ldapsearch.format(uri="ldap:\\{0}:{1}".format(self.host, self.port),
                                         dn=dn,
                                         filter=filter,
                                         attrs=attrs)
        self.ldif = LdapSearch.shex(cmd)


    @staticmethod
    def shex(cmd):
        try:
            proc = Popen(__cmd.split(), shell=False, stdout=PIPE, stderr=PIPE)
            out, err = proc.communicate()
            rtncode = proc.returncode
            
        except  Exception as ex:
            out = ""
            msg = "Execution failed; return code: {0}.  {1}.format(rtncode, str(ex))
            raise ShellExecutionError(msg)
            
        else:
            if rtncode == 0:
                return out
            else:
                msg = "Execution failed; return code: {0}.   {1}.format(rtncode, err)
                raise ShellExecutionError(msg)

if __name__ == "__main__":
    ls = LdapSearch(HOST, PORT)
    ls.search(DEFAULT_BASEDN, DEFAULT_FILTER, DEFAULT_ATTRS)
    
    print(ls.ldif)
