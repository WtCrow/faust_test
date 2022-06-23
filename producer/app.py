from faustprometheus.monitor import PrometheusMonitor
from external_agents import external_consumer_agent
from faust.types import ProcessingGuarantee
import logging
import faust


app = faust.App(
    'PoC_producer',
    broker=f'kafka://kafka:9092',
    value_serializer='raw',
    processing_guarantee=ProcessingGuarantee.EXACTLY_ONCE
)
app.monitor = PrometheusMonitor(app)

input_topic = app.topic('producer_input')
output_topic = app.topic('consumer_output')


@app.agent(input_topic)
async def producer_agent(messages):
    async for message in messages:
        logging.info(f'[custom_message] New message: {message}. Send to processing')
        result = await external_consumer_agent.ask(message, reply_to=output_topic)
        logging.info(f'[custom_message] Result: {result}')
