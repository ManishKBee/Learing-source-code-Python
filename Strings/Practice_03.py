# python code to replace double space with NO space

DM='''Digital  marketing  is  the  use  of  
the  Internet  to  reach  consumers.  
Digital  marketing  is  a  broad  field,  
including  attracting  customers  via  
email,  content  marketing,  search  
platforms,  social  media,  and  more.'''

print(DM.find("  ")) # for detecting the double space

DM=DM.replace("  ","") # for replacing the double space with NO space

print(DM)