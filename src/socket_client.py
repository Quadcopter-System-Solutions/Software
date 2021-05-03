import asyncio
import socketio

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print("connection established")
    await sio.emit("message", "hello")


@sio.event
async def image(data):
    print("message received with ", data)


@sio.event
async def disconnect():
    print("disconnected from server")


async def main():
    await sio.connect("http://localhost:8080")
    await sio.wait()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
