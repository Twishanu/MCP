from fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool
async def getWeather(location:str)->str:
    """Get the current weather of the given location"""
    # hardcoded
    return "The current weather of Kolkata is sunny and humid"

if __name__=="__main__":
    mcp.run(transport="streamable-http")