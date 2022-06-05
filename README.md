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

    This should also include number of votes for each option, as well as the total number of votes submitted.

## Improve error handling

As a developer, you need to be thinking about what can go wrong in your program! In this section, we will identify and address potential sources of errors.

### 1. Identify sources of error

Discuss in your group what would happen if:

+ You enter a command that isn't recognised.
+ When creating a poll, you don't enter a title and/or description before clicking submit.
+ You don't create a poll before trying to start one.
+ You create a poll but don't add any options before trying to start it.
+ You try to add an option after a poll has already started.
+ No votes are recorded before the poll is closed.
+ You try to create a second poll

* <b>Exercise:</b> Try these out to detemine what the current behaviour is and have a think about what the desired behaviour would be.

### 2. Send helpful error messages

In many of the cases in the previous exercise, the program just fails silently :( When things go wrong we should be letting the user know!

+ **Exercise**: Upon receiving an unknown command, send an error message in the space and suggest trying `help` to view list of available commands.

When writing error messages, it is best practice to be clear, precise, and contructive. Note how in the message above, a solution is provided.

+ **Exercise:** If the user tries to start a poll without creating one first, send an error message in the space and suggest trying `create poll`.

## Send a confirmation message upon receiving a vote

In general, users should receive feedback when they invoke a command or submit a reponse to confirm the success of the action. In this task, when a user submits a vote we would like to send them a confirmation message.

 + **Exercise:** Upon submitting a vote, send the user a direct message to confirm that their vote was recorded successfully. This should include the user's choice.

## Allow user to create a second poll

Currently, once invoking the `create poll` command and submitting the description for a poll, any subsequent attempts to use `create poll` are ignored. This is something we need to change!

+ **Exercise:** After a poll has ended, allow the user to create a new one. Make sure that the options and votes recorded are reset.

+ **Exercise:** If a user tries to create a new poll while there is a poll in progress, send a message to tell the current poll needs to be closed before you can create a new one.

## Multiple votes per person :O


As things are, we've got an issue! People can vote multiple times, can you think of a good way to prevent this?

* **Exercise**: Only allow one vote per person. Either send a direct message to the user that they cannot vote more than once, or let the user change their vote and send a new confirmation message.

## Challenge task!
Fixing up -- just a second!

## Stuck? Tips for Debugging:
Fixing up -- just a second!

# Task 4 - Create a new bot of your own

## Resources

* [Cisco Webex for Developers](https://developer.webex.com/docs/platform-introduction): Platform documentation
* [Webex Teams APIs](https://webexteamssdk.readthedocs.io/): Webex Teams SDK documentation
* [Webex Cards Guide](https://developer.webex.com/docs/api/guides/cards): Webex Teams SDK documentation for sending Adaptive Cards
* [Adaptive Cards Spec](https://adaptivecards.io/explorer/): Schema Explorer for Adaptive Cards and interactive online demo
* [Cisco Webex Teams App Hub](https://apphub.webex.com/categories): Get some inspiration to develop your own bot from this list of Cisco Webex Teams Bot examples
* [RapidAPI](https://rapidapi.com/): The world's largest API directory