# <============================================== IMPORTS =========================================================>
from aiohttp import ClientSession
from httpx import AsyncClient, Timeout
from Python_ARQ import ARQ
import asyncio

# <=============================================== SETUP ========================================================>

class State:
    def __init__(self):
        self.session = None
        self.async_client = None
        self.arq = None

    async def initialize(self):
        # Initialize Aiohttp Async Client
        self.session = ClientSession()

        # Initialize HTTPx Async Client
        self.async_client = AsyncClient(
            http2=True,
            verify=False,
            headers={
                "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
            },
            timeout=Timeout(20),
        )

        # Initialize ARQ Setup
        ARQ_API_KEY = "RLWCED-WZASYO-AWOLTB-ITBWTP-ARQ"  # Replace with your ARQ API key
        ARQ_API_URL = "https://arq.hamker.dev"
        self.arq = ARQ(ARQ_API_URL, ARQ_API_KEY, self.session)

    async def close(self):
        # Close Aiohttp Session
        if self.session:
            await self.session.close()

        # Close HTTPx Async Client
        if self.async_client:
            await self.async_client.aclose()

# Create a global state instance
state = State()

# Initialize State
async def setup_state():
    await state.initialize()

# Close State
async def close_state():
    await state.close()

# Ensure proper initialization and cleanup in the main context
if __name__ == "__main__":
    asyncio.run(setup_state())
