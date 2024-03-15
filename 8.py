import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'(.*) college(.*) admission(.*)',
     ['For admission inquiries, you can visit our website or contact our admission office.']),
    (r'(.*) (apply|application)(.*)',
     ['You can apply online through our website or obtain an application form from our admission office.']),
    (r'(.*) (deadline|last date)(.*)',
     ['The deadline for admission applications varies. Please visit our website for the most up-to-date information.']),
    (r'(.*) (requirements|eligibility)(.*)',
     ['To check eligibility criteria and requirements, please visit our website or contact our admission office.']),
    (r'(.*) (scholarship|financial aid)(.*)',
     ['Information about scholarships and financial aid can be found on our website or by contacting our financial aid office.']),
    (r'(.*) (contact|reach)(.*)',
     ['You can contact us at admission@college.edu or call us at +123456789.']),
    (r'quit', ['Goodbye!']),
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

def main():
    print("Welcome to College Admission Chatbot!")
    print("Ask any questions related to college admission or type 'quit' to exit.")
    for _ in range(10):
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
