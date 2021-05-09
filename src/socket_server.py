import base64
import asyncio
import socketio
from aiohttp import web
from cv2 import cv2


async def start_socket_server(fps: int = 60):
    sio = socketio.AsyncServer()
    app = web.Application()
    sio.attach(app)

    cap = cv2.VideoCapture(0)

    @sio.event
    async def connect(sid, environ):
        print("Connect: ", sid)

    @sio.event
    def disconnect(sid):
        print("Disconnect: ", sid)

    async def loop():
        while True:
            ret, frame = cap.read()  # get frame from webcam
            res, frame = cv2.imencode(".jpg", frame)  # from image to binary buffer
            data = base64.b64encode(frame)
            await sio.emit("image", data.decode('ascii'))

            await asyncio.sleep(1 / fps)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', '8080')

    task1 = asyncio.create_task(loop())
    task2 = asyncio.create_task(site.start())

    await asyncio.gather(*[task1, task2])


if __name__ == "__main__":
    asyncio.run(start_socket_server())
