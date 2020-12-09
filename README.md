# SCAV-Lab2
We assume that in the project folder there is the needed data.
The first step is initialize the directories with iodir class:
- inp: Will save the video path
- outp: Will save the Results folder directory
## Exercice 1:
In this exercice our goal is being able to cut a video. We have contraint the duration of the video to 10s, but the user is able to decide where to init the cut.
Notice that once we have cutted the video, we update the input path of the iodir instance to work with the cutted video:
```
    init= input("Insert start time in XX:XX:XX format::\n")
    output = str(dyr.outp / "BBBc.mp4")#set output video name
    command = f"ffmpeg -ss {init} -i {dyr.inp} -t 00:00:10 -c copy {output}"#ffmpeg command
    os.system(command)
    dyr.inp = output
```
## Exercice 2:
In this exercice our goal is being able to see the video at the same time that the yuv histogram, in order to do that we have used the following ffmpeg command:
```
 command = f"ffplay {dyr.inp} -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay "
```
## Exercice 3:
In this exercice our goal is being able to change the resolution of the video, the options are:
- 720p or 480p 
- 360x240 or 160x120

When we choose the first option we scale the video using -2:720 to avoid errors. Once the user has indicated which new resolution wants we do:
```
    output = str(dyr.outp / "BBB_resize{}.mp4".format(scale[iscale]))#set output video name and path
    command = f"ffmpeg -i {dyr.inp} -vf scale={scale[iscale]} -c:a copy {output}"#ffmpeg command
```
## Exercice 4:
In this exercice our goal is extract the audio from the video and convert it to mono, we had used the following command:
```
    output = str(dyr.outp / "BBB_mono.mp3")#set output video name and path
    command = f"ffmpeg -i {dyr.inp} -acodec mp3 -ac 1 {output}"#ffmpeg command
```
## Exercice 5:
In order to put all the previous exercice into a script, we have implemented a switch that is mainly implemented using the following lines:
```
switcher = {
        1: one,
        2: two,
        3: three,
        4: four
    }
```   
First we define the different options which corresponds with the proposed exercices. Then, we will name each exercice function as one(), two(),etc. Finally we have to define a function that returns the desired exercice function by means of an index:
```
def execall(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
```
The index to define the exercice to call is entered by the user in the main:
```
if __name__ == "__main__": 
    dyr=setDir()#set directories
    x = input("[1]Cut the video\n[2]Visualize YUV histogram\n[3]Resize the video\n[4]Stereo to Mono\n")
    while not x=='5':
        print(execall(int(x)))
        x = input("[1]Cut the video\n[2]Visualize YUV histogram\n[3]Resize the video\n[4]Stereo to Mono\n[5]Exit\n")
