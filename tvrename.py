# import stuff
from os import rename, scandir

# automatically rename entire shows
for folder in scandir("."): 
    if folder.is_dir(): #make sure random files aren't inlcuded
        show = folder.name
        for season in scandir(folder):
            if season.name.lower().startswith("season"): # make sure we only get season folders
                sea = season.name.lower()[7:]
                ep = 1
                for episode in scandir(season):
                    if episode.name.endswith("mkv") or episode.name.endswith("mp4") or episode.name.endswith("webm"): # make sure we target media files
                        # format episode number
                        if ep < 10:
                            eps = f"0{ep}"
                        else:
                            eps = f"{ep}"
                            
                        path = "\\".join(episode.path.split("\\")[:3])
                        rename(episode, f"{path}/{show} - s{sea}e{eps}.{episode.name.split('.')[-1]}")
                        ep += 1
