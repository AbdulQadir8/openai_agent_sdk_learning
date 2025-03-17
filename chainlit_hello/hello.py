# import chainlit as cl

# @cl.on_message
# async def handle_message(message: cl.Message):
#     await cl.Message(content=f"Hello {message.content}").send()


import chainlit as cl

@cl.on_chat_start
async def start():
    # Sending an initial message
    await cl.Message(
        content="Hello! I'm a chatbot powered by Chainlit. How can I help you today?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Get user message content
    user_message = message.content
    
    # Simple echo response
    response = f"You said: {user_message}"
    
    # Send response back to user
    await cl.Message(
        content=response
    ).send()
