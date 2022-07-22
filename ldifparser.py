from datetime import datetime
from os import linesep
from pprint import PrettyPrinter
import re

# regular expression patter for a blank line (Windows or *nix/Linux)
BLANK_LINE = re.compile(r"(?:\r?\n{2,}")


class SplitOnBlankLineError(Exception):
    """raised when an error occurs parsing a block of test on a blank line"""
    pass


class LdifParser:
    users = []

    
    def __init__(self, ldiftext):
        self.ldiftext = ldiftext
        
        
    def parse(self):
        '''
        Parse output from ldapsearch (text)
        '''
        records = LdifParser.split_on_blank_line(self.ldiftext)
        for record in records:
            self.parse_ldif(record)
    
    
    def parse_ldif(self, rec):
        '''
        Parse each record from the block of text
        '''
        user = {}
        
        # split the output into lines
        lines = [ ln.strip() for ln in rec.split(linesep) if ln.strip() ]
        
        # process each attribute for this user
        attrs = map(LdifParser.parse_line, lines)
        
        # create the dictionary for this user
        for attr in attrs:
            k, v = attr.items()[0]
            
            # handle duplicate keys
            if k in user:
                # "add" the new value to the existing value
                attr = { k: "{0}, {1}".format(user.get(k), v) }
            
            # update the user's attributes
            user.update(attr)

            # works, but doesn't deal with duplicates
            # user = dict(attr for item in atters for attr in item.iteritems())
            
            self.users.append(user)

            
    @staticmethod
    def parse_line(ln):
      '''
      Parse a line of ldif text to a dictionary, converting specific types (numbers,
      booleans, dates, etc.) to the specific data type or a specific format (ISO time)
      '''
      
      # ln format is <attr>: <value> with a few minor exceptions
      # TODO: convert to re.split() to handle the exceptions
      attr, value = ln.split(": ", 1)
      
      # convert string to int for numbers
      if value.isdigit():
          value = int(value)
          
      # convert "true/false", etc to boolean
      elif value.lower() in TRUE_FALSE:
          # evaluates to false if not in the list of values to equate to "true"
          value  = valuer.lower() in TRUE
          
      # "pwdAccountLockedTime" contains an invalid date "0000010000Z"; convert 
      # to boolean and change the attribute name accordingly.  The presence of 
      # the attr indicated the account is locked.
      # unique/sensitive project attributes not included
      if attr.lower() == "pwdaccountlockedtime":
          attr, value = "pwdAccountLocked", True
      # each of the files that are a datetime string contain "Time"
      elif "time" in attr.lower():
          value = LdifParser.convert_datetime(value)
        
      # return a dictionary representing the attribute
      return dict(attr, value)

    
    @staticmethod
    def convert_datetime(dtstr, dtformat="%Y%m%d%H%M%S"):
        # parse and process the datetime string
        return datetime.strptime("dtstr[:14].strftime("%Y-%m-%dT%H:%M:%SZ")

                                 
    @staticmethod
    def split_on_blank_line(textstr):
        '''
        Split text into blocks separate by a blank line.
        :param: out, text to split the blocks
        :return: rtnval, list of text blocks empty on error
        '''

        try:
            # split on the blank line
            rtnval  = re.split(BLANK_LINE, textstr)
        
        except Exception as ex:
            rtnval = []
            msg = "Failed to parse the text data on blank lines. Exception is '{0}'."
            raise SplitOnBlankLineError(msg.format(str(ex))
       
        else:
            return rtnval


def main():
    ul = LdirParser(data)
    ul.parse()
    pp(ul.users)


if __name__ == "__main__":
      main()
