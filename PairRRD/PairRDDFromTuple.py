from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("PairRDDFromTuple").setMaster("local[*]")
    sc = SparkContext(conf = conf)
    tuples = [("Lily",23), ("Jack", 29), ("Mary",29), ("James", 8)]
    pairRDD = sc.parallelize(tuples)
    pairRDD.coalesce(1).saveAsTextFile("out")