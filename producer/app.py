from external_agents import consumer_agent
import faust


app = faust.App(
    'PoC_producer',
    broker=f'kafka://kafka:9092',
    value_serializer='raw',
    broker_credentials=None,
    autodiscover=True,
)

output_topic = app.topic('output')


@app.agent(output_topic)
async def producer_agent(messages):
    async for message in messages:
        print(f'[custom_message] New message: {message}. Send to processing')
        result = await consumer_agent.ask(message)
        print('[custom_message] Result: ', result)
