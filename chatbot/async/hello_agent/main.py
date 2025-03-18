import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

run_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


agent1 = Agent(
        name="Assistant",
        instructions="You are helpful Assistent.",
        model=model
    )



@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello! I am the panaversity Support Agent. How can I help you?").send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    history.append({"role":"user","content":message.content})
    result = await Runner.run(agent1,
                              input=history,
                              run_config=run_config)
    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()