# LdapSearch
Wrapper for the ldapsearch command for older Sun/Oracle DS

We are limited to the python installation within our very, very old Solaris 10 operating system; updating the distribution is not an option and features default install of Python 2.6.4 in most cases and when we're really luck 2.7.5!  Had to find a way to retrive the data from the Directory Server (LDAP) using only the "ldapsearch" command.  While there is a web interface for the data it is stored in a MySQL database which has no indexes and is inaccessible to the average user.  The web interface can take 15+ to login and retrieve a record for a single user and viewing the interface for multiple user is not possible.

We decided to pull the data for all users, parse it to JSON and push it into Elasticsearch; as a result, we can retrieve the data in numerous ways and retrieve and individual user's information in less then .7 seconds in > 20,000 records.

In a new system we're standing up, we're using Red Hat Linux and for the moment, I'm using the default 2.7 until we fully define the software baseline and can update to Python 3.

Constructive criticism is welcomed.
