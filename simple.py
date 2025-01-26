import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
import os

from browser_use import Agent

load_dotenv()

# Initialize the model
api_key = os.getenv('DEEPSEEK_API_KEY')

llm = ChatOpenAI(
	base_url='https://api.deepseek.com/v1', 
	model='deepseek-reasoner', 
	api_key=SecretStr(api_key)
)

task = 'Find hotels with the best reviews in Shanghai. Three men will stay for 4 nights from Feb 23th to Feb 27th, and the budget is $500.'

agent = Agent(task=task, llm=llm, use_vision=False)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
