from gtkforms import *


opts = options()\
                .add('userid', label="Login Name", value= "")\
                .add('password', label="Password", value= "*")\
                .add('remember', label="Remember", value= True)
print ("before...")
print ("pippo=\t\t" + str(opts.userid))    
print ("pluto=\t\t" + str(opts.password))    
print ("paperino=\t"+ str(opts.remember))
create_gtk_dialog(opts).run()
print ("...after")
print ("pippo=\t\t" + str(opts.userid))    
print ("pluto=\t\t" + str(opts.password))    
print ("paperino=\t"+ str(opts.remember))
        
