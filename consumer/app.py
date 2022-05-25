from asyncio import sleep
import logging
import faust


app = faust.App(
    'PoC_consumer',
    broker=f'kafka://kafka:9092',
    value_serializer='raw',
)

input_topic = app.topic('consumer_input')


@app.agent(input_topic)
async def consumer_agent(messages):
    async for message in messages:
        logging.info(f'[custom_message] Receive : {message}. Start processing')
        await sleep(5)
        logging.info('[custom_message] End processing')
        yield message + b' processed'
