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

def one():
    output = str(dyr.outp / "BBBc.mp4")#set output image name
    command = f"ffmpeg -ss 00:05:00 -i {dyr.inp} -t 00:00:10 -c copy {output}"#ffmpeg command
    os.system(command)
    return "Done"
 
def two():
    command = f"ffplay {dyr.inp} -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"#ffmpeg command
    os.system(command)
    return "Done"
 
def three():
    # aux = input("New size")
    output = str(dyr.outp / "BBB_mono2.mp3")
    command = f"ffmpeg -i {dyr.inp} -vf scale=160:120 -c:a copy {output}"#ffmpeg command
    os.system(command)
    return "Done"

def four():
    output = str(dyr.outp / "BBB_mono2.mp3")
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
    x = input("[1]Cut the video\n[2]Visualize YUV histogram\n[3]Convert the video\n")
    while not x=='4':
        execall(int(x))
        x = input("[1]Cut the video\n[2]Visualize YUV histogram\n[3]Convert the video\n")
        

            
    
   