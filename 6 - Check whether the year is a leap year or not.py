year = 2016
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} \n yes".format(year))
       else:
           print("{0} \n no".format(year))
   else:
       print("{0} \n yes".format(year))
else:
   print("{0} \n no".format(year))
