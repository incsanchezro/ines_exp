---
geometry: margin=1.5cm
header-includes:
    - \linespread{1.5}
    - \usepackage{graphicx}
    - \usepackage{helvet}
	- \renewcommand{\familydefault}{\sfdefault}
    
---

\begin{center} 
\includegraphics[width=\linewidth]{figures/Cover.png} 
{\LARGE Computing Fundamentals for Hydrological Modelling}
\\
\vspace{1cm}
{\Large Andrew Ireson}
\\
{\large Version 1.0\\ \today}
\\
\includegraphics[width=\linewidth]{figures/Cover.png}
\end{center}
\newpage

# Overview:

To do hydrological modelling effectively you need to be able to carry out the following tasks:

1) wrangle spatial and or timeseries data into the correct format to be read by the model

2) configure the model parameters and run options, and run the model

3) read the model outputs into your analysis software

4) run analysis software to plot and calculate statistics from data and model output files

Some models, particularly commercial models, have inbuilt graphical user interfaces, GUIs (i.e. controlled by a mouse) which handle all of the above, or at least some subset of the above. Other models, particularly research models, have no GUI, and require the user to do all the above themselves. Models which are particularly computationally demanding, that is models that solve large problems, such as global climate models or large scale hydrology models, are run on high performance computer clusters, with parallel processors (e.g. one year of model runtime could ideally be completed in one day if the run is split up between 365 processors). In this case, a GUI would get in the way of efficiency, and would be hard to run on a remote server. Such models are run using a Command Line Interface, CLI, and CLI models require a fifth skill set:

5) copy data to and from a remote server, navigate the file space on the server, and execute the model on the server all of which is done using the Linux command line interface.

MESH and CLASS are examples of CLI models. 

Irrespective of the model being used, developing some data analysis scripting skills (typically in python, R or MATLAB) is absolutely essential. Excel should not be used routinely. In addition, many models will require GIS skills to set up the model parameters and configuration. These skills are not addressed here. 

This document provides an overview of the very basic tools needed to run CLI models. We cover:

* The linux commandline - very basic commands you will need

* Text editors

* Remote access to servers - i.e. copying data to and from a linux server, and running models on the server

* Compiling and executing FORTRAN programs (using pre-existing Makefiles) 


## Basic commands

This is a list of the really basic bash commands (i.e. commands for the linux/osx/unix command line) that you will regularly use. I provide example syntax. You can find out what they do by typing `man command` or by googling!  I'm assuming here that you can figure out how to open a bash terminal, which is straightforward on a Mac or linux machine). If you're on Windows you should probably install the Linux subsystem for windows if you can. Some guidelines for doing this are here: [https://wiki.usask.ca/display/MESH/Installing+and+Activating+Windows+Subsystem+for+Linux+on+Windows+10](https://wiki.usask.ca/display/MESH/Installing+and+Activating+Windows+Subsystem+for+Linux+on+Windows+10).

|Bash command       | Description                                 |
|-------------------|---------------------------------------------|
|`pwd`              |tell me which folder I'm currently in        |
|`ls`               |list contents of current folder              |
|`cd output`           |change directory to subfolder xxx            |
|`cd ..`            |change directory up one level                |
|`cd ../output`        |change directory up one level and then into output |
|`cd`               |change to the home folder                    |
|`cp file1 file2`   |copy file1 to file2 all in the same folder     |
|`cp file1 output/file2`   |copy file1 to file2 in subfolder output    |
|`mv file1 file2`   |move file1 to file2 (i.e. rename the file)     |
|`mv file1 output/.`   |move file1 into subfolder output    |
|`rm file1`         |delete file1, but cannot be undone!          |
|`mkdir output`       |make a new directory in the current folder   |
|`rmdir output`       |remove an empty directory                    |
|`man ls`           |manual describing bash commands (here `ls`)  |
|`history`          |review the past commands you have entered    |
|`nano filename`    |open the nano editor (could be useful on the server)        |
|`vi filename`    |open the vi editor (experts only!) To exit press Esc then :q! enter)        |
|`atom filename`    |open the atom text editor, if installed and configured correctly     |
|`wc -l filename` | count the number of lines in a file |
| `head filename` | print the top 10 lines of the file to the screen |
| `cat filename`  | print every line of a file to the screen |
|`touch filename` | create empty file (or update the date on an existing file without changing contents) |
|`./filename`       |run an executable file in the current folder |
|`make` | run the Makefile in the current folder, which typically will compile the model from source code |

## Using commands with options

Often commands are combined with flags, to modify the actions. Here are some uesful examples.

