import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')
    await sio.emit('message', {'response': 'my response'})
    

@sio.event
async def message(data):
    print('message received with ', data)
    await sio.emit('message', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:8080')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())