# Cisco Webex Teams Bot: Getting Started

A Cisco Webex Teams bot is an automated user within the Webex Teams platform that can be interacted with, enhancing the user experience within an organisation. The following instructions will guide you through the steps required to create and run your own Cisco Webex Teams Bot.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup Bot](#setup)
3. [Run Bot](#run)
4. [Understanding Bot](#understanding)
5. [Resources](#resources)

<a name="prerequisites"></a>
## Prerequisites

### Create a Cisco Webex Teams account

Go to the [Cisco Webex](https://www.webex.com/) website and select **Teams** in the **Sign in** drop down menu on the top right corner. Fill in your details and follow the instructions to create an account.

### Install Git

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.  Find out more about git [here](https://git-scm.com/about).

The git installation will depend on your machine's Operating System (OS). After installing, confirm that git is available by entering the following command on terminal.

````sh
git --version
````

* **Install git on MacOS**

Probably the quickest way to get git on your machine is to install it with **Homebrew**. Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's macOS operating system and Linux.

To install Homebrew, open Terminal and run the following command.

````sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````
Once the installation is finished, install Git by running the following command.

````sh
brew install git
````

* **Install git on Ubuntu/Linux**

To install Git on your machine, run each of the following commands in your terminal sequentially.

````sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
````

* **Install git on Windows**

Go to the [Downloading Git for Windows](https://git-scm.com/download/win) page, download and install it.  Keep all the settings standard as you run through the installation process.

### Install Docker

Docker is an open platform for developing, shipping, and running applications. It is the most trendy container technology for running modern software apps particularly in the cloud. Find out more about Docker and containers [here](https://www.docker.com/why-docker).

The docker installation will depend on your operating system. After installing, confirm that Docker is available by entering the following command on terminal.

````sh
docker -v
````

* **Install Docker on MacOS**

Go to the [Install Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/) webpage. Head to Docker Hub by clicking the **Download the Docker Hub** button. After checking if your Apple Mac OS version fits the requirements, click on the **Get Docker** button and follow the installation instructions.

* **Install Docker on Ubuntu/Linux**

To set up the Docker repository in your machine, run each of the following command lines in your terminal sequentially.

````sh
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
````

Finally, to install Docker simply run

````sh
sudo apt-get update
sudo apt-get install docker-ce
````

* **Install Docker on Windows**

Go to the [Install Docker Toolbox on Windows](https://docs.docker.com/toolbox/toolbox_install_windows/) webpage and click on **Get Docker Toolbox for Windows** to start download. Follow the installation, accept admin prompts and requests to install network adapters.

* **Install Docker on other OS**

Please find instructions on how to install Docker on other Operating Systems [here](https://docs.docker.com/install/).

<a name="setup"></a>
## Setup Bot

### 1. Create a Bot

Go to [Cisco Webex for Developers](https://developer.webex.com/) and log in with your **Cisco Webex Teams** account details.

Click **Documentation** on the top bar and select the **Bots** section on the left. On this [Bots Documentation](https://developer.webex.com/docs/bots) webpage you will find an extended explanation on what are Bots and how to create them.

To proceed, click on the **Create a Bot** button and fill up all the required information to describe your new Bot. Finally, scroll down and click on the **Add Bot** button. Your Bot has now been created.

Click on **Regenerate Access Token** and save it since you will need it later.

### 2. Open Terminal and Define Working Directory

* **Non-Windows Users**

Good news! This is quite a trivial step for you since you just need to open your terminal. We recommend you work on your home directory, `/home/<username>` (Linux) or `/Users/<username>` (macOS), both shown as `~`. However, you can navigate to another directory using `cd <other-directory>`.

* **Windows Users**

Open the **Docker Quickstart Terminal** from the **Start Menu**. Once you see an ASCII boat in the terminal (the Docker logo) and can type in the terminal, navigate to the **Public** directory by running the following command.

````sh
cd /c/Users/Public
````

Note that if `c` isn't your Windows drive letter, you must replace it with the correct drive letter.

Remember that you must continue working on this terminal for the following steps.

### 3. Clone git Repository

Clone the current git repository recursively with submodules to your local machine by running the following command on your terminal.

```sh
git clone --recursive https://github.com/haskalpa/docker-webexteams-bot-example.git
```

If you run the command `ls`, you will find all the directories and files inside your current directory. To go to directory you have just cloned simply run `cd docker-webexteams-bot-example`. Try running `ls` and check that you can see all the files you will need to get your Bot up and running.

### 4. Configure with Access Token

Remember the access token for the bot that you saved earlier? Here is where you will need it.

Open the folder that you have just created, **docker-webexteams-bot-example**. Inside you will find a folder named **config**, open it. Then, create a copy of the **config_example.yaml** file and rename it to **config.yaml**.

Open the new file with your favourite text editor. If you still do not have one, take a quick look at [Atom](https://atom.io/), [Visual Studio Code](https://code.visualstudio.com/) or (in case you are a very brave developer) [Vim](https://www.vim.org). This is what the file contents should look like:

````sh
---
hello_bot:
teams_access_token: <my_bot_access_token>
````

Yep, you guessed it! Replace `<my_bot_access_token>` with the Access Token you save during the **Create a Bot** step.

### 5. Build Docker container

Back to the terminal window: run the following command to build your Docker container.

```sh
./build.sh
```

After a couple of seconds, you should get a `Successfully built` message in your terminal window.

<a name="run"></a>
## Run Bot

### 1. Run Docker container

If you are a **Windows user**, you will need to start with **Step 1**. If not, just skip this step and go directly to **Step 2**.

**Step 1**

Open **Notepad++** and open the file **run_hello_bot.sh**. You don't have Notepad++? Just quickly install it [here](https://notepad-plus-plus.org/).

Once you have opened the file, go to the **Edit** menu on the top bar and click **EOL Conversion**. Set this to **Unix (LF)**. Then, save the file and close Notepad++.

Repeat the above with **hello_bot/run.sh**.

**Step 2**

Run the Docker container with the following command.

```sh
./run_hello_bot.sh
```

### 2. Interact with your Bot

Login to your [Webex Teams](https://teams.webex.com/) account and **Create a space** by clicking the **+** button. Chose a name for the new space. Then, add your Bot to this space with the **Bot Username** you specified during the Create a Bot step. The format of this username should be **XXXX@webex.bot**.

Say hello to your bot by typing and saying something `hello`. If the bot replies `hello, person who has email <your email>`, congratulations! You managed to set up your first Bot.

<a name="understanding"></a>
## Understanding the Bot

### How does the bot know my personal email?

The bot is essentially running a single Python file, `hello_bot.py`. Through the Webex Teams API, once the bot receives a message, it also receives the `Person` who sent the message, which includes various details about them. One of these details is the email account of the user that messaged it.

### Fetch the logs of a container

If your bot seems to be having problems, have a look at the logs with

```sh
docker logs -f hello_bot
```

### Run a command in a running container

Need to do some troubleshooting? The following steps will help you if you need to debug your Python script. Open docker shell into your container with

```sh
docker exec -it hello_bot bash
```

To show running processes for all user run inside the shell

```sh
ps auxw
```

You should get a list similar to

```sh
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  18028  2948 pts/0    Ss   11:45   0:00 bash /workspace/run.sh
root         7  0.2  0.0  20536 14676 pts/0    Sl   11:45   0:00 ngrok http 5000 -bind-tls=true -config /opt/config/ngrok.yaml -log=
root        23  0.1  0.2 103268 40200 pts/0    S    11:45   0:00 python hello_bot.py
root        24  0.0  0.0  18236  3296 pts/0    S+   11:45   0:00 bash
root        34  0.0  0.0  18240  3384 pts/1    Ss   11:49   0:00 bash
root        44  0.0  0.0  34424  2808 pts/1    R+   11:49   0:00 ps auxw
```

Here you will find your script running, a line with `python hello_bot.py` as the command. In this example, the process has the ID `23`. Therefore, to kill the python bot script you will need to run inside the shell.

```sh
kill 23
```

If you want to confirm the previous step, run `ps auxw` again and check that the `python hello_bot.py` line has disappeared. You can now make changes to your `hello_bot.py` script. To run it again, you just need to run the following command.

```sh
python hello_bot.py
```

To exit the docker shell just run `exit`.

<a name="resources"></a>
## Resources

* [Cisco Webex Teams App Hub](https://apphub.webex.com/categories): Get some inspiration to develop your own bot from this list of Cisco Webex Teams Bot examples