|Bash command       | Description                                 |
|-------------------|---------------------------------------------|
|`ls`               |list contents of current folder              |
|`ls -a`            |shows all files, including hidden ones       |
|`ls -l`            |shows details of the files, such as sizes    |
|`ls -lah`          |combines last 2 with human readable output   |
|`du`               |disk usage                                   |
|`du -h -d 1`       |disk usage, human readable, all subfolders   |
|`df -h`            |disk free space, human readable              |

## Scripts

Sequences of these commands can be placed in scripts, so that they can be routinely executed. We won't cover this here, though it's extremely useful for routine and repetitive model runs.

## Regular expressions

If you type `ls *.txt` in the commandline, the command will list all the files in the current folder with a .txt extension.

If you type `ls andrew.*`, this will list all the files named andrew with any extension.

So, the character `*` finds anything which matches this pattern. A nice useage of this could be to delete all the .o files after compiling a fortran program, which you would do by typing `rm *.o`. (Be careful though - do not type `rm *` by accident as you'll permanently delete everything in the current folder.

There are many other wildcard expressions like `*`, but this is the most useful by far, so all we need for now.

## Text editors

A text editor is a simple piece of software used to open, edit and save text files. Text files are used for a huge amount of stuff in computing - a webpage is just a text file (html) that is read by a piece of software and converted into fancy looking text and graphics. You can write complicated documents in text files using LaTeX or markdown (this document is written in markdown and compiled as LaTeX using pandoc... but don't worry about that). Source code for computer languages like Fortran are all written in simple text files, which a compiler then converts into an executable program. Scripting languages, like python and R save scripts as text files, which an interpretter reads and executes. Then there are data files, which are very very often stored in text file formats. Common examples are csv files (comma delimited files that are often opened in Excel - but they are nothing but text files) and .dat files (which I don't think has any special meaning, by convention). 

So, it's important to have a reliable text editor that will allow you to efficiently open, navigate, edit and save files. I recommend atom. Notepad++ is also good. Sometimes the most basic text editors seem to write additional characters to files, to these should be avoided. Computer nerds tend to use either vim or emacs, which are very complicated to learn, but very efficient once learnt and can be used for more or less everything. Vim is available on any linux server too, which is a nice advantage of learning this... but this is strongly NOT recommended if you want to graduate from your program on time. If you do ever need to edit a textfile while you're connected to a server via ssh (see below) you can always open the nano editor (see table above), which is straightforward to use.

## Working on a server

### What is meant by working on a server?

Before we get into how to work on a server, let's think about what this actually means with an analogy. Imagine a computer is like an office. As the user of the computer you are the boss of the office. You are constantly telling people in your office to complete this and that task... you photocopy this document, you file these books away, you calculate the cost of the new furniture. This is equivalent to working on your own computer. You issue the task directly and they are carried out by the local processor. If your office burns down (i.e. your computer crashes) any actions that were in process are terminated (you don't get the answer to the calculation) and you might even lose all your data (the photocopies and the books). Working on a server is equivalent to the boss being located in a different office from the office where all the workers are. You, the boss, phone the office (connects to the server through a terminal connection). You issue all the same commands over the phone and they are carried out in exactly the same way in the remote office. However, there are some differences. The hustle and bustle of getting the work done takes place away from where you are sitting, so your own office is nice and quiet and all the local staff can work on any other tasks without getting interupted. Your office (i.e. computer) could be a piece of junk office that you got on kijiji for $100, as long as it has a phone (i.e. commandline interface) and it won't affect how fast the jobs get done. If you only want the answer to the calculation, it can be reported back over the phone quickly (i.e. a simple result from a model run). However, if you want the files sent to your local office this can take time (i.e. you will have to spend some time copying these over the network back to your computer, which can become a major constraint). If your office burns down (computer crashes) the data are safe and the jobs keep running (if you set them off correctly). Finally, while you're local office might have 4 or 8 workers (processors) the remote office might have hundreds. These remote processors might individually be slower than your local processors, but as there are so many, if you can parallelize your work (delegate to mutliple workers efficiently) it will be quicker overall.
  

### How to use a server

You can use the command line to control a remote computer and to copy files between computers.

`ssh` is used to connect to, and control, a remote computer. When you are connected using ssh, you can perform all the command line operations as above, but they are executed on the remote computer. This is particularly useful when working with servers, such as the plato server at the U of S.

To connect to a remote computer using ssh you type the following:

```bash
ssh username@servername
```

You will be prompted to enter a password. Once you have done that, type `ls` and `pwd` and spend sometime exploring the server. You can try this out by connecting to my server with username "mws_students", servername "water-ami.usask.ca" and password "hydrology2019". Try it out.

If you are on Windows you could use putty, which is exactly equivalent to doing an ssh connection from a terminal window.

