import tensorflow as tf


def gaussian_blur(input_tensor: tf.Variable, blur_tensor: tf.Variable, deviation: tf.Variable = 0.1) -> tf.Tensor:
    """
    blur input tensor by gaussian function
    output size: (input_tensor, blur_tensor)
    """
    # if input_tensor.dtype is
    input_tensor = tf.expand_dims(input_tensor, -1)
    blur_tensor = tf.expand_dims(blur_tensor, 0)

    gamma = -0.5 / tf.square(deviation)

    return tf.exp(gamma * tf.square(input_tensor - blur_tensor))





if __name__ == "__main__":
    v1 = tf.Variable([0, 0, 0], dtype=tf.float32)
    v2 = tf.Variable([1, 1, 1], dtype=tf.float32)
    v3 = tf.Variable([1, 4, 6], dtype=tf.float32)
    print(gaussian_blur(v1, v2,v3))
