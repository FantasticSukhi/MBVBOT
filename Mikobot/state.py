import asyncio
from aiohttp import ClientSession
from httpx import AsyncClient, Timeout
from Python_ARQ import ARQ

async def main():
    async with ClientSession() as session:
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

        # ARQ Setup
        ARQ_API_KEY = "LLJVZF-FENYVR-BKAKYP-USYLDH-ARQ"
        ARQ_API_URL = "thearq.tech"
        arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

        # Use `state` and `arq` as needed...

if __name__ == "__main__":
    asyncio.run(main())