The next thing you need to do is copy files between the server and your local machine. If you're on a Windows computer, I recommend you install winSCP for this task, as it's very easy. 

To copy files between your computer and a server you can also use the bash command `scp`, which must be issued from the terminal on the local computer (i.e. not from an ssh connection to a server). 

To copy a file from your local computer to a folder called "subfolder" located in the home folder on the server type: `scp filename username@servername:~/subfolder/`

To copy a file from the server (same location as above) to your local machine, change into the folder on your local machine where you want the file to be copied to, then type `scp username@servername:~/folder/filename .` 

Note, here the `~` character refers to the home folder. 

To copy a folder and the -r flag, so the all subfolders are also copied, e.g.  `scp -r username@servername:~/folder .` 


### Working on Andrew's linux server

You can get an account on my linux server - just ask me. The computer name is `water-ami.usask.ca`. I will give you a username and password. To change your password, connect onto the server using `ssh`, then type

```bash
passwd
```

## Working collaboratively with git

`git` is a software tool that allows you to 1) track changes in your files and 2) work collaboratively sharing files with others. You will likely use `git` both privately, to track your own work, and collaboratively, in particular to co-develop scripts with others. Here, each is outlined.

### Setting up git

We will run `git` from the commandline. First install `git` on your system. You can do this on linux with apt-get or on mac with homebrew, or you can just download from the [git website](https://git-scm.com/).

Once installed, open the terminal and configure your user settings, as follows:

```bash
git config --global user.name "Andrew Ireson"
git config --global user.email "andrew.ireson@usask.ca"
```

Now you are ready to go.

### Working privately with `git`

A `git` repository is a folder on your computer. In the background hidden from you, `git` stores older versions of files. You must periodically "commit" your files to the repository, and provide a message when you do this. The messages are really helpful when you come back to the work at a later date. 

Follow this demonstration:

Create a new folder somewhere on your computer, e.g.
```bash
cd ~/Desktop
mkdir testing123
cd testing123
```

To create a new repository in this folder type:
```bash
git init
```

Now see the status of your repository by typing
```bash
git status
```

The repository is empty. Let's add a file using nano. Type
```bash 
nano readme.md
```

Type some text in the file, then hit ctrl+X to save the file. You should see the file listed when you type `ls`. Run `git status` again, and you will see a message showing that you have untracked files. To commit your files to the repository is a two step command (helps minimize mistakes, but don't get hung up on the two steps):
```bash
git add .
git commit -m "My first commit"
```

Those are all the basic steps that you run periodically to keep hte repository up to date. Use meaningful messages so that you and others can understand what you did. Check the status again using `git status`. You can also see the history by typing

```bash 
git shortlog
```

or for a nicer display type 
```bash 
git log --format=format:"    %<(60,trunc)%Creset%s %Cgreen<<<---%cr" --revers
```

This last command is very long, so you should make an alias for it, if you want to use it. e.g. place the following line in the .profile or .bashrc file in your home folder:
```bash 
alias shortlog='git log --format=format:"    %<(60,trunc)%Creset%s %Cgreen<<<---%cr" --reverse'
```

That is all there is to working privately. Here is a screenshot of the end of my git log from a project that has been going on for a long time. You can see that I leave myself useful messages, that help me pick up the work again when I get back to it

\begin{center}
\includegraphics[width=0.6\linewidth]{figures/gitshortlog.png} 
\end{center}


### Working collaboratively with `git`

To work on a project with someone else, a `git` repository can be hosted on a server. This means, in addition to having a repository on your computer, that you continually update as above, you also periodically push your work to the repository on the server, and pull changes made by others from the server to your computer. Here is the work flow for this, assuming that the remote repository already exists, either on github or on a linux server (see advanced section below if oyu need to create a remote repository).

First you need to clone the repository onto your machine. This will copy all the files from the server, and make a local git repository at the same time. To do this, type

```bash
git clone [repository_address]
```

The `repository_address` could be on a local server, or on github. Github is great and easy to work with, but everything here is public, which is not always what you want. To clone a github repository, you can copy the link from the github page:

![](figures/github_clone.png)

You would then simply paste this into the command above, i.e.

```bash 
git clone https://github.com/amireson/RichardsEquation.git
```

If you are working on a repository on a linux server, you use the following command to clone the repository:

```bash
git clone ssh://username@serveraddress:/home/username/foldername
```

The first part after ssh is the regular username/server name syntax that ssh uses. After the second colon, you need to add the full path of the folder where the repository sits.

Now you have the local repository, you can work on this and add/commit files as normal. When you are ready to send your files to the server, you type:

```bash 
git push origin master
```

On the other hand, if someone else edits the remote repository, and you want to get hold of their updates, you should first make sure your local repository is up to date. Then you should push any changes you have made to the server. Then you should pull the changes they have made back to your local repository using:

```bash
git pull origin master
```

That is it! Note, you can also work on your own branch, instead of master. I have not done this yet, so will not document that here.

### Git branches
Git can be used to track any project (i.e. papers or scripts). Under collaborative networking, this version control system will support you and your coworkers on the fast and update development. With this objective, on git, the lastest and updated version of the project is located on the master branch. A new developer should create their branches (local branches) to create improvements and contributions to the master project. In order to protect the general project, it is desirable that always the collaborators work on their branches and once the contribution fulfils the task or issue required, merge the improvement with the master branch. In other words, a branch is a local draft space where the collaborator can create its contributions and verify that it is stable. Perhaps, for this reason, the GitHub community have restated that "A branch represents an independent line of development". Each new contribution to the master branch is labelled as a commit. A commit is a message that indicates git what exactly was the new contribution. This message is both a simple sentence and a clear message about the new contribution. A good practice is to include a new commit for each new contribution (task or issue solution), instead to create a single commit for a massive number of contributions.

Once you have cloned the project into your local system, you should create your own branch. Use the command: "git branch <branch>", where branch corresponds to the name or pseudo-name for the collaborator. If for any reason you wish to delete the local branch, use the command: "git branch -d <branch>". To work on your own brach use the command "git checkout <branch>". Once you have fulfilled the task or issue requirement (editing the file), you should add the file to develop the commit; use the command: "git add FILE". The last command indicates to git that you have created a new version of your branch. With the command: "git commit -m "message" " you can create the commit message. 
To merge your contribution to the master branch (update the project version based on your new contribution) use the command: "git merge <branch>". To merge your branch with the master, you should be located on the master branch ("git checkout master"). In order to avoid any merging conflict BEFORE to merge your branch is adviseble to update the master with the command :"git pull". Finally when you have realiced the properly merging you can update the master version on the general server (Andrew's server or online server), please use the command: "git push".Table 1. summarizes the steps to create and push a commit based on the previous commands. 
    
|Git  command       | Description                                 |
|-------------------|---------------------------------------------|
|`git pull`              |to update the master branch on your local system              |
|`git checkout <branch>`            |to start your work on your local workspace (your local branch)       |
|`git edit FILE `            |Optional. This command is used to edit the file. Please visit the section Text editor.Also, you can edit the file on your favourite software |
|`git add FILE`          |To add the new file    |
|`git commit -m "message" `               |To include the commit message                          |
|`git checkout origin master `       |To change the workspace towards origin master   |
|`git pull`            |To update before to merge the new contribution. Mandatory in order to avoid merging conflicts        |
|`git push`            |To update the master branch      |
    
  

### Advanced: setting up a remote repository on a linux server

You probably don't need to do this, but I'm including here for my reference.

First, you need to have a local repository on your computer that you want to push to the server. Make sure that local repo is full upto date, with all changes committed. Next, `ssh` onto the remote server. Navigate to the folder where you want your repo and create a folder with the repo name. Now go into that folder and type

```bash
git init --bare
```

That is now available. However, if you want others to be able to access this repository too, you must change some permissions. Create a group on linux for all users you want to have access to the repository with the command

```bash
sudo groupadd iresonlab
```
(where `iresonlab` is the name of the new group).

Now add users to this group using:

```bash
sudo usermod -a -G iresonlab andrew
```
Now change the group of the repository by navigating to the folder below the repository, and typing

```bash
sudo chgrp -R iresonlab reponame
```

Now all users in this group will be able to pull from and push to this repository. But, we still haven't added anything to the repository. Next, exit from the server, by typing `exit`. Make sure you are in your local git repository, that you want to push to the server. Then type

```bash
git remote add origin andrew@water-ami.usask.ca:/home/SharedRepos/menna/MESHGW
```
(where andrew is the user name on the server, water-ami.usask.ca is the server name, and /home/SharedRepos/menna/MESHGW is the folder on the server where you just greated the bare repository).

Next type

```bash
git push origin master
```

This sends the files to the remote machine. Note, "origin" is the name of the remote repository and "master" is the branch name.

Now, you and other members of the group and push and pull to this repository as described above.

## Activities

Two activities have been prepared to help learn some of this stuff, included in this repository. 

Maze - an activity to learn navigating the commandline. Copy this folder to your home folder, then open the command line navigate into the folder maze and read the readme.txt file for instructions.

CLASS_Ex - an activity to learn moving files and compiling and running executable programs. Again, see instructions in the readme.txt file in this folder.
