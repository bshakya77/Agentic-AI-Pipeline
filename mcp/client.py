from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
import sys
from pathlib import Path

## stdio is commonly useful for local servers that the client can launch directly. Streamable HTTP is useful when the server runs separately and the client connects to its URL, as with your weather server.
async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":[str(Path(__file__).with_name("mathserver.py"))],
                "transport":"stdio",
            },
            "weather":{
                        "url": "http://localhost:8000/mcp", ##Start the HTTP server which communicate with client. 
                        "transport":"streamable_http",
                    },
        }

    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b")
    agent = create_agent(model=model, tools=tools)

    #query = input("What is (3+7) x 12?")
    math_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is (3+7) x 12 and what rule is used?"}]})
    print("Math Response:", math_response["messages"][-1].content)

    weather_reponse =  await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in California and what is the exact temperature?"}]})
    print("Weather Reponse:", weather_reponse["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
    