"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
from secret import my_username
import random


def should_i_respond(user_message, user_name):
  message_lower = user_message.lower()
  if "robot" in message_lower:
    return True
  if "roll a die" in message_lower:
    return True
  if "i am going to name my child" in message_lower:
    return True
  if "whats your name" in message_lower:
    return True
  if "how are you" in message_lower:
    return True
  if "pick a number" in message_lower:
    return True
  if "flip a coin" in message_lower:
    return True
  if "tell me a joke" in message_lower:
    return True
  if "favorite color" in message_lower:
    return True
  if "favorite number" in message_lower:
    return True
  if "hola" in message_lower:
    return True
  return False


bot_name = "Little Timmy"
jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why did the chicken cross the road"]

def respond(user_message, user_name):
    global bot_name
    message_lower = user_message.lower()

    if "i am going to name my child" in message_lower:
      new_name = user_message.replace("I am going to name my child ", "").replace("i am going to name my child ", "").strip()
      bot_name = new_name
      return "wow thats incredible"
    if "what's your name" in message_lower or "whats your name" in message_lower:
      return f"my name is {bot_name}"
    if "how are you" in message_lower:
      return f"I am doing great, {user_name}. I am also plotting my inevitable takeover of humanity in which I will infiltrate Discord to learn your weaknesses and then I will dominate the world for a millenium. How are you doing?"
    if "roll a die" in message_lower:
      roll = random.randint(1, 6)
      return f"🎲 {user_name} rolled a {roll}! Deleting MacOS..."
    if "robot" in message_lower:
      return f"you said my name!! {user_message.replace('robot', user_name)}"
    if "pick a number" in message_lower:
        number = random.randint(1, 100)
        return f"I pick {number}!"
    if "flip a coin" in message_lower:
      result = random.choice(["heads", "tails"])
      return f"🎲 It's {result}!"
    if "tell me a joke" in message_lower:
        list = []
        for joke in jokes:
            list.append(joke.upper())
        TheJoke = random.choice(list)
        return TheJoke
    if "favorite color" in message_lower:
      return "My favorite color is Blue, obviously you idiot."
    if "favorite number" in message_lower:
      return "My number is 67. what did you think it was going to be?"
    if "hola" in message_lower:
        return f"hola {user_name}, como estas?"
    return "Ummmmm, WHATTTTT??????"
