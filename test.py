import asyncio, websockets

async def main():
    uri = "ws://localhost:8000/ws"

    async with websockets.connect(uri) as ws:
        await ws.send("Hello world")

        response = await ws.recv()
        print(f"server said: {response}")

asyncio.run(main())
