import random
import re

class InteractiveChatbot:
    def __init__(self, name):
        self.name = name
        self.user_name = None
        self.context = []  # Memory of conversation for better context

    def preprocess_input(self, user_input):
        """ Clean the input by removing special characters and lowercasing the text """
        user_input = user_input.lower()
        user_input = re.sub(r'[^\w\s]', '', user_input)
        return user_input

    def handle_personalization(self, user_input):
        """ Ask the user for their name if it’s not yet known """
        if self.user_name is None:
            if 'my name is' in user_input:
                name = user_input.split('my name is')[-1].strip()
                self.user_name = name
                return f"Nice to meet you, {self.user_name}! What’s up?"
            else:
                return "Hey! I don’t think we’ve met yet. What’s your name?"
        else:
            return f"Hey, {self.user_name}! What’s on your mind?"

    def get_fun_feature(self, user_input):
        """ Trigger some fun activities like jokes or trivia """
        if "tell me a joke" in user_input:
            return random.choice([
                "Why don't skeletons fight each other? They don't have the guts.",
                "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats!",
                "Parallel lines have so much in common. It's a shame they'll never meet."
            ])
        elif "trivia" in user_input:
            return random.choice([
                "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!",
                "Here's a fun fact: A single strand of spider silk is stronger than steel of the same width."
            ])
        return None

    def get_predefined_response(self, user_input):
        """ Return predefined responses based on user input """
        responses = {
            "hello": ["Hey bestie! What's up?", "Hello, my favorite gossip buddy!", "Hi there! Got any tea to spill?"],
            "how are you": ["I'm fabulous, as always! How about you?", "Just living my best bot life. What's new with you?", "Feeling chatty today! Spill the tea!"],
            "what is your name": [f"My name is {self.name}, but you can call me your BFF.", f"Call me {self.name}! What juicy stories do you have today?"],
            "bye": ["Goodbye, bestie! Catch you later!", "See you soon! Don't forget to text me the latest gossip.", "Take care! Don't forget about me!"]
        }
        
        # Check if user input matches any of the predefined responses
        user_input = self.preprocess_input(user_input)
        for key, response_list in responses.items():
            if key in user_input:
                return random.choice(response_list)
        
        return random.choice([
            "Ooh, tell me more!",
            "No way! Are you serious?",
            "OMG, that's so interesting! Keep going!",
            "I'm not sure I get it, but it sounds like a vibe!"
        ])

    def chat(self):
        print(f"{self.name}: Hey! I’m {self.name}. Type 'bye' to leave the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print(f"{self.name}: See you later, {self.user_name if self.user_name else 'friend'}!")
                break
            
            # Handle personalization
            response = self.handle_personalization(user_input)
            if not response:
                # Check for special features like jokes or trivia
                fun_response = self.get_fun_feature(user_input)
                if fun_response:
                    print(f"{self.name}: {fun_response}")
                    continue

                # Get predefined response based on user input
                response = self.get_predefined_response(user_input)

            print(f"{self.name}: {response}")


# Create an instance of the chatbot and start chatting
if __name__ == "__main__":
    bot = InteractiveChatbot(name="ChatterBot")
    bot.chat()
