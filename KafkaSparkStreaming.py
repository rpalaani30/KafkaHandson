
#   pyspark --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2
#   Run the below code

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

ssc = StreamingContext(sc, 5)


lines = KafkaUtils.createStream(ssc, 'cxln1.c.thelab-240901.internal:2181', "spark-streaming-consumer", {'TestKafkaPal':1})


# Split each line in each batch into words
words = lines.flatMap(lambda line: line[1].split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the elements of each RDD generated in this DStream to the console
wordCounts.pprint()

# Start the computation
ssc.start()

# Wait for the computation to terminate
ssc.awaitTermination()





