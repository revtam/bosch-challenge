## Automotive

Automotive is a runtime environment built to test your code for the bosch hackathon
challenge. It enables you to use any programming language as long as you provide the executable, and your work’s entry file. To use the runtime environment, open a new
terminal window (eg. cmd, Powershell, or a linux terminal emulator) and navigate to the folder where the environment is located.

Eg. If you're os is x64 Windows then you'll need `windows/64bit/automotive.exe`

## Challenges

For each task, you'll have to implement a program that will be tested against
the requirements. You can either provide an already executable (precompiled)
file or a interpreter and your program's path, such as "python" and "example.py".
For more information, open a new terminal, cmd or PowerShell window and run the following command:

```sh
./automotive -h
```

For the tasks, you are given a json file, which includes a map. This map has to
be used to navigate your car from the starting point to the destination point. For
the first task, your job will be to implement an application that, based on the
actual traffic conditions, finds the most optimal route and navigates your
self-driving car from "A1" point to "D4". To read a more detailed description
on how the first task works run the following command in a terminal:

```sh
./automotive help taskone
```

Each time a new task is made available throughout the challenge, we will provide you
with a new runtime environment. Please note that you can use each new executable to run and solve any previous task.

## How to run your code

You can test your program by providing the path to an executeable:

```sh
./automotive <taskname> ./my_precomplied_program
```
or:
```sh
./automotive <taskname> python ./my_python_file.py
```

To submit your solution  simply add the [-u, --upload-as-user] flag
and provide your API key to the command above:

```sh
./automotive taskone my_precomplied_program -u=apikey
```
or:

```sh
  ./automotive taskone python ./my_python_file.py -u=apikey
```

Please note that you can test your program as many times as you would
like to. However, the number of submissions is limited to each task, so
make sure to double-check before you submit your project.
