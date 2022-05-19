from consumer import consumer_agent
import faust


app = faust.App(
    'PoC_producer',
    broker='kafka://localhost:9093',
    value_serializer='raw',
)

output_topic = app.topic('output')


@app.agent(output_topic)
async def producer_agent(messages):
    async for message in messages:
        print(f'New message: {message}\nSend to processing')
        result = await consumer_agent.ask(message)
        print('Result: ', result)
