import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# TokenBucket rate limiter: 10 requests per 60 seconds
class TokenBucket:
    def __init__(self, rate, per):
        self.capacity = rate
        self.tokens = rate
        self.per = per
        self.last = time.time()

    def consume(self, tokens=1):
        now = time.time()
        elapsed = now - self.last
        self.last = now
        self.tokens += elapsed * (self.capacity / self.per)
        if self.tokens > self.capacity:
            self.tokens = self.capacity
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

def main():
    
    """
    Initializes and runs a simple CLI chatbot with concise responses.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY was not found in the .env file.")
        return

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
    
    # This template includes an instruction to keep answers brief.
    template = """
    You are a helpful and concise chatbot.
    Keep your answers brief and to the point, ideally under 30 words.

    Current conversation:
    {history}
    
    Human: {input}
    AI:"""
    bucket = TokenBucket(rate=10, per=60)  # 10 requests per 60 seconds

    # 3. Create a PromptTemplate instance
    prompt = PromptTemplate(
        input_variables=["history", "input"], 
        template=template
    )

    memory = ConversationBufferMemory(k=4, return_messages=True)
    
    # 4. Add the custom prompt to the ConversationChain
    chain = ConversationChain(
        llm=llm, 
        memory=memory, 
        prompt=prompt, # This is the new addition
        verbose=True
    )

    print("🤖 Chatbot is ready!. Type 'exit' to end.")
    print("-" * 50)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("🤖 Goodbye!")
            break
        if not bucket.consume():
            print("429: Rate limit exceeded. Please wait.")
            continue
        response = chain.invoke(input={"input": user_input})
        print(f"AI: {response['response']}")

if __name__ == "__main__":
    main()