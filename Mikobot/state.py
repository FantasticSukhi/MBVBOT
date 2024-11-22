import asyncio
from aiohttp import ClientSession
from httpx import AsyncClient, Timeout
from Python_ARQ import ARQ

# Create a global variable for the session
session = None

async def create_session():
    global session
    session = ClientSession()

async def main():
    # Create the aiohttp ClientSession
    await create_session()

    # HTTPx Async Client
    state = AsyncClient(
        http2=True,
        verify=False,
        headers={
            "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
            "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
        },
        timeout=Timeout(20),
    )

    # <=============================================== ARQ SETUP ========================================================>
    ARQ_API_KEY = "RLWCED-WZASYO-AWOLTB-ITBWTP-ARQ"  # GET API KEY FROM @ARQRobot
    ARQ_API_URL = "arq.hamker.dev"

    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

    # You can now use `arq` and `state` as needed in your async context

if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
