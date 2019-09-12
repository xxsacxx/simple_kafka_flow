from producer import pass_to_kafka
import numpy as np
import pandas as pd
# import exceptions
# from exceptions import (
#     ERROR_CODES,
#     KafkaException,
#     InvalidMessageSize,
#     MessageSizeTooLarge,
#     NotLeaderForPartition,
#     ProduceFailureError,
#     ProducerQueueFullError,
#     ProducerStoppedException,
#     SocketDisconnectedError,
#     UnknownTopicOrPartition,
# )

data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])
                
df = (pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))
def passdf(df):
    try:
        pass_to_kafka(df)
    except Exception:
        print("Message sent")

for i in range(5):
    passdf(df)
