with open('/etc/passwd') as f:
    for l in f:
        user, pswd, id_u, id_g, com, home, shell = l.split(':')
        print( "USER    = %s" % user )
        print( "UID     = %s" % id_u )
        print( "GID     = %s" % id_g )
        print( "COMMENT = %s" % com )
        print( "HOME    = %s" % home )
        print( "SHELL   = %s" % shell )