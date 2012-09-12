"""Specify a root folder where all your tv-series episodes are located. 
Add or remove media file extensions as required in the list called video_extension.
The script opens a random media clip using the player specified"""

import os,commands,random

#editable parameters
source_folder	= "/media/MEDIA/FRIENDS"	#location of root folder
video_extension = ["mkv", "avi"]		#extensions to search for
media_player	= "vlc"				#what to open the media file with

#local variables
find_args 	= source_folder + " -type f"	
find_command	= "find"

for i in range(len(video_extension)):
   if(i == 0):
      find_args += " -name *\." + video_extension[i]
   else:
      find_args += " -o -name *\." + video_extension[i]
	
find_command += (" " + find_args)
filenames = commands.getoutput(find_command).split('\n')
episode_number = int( random.uniform(1,len(filenames)) )

#print find_command
#finally run vlc with the generated path

os.system(media_player + " \"" + filenames[episode_number] + "\"")


