# Cisco Webex Teams Bot: Getting Started

A Cisco Webex Teams bot is an automated user within the Webex Teams platform that can be interacted with, enhancing the user experience within an organisation. The following instructions will guide you through the steps required to create and run your own Cisco Webex Teams Bot.

## Prerequisites

#### Create a Cisco Webex Teams account

Go to the [Cisco Webex](https://www.webex.com/) website and select **Teams** in the **Sign in** drop down menu on the top right corner. Fill in your details and follow the instructions to create an account.

#### Install Git

"Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency." [Link to install git](https://git-scm.com/download/).

#### Install Python

"Python is an interpreted, high-level, general-purpose programming language" [Link to install latest python version](https://www.python.org/downloads/).

#### Download Ngrok

"Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels." [Link to download ngrok](https://ngrok.com/download).

## Setup Bot

#### 1. Create a Bot

Go to [Cisco Webex for Developers](https://developer.webex.com/) and log in with your **Cisco Webex Teams** account details.

Click **Documentation** on the top bar and select the **Bots** section on the left. On this [Bots Documentation](https://developer.webex.com/docs/bots) webpage you will find an extended explanation on what are Bots and how to create them.

To proceed, click on the **Create a Bot** button and fill up all the required information to describe your new Bot. Finally, scroll down and click on the **Add Bot** button. Your Bot has now been created.

Click on **Regenerate Access Token** and save it since you will need it later.

#### 2. Open Terminal and Define Working Directory

Open a terminal and you can start working on your home directory (`/Users/<username>` for macOS, `<root>\Users\<username>` for Windows or `/home/<username>` for Linux). Otherwise, you can navigate to another directory using `cd <other-directory>`.

#### 3. Clone git Repository and Install Dependencies

Clone the git repository to your local machine by running the following command on your terminal.

```sh
git clone https://github.com/sarupanda/webex-teams-python-bot.git
```

To go to the directory you have just cloned simply run `cd webex-teams-python-bot`. Try running `ls` and check that you can see all the files you will need to get your Bot up and running.

After installing Python, open terminal and run the following command to install dependencies.

```sh
pip3 install flask requests webexteamssdk
```

## Run Bot

#### 1. Run Ngrok

Unzip the ngrok file that you downloaded above and copy the executable file to the `webex-teams-python-bot` folder. On a terminal window, go to this directory and run the following command to expose a web server on port 5000 of your local machine to the internet.

```sh
./ngrok http 5000
```

#### 2. Configure Access Token

Open `hello_bot.py` with your favourite text editor. If you still do not have one, take a quick look at [Visual Studio Code](https://code.visualstudio.com/), [Atom](https://atom.io/) or (in case you are a very brave developer) [Vim](https://www.vim.org).

Replace `<my-bot-access-token>` on Line 8 with the Access Token you saved during the **Create a Bot** step.

#### 3. Run Bot

On the terminal window, run the following to get your bot working.

```sh
python3 hello_bot.py
```

#### 4. Interact with your Bot

Login to your [Webex Teams](https://teams.webex.com/) account and **Contact a person** by clicking the **+** button. Then, enter your Bot Username (something like **XXXX@webex.bot**) and send a random message within the chat.

## Resources

* [Cisco Webex for Developers](https://developer.webex.com/docs/platform-introduction): Platform documentation
* [Webex Teams APIs](https://webexteamssdk.readthedocs.io/): Webex Teams SDK documentation
* [Cisco Webex Teams App Hub](https://apphub.webex.com/categories): Get some inspiration to develop your own bot from this list of Cisco Webex Teams Bot examples
* [RapidAPI](https://rapidapi.com/): The world's largest API directory