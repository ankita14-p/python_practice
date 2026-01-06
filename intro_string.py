#string
name="harry"

#string is immutable 
#string length
print(len(name))

#string slicing
#name[ind_start:ind_end:step] --> ind_end is not included
name_short=name[0:3]
print(name_short)
#name[:ind_end]--> ind_staert is considerred as 0
#name[ind_start:]--> ind_end is considered as len(name)
