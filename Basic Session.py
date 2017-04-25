import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.add(a, b)

with tf.Session() as sess:
    print(sess.run(c, feed_dict={a: [2., 4., 3.14], b: [1.5, 4.2, 3]}))
