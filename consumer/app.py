from asyncio import sleep
import faust


app = faust.App(
    'PoC_consumer',
    broker=f'kafka://kafka:9092',
    value_serializer='raw',
    broker_credentials=None,
    autodiscover=True,
)

input_topic = app.topic('input')


@app.agent(input_topic)
async def consumer_agent(messages):
    async for message in messages:
        print(f'[custom_message] Receive : {message}. Start processing')
        await sleep(5)
        print('[custom_message] End processing')
        yield message + b' processed'
