# import stuff
from os import listdir, rename, scandir

# automatically rename entire shows
for folder in scandir("."): 
    if folder.is_dir(): #make sure random files aren't inlcuded
        show = folder.name
        for season in scandir(folder):
            if season.name.lower().startswith("season"): # make sure we only get season folders
                sea = season.name.lower()[7:]
                ep = 1
                for episode in scandir(season):
                    if episode.endswith("mkv") or episode.endswith("mp4") or episode.endswith("webm"): # make sure we target media files
                        # format episode number
                        if ep < 10:
                            eps = f"0{ep}"
                        else:
                            eps = f"{ep}"

                        rename(episode, f"{show} - s{sea}e{eps}.{episode.name.split('.')[-1]}")
                        ep += 1