import faust


app = faust.App(
    'PoC_consumer',
    broker='kafka://kafka:9092',
)

input_topic = app.topic('input')


@app.agent(input_topic)
async def consumer_agent(messages):
    """External agent"""
    pass
