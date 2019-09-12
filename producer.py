from setup import topic
def pass_to_kafka(df):
    with topic.get_sync_producer(linger_ms=0) as p:
        while True:
            message = df
            p.produce(bytes(message))
            try:
                p.stop()
            except ProducerStoppedException:
                print("Message sent")

            