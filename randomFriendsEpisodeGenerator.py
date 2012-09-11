#!/bin/env python

import os,commands,random

#editable parameters
friends_folder 	= '/media/MEDIA/FRIENDS'	#location of root folder
video_extension = ["mkv", "avi"]		#extensions to search for

#local variables
find_args 	= friends_folder + " -type f"	
find_command	= "find"

for i in range(len(video_extension)):
   if(i == 0):
      find_args += " -name *\." + video_extension[i]
   else:
      find_args += " -o -name *\." + video_extension[i]
	
find_command += (" " + find_args)
filenames = commands.getoutput(find_command).split('\n')
episode_number = int( random.uniform(1,len(filenames)) )

#finally run vlc with the generated path
os.system("vlc \"" + filenames[episode_number] + "\"")


