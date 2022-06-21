from faust.types import ProcessingGuarantee
import logging
import faust


app = faust.App(
    'PoC_consumer',
    broker=f'kafka://kafka:9092',
    value_serializer='raw',
    processing_guarantee=ProcessingGuarantee.EXACTLY_ONCE
)

input_topic = app.topic('consumer_input')


@app.agent(input_topic)
async def consumer_agent(messages):
    async for message in messages:
        logging.info(f'[custom_message] Receive : {message}. Start processing')
        if message.decode('utf-8') == 'raise':
            raise Exception('raise message')
        logging.info('[custom_message] End processing')
        yield message + b' processed'
