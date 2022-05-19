from asyncio import sleep
import faust


app = faust.App(
    'PoC_consumer',
    broker='kafka://localhost:9093',
    value_serializer='raw',
)

input_topic = app.topic('input')


@app.agent(input_topic)
async def consumer_agent(messages):
    async for message in messages:
        print(f'Receive : {message}\nStart processing')
        await sleep(5)
        print('End processing')
        yield message + b' processed'
