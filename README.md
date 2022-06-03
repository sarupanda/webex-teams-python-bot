# Cisco Webex Teams Bot: Getting Started

A Cisco Webex Teams bot is an automated user within the Webex Teams platform that can be interacted with, enhancing the user experience within an organisation.

# Task 1 - Set up and run hello bot

This first task will get you all set up to run a very simple hello bot that replies with a basic message.

### Create a Webex account

Go to [Cisco Webex for Developers](https://developer.webex.com/) and click **Sign up** on the top right corner. Fill in your details and follow the instructions to create an account.

### Create a Webex Bot

Go back to [Cisco Webex for Developers](https://developer.webex.com/) and log in with your account details.

Click **Documentation** on the top bar and select the **Bots** section on the left. On this [Bots Documentation](https://developer.webex.com/docs/bots) webpage you will find an extended explanation on what Bots are and how to create them.

To proceed, click on the **Create a Bot** button and fill up all the required information to describe your new Bot. Finally, scroll down and click on the **Add Bot** button.

Now that your Bot has been created, save the **Access Token** since you will need it later.

### Install Git

"Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency." [Link to install git](https://git-scm.com/download/).

### Install Python

"Python is an interpreted, high-level, general-purpose programming language" [Link to install the latest python version](https://www.python.org/downloads/).

### Download Ngrok

"Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels." [Link to download ngrok](https://ngrok.com/download).

## Setup Bot

### 1. Open Terminal and Define Working Directory

Open a terminal and you can start working on your home directory (`/Users/<username>` for macOS, `<root>\Users\<username>` for Windows or `/home/<username>` for Linux). Otherwise, you can navigate to another directory using `cd <other-directory>`.

### 2. Clone git Repository and Install Dependencies

Clone the git repository to your local machine by running the following command on your terminal.

```sh
git clone https://github.com/sarupanda/webex-teams-python-bot.git --recursive
```

To go to the directory you have just cloned, simply run `cd webex-teams-python-bot`. Try running `ls` and check that you can see all the files you will need to get your Bot up and running.

After installing Python, open terminal and run the following command to install dependencies.

```sh
pip3 install flask requests ./webexteamssdk
```

## Run Bot

### 1. Run Ngrok

Unzip the ngrok file that you downloaded above and copy the executable file to the `webex-teams-python-bot` folder. On a terminal window, go to this directory and run the following command to expose a web server on port 12000 of your local machine to the internet.

```sh
./ngrok http 12000
```

### 2. Configure Access Token

Open `task1.py` with your favourite text editor. If you still do not have one, take a quick look at [Visual Studio Code](https://code.visualstudio.com/), [Atom](https://atom.io/) or (in case you are a very brave developer) [Vim](https://www.vim.org).

Replace `<my-bot-access-token>` on Line 8 with the Access Token you saved during the **Create a Bot** step.

### 3. Run Bot

On the terminal window, run the following to get your bot working.

```sh
python3 task1.py
```

### 4. Interact with your Bot
Login to your [Webex Teams](https://teams.webex.com/) account and **Create a Space** by clicking the **+** button. Then, enter your Bot Username (something like **XXXX@webex.bot**) as well as your own email address.

To start interacting with the bot, type `@<bot_name>` along with your message. For example, if the bot was called "HelloBot" you would type `@HelloBot hello`

# Task 2 - Getting started with Poll Bot.
The goal of this task is for you to get the poll bot up and running and make a few test polls with the rest of your team.

## Create new poll bot in your bots
Follow the steps of the previous task to create a new bot called "Poll Bot". Grab and insert the access token into the string replacing ```<bot-access-token>``` with your token value.

## Run the bot
To run the bot, execute in a terminal the command:

```sh
python3 task2.py
```

Make sure that ngrok is also running like in the previous task in a separate terminal.

## Create some polls
Login to your [Webex Teams](https://teams.webex.com/) account and **Create a Space** by clicking the **+** button. Then, enter your Bot Username (something like **XXXX@webex.bot**) as well as your own email address. The bot has four commands: `create poll`, `add option`, `start poll` and `end poll`. To invoke one of those commands, type `@<bot_name>`, a space, and then the command.

For example, if your bot was named John, to create a poll, you would type `@John create poll` and send that into the space.

# Task 3 - Make improvements to Poll Bot

 For this section, the aim will be to extend the functionality of the poll bot. As you will have seen from experimenting with it in the previous section, it is quite limited in terms of what it can do. You will be adding new features of your own and addressing some issues with the current implementation.

## Add some new commands
### 1. Add a `help` command

The first new feature that we will add is a `help` command that gives the user a list of the available commands along with a brief description of what each command does. After all, the bot is pretty useless if people don't know how to interact with it!

 - <b>Exercise:</b> Using the code in `task3.py`, add a new command `help` that posts a help message either directly to the user or in the space. This can be just in plain text.
    <details>

    <summary><b>Hint</b></summary>

    You may find it helpful to use `send_direct_message()` or `send_message_in_room()` which have already been defined for you.

    </details>

### 2. Add a command that gives the current status of a poll

It would also be nice to be able to check the status of an ongoing poll, so that the author can preview the results before closing the poll.

 - <b>Exercise:</b> Define a new command `status poll` that shows the title and description of the poll, whether the poll has started, and if available, the preliminary results.

    This should also include number of votes for each option, as well as the total number of votes submitted. Consider prompting the user to use the `start poll` command if the poll hasn't been started yet.


# Task 4 - Create a new bot of your own

## Resources

* [Cisco Webex for Developers](https://developer.webex.com/docs/platform-introduction): Platform documentation
* [Webex Teams APIs](https://webexteamssdk.readthedocs.io/): Webex Teams SDK documentation
* [Webex Cards Guide](https://developer.webex.com/docs/api/guides/cards): Webex Teams SDK documentation for sending Adaptive Cards
* [Adaptive Cards Spec](https://adaptivecards.io/explorer/): Schema Explorer for Adaptive Cards and interactive online demo
* [Cisco Webex Teams App Hub](https://apphub.webex.com/categories): Get some inspiration to develop your own bot from this list of Cisco Webex Teams Bot examples
* [RapidAPI](https://rapidapi.com/): The world's largest API directory