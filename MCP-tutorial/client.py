from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import asyncio
import os

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args": ["mathserver.py"],
                "transport":"stdio"
            },
            "weather":{
                "url":"http://127.0.0.1:8000/mcp", # server must be up
                "transport":"streamable_http"
            }
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    ### client must fetch the tools/prompts present in the servers
    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b")

    ### when creating the agent we must give it the model and the tools
    agent = create_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content":"What is (3+5)*10?"}]}
    )

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content":"How is the weather for today?"}]}
    )

    print(f"Math response: {math_response["messages"][-1].content}")
    print(f"Weather response: {weather_response["messages"][-1].content}")

if __name__ == "__main__":
    asyncio.run(main())
