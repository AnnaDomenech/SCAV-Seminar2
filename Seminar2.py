import os
from pathlib import Path

class iodir:
    inp : str
    outp : str
    def __init__(self,inp,outp):
        self.inp=inp
        self.outp=outp

def setDir():
    name = "BBB.mp4"
    input_path= Path.cwd()#get current directory
    #for each file in folder get input path (Lenna.jpg)
    file_path= [ subp for subp in input_path.iterdir() if subp.match(name)]
    file_path.sort()
    output_path =  Path.cwd() / "Results"#set output folder path 
    output_path.mkdir(parents=True, exist_ok=True)# create it 
    return iodir(str(file_path[0].name),output_path)

#Exercice 1
def one():
    init= input("Insert start time in XX:XX:XX format::\n")
    output = str(dyr.outp / "BBBc.mp4")#set output video name
    command = f"ffmpeg -ss {init} -i {dyr.inp} -t 00:00:10 -c copy {output}"#ffmpeg command
    os.system(command)
    dyr.inp = output #change input dir to work with the cutted video
    return "Done"

#Exercice 2 
def two():
    output = str(dyr.outp / "yuv_histogram.mp4")#set output video name and path
    command = f"ffplay {dyr.inp} -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay "#ffmpeg command
    os.system(command)
    return "Done"

#Exercice 3
def three():
    iscale=int(input("\nChoose a new size:\n[0]720\n[1]480\n[2]360x240\n[3]160x120\n"))
    scale = ['-2:720','-2:480','360:240','160:120']#The different options to resize the video
    output = str(dyr.outp / "BBB_resize{}.mp4".format(scale[iscale]))#set output video name and path
    command = f"ffmpeg -i {dyr.inp} -vf scale={scale[iscale]} -c:a copy {output}"#ffmpeg command
    os.system(command)
    return "Done"

#Exercice 4
def four():
    output = str(dyr.outp / "BBB_mono.mp3")#set output video name and path
    command = f"ffmpeg -i {dyr.inp} -acodec mp3 -ac 1 {output}"#ffmpeg command
    os.system(command)
    return "Done"

def execall(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()

switcher = {
        1: one,
        2: two,
        3: three,
        4: four
    }

if __name__ == "__main__": 
    dyr=setDir()#set directories
    x = input("[1]Cut the video\n[2]Visualize YUV histogram\n[3]Resize the video\n[4]Stereo to Mono\n")
    while not x=='5':
        print(execall(int(x)))
        x = input("[1]Cut the video\n[2]Visualize YUV histogram\n[3]Resize the video\n[4]Stereo to Mono\n[5]Exit\n")
        

            
    
   