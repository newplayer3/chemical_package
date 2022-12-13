import tensorflow as tf


def gaussian_blur(input_tensor: tf.Variable, blur_tensor: tf.Variable, deviation: float = 0.1) -> tf.Tensor:
    """
    blur input tensor by gaussian function
    output size: (input_tensor, blur_tensor)
    """

    input_tensor = tf.expand_dims(input_tensor, -1)
    blur_tensor = tf.expand_dims(blur_tensor, 0)

    gamma = -0.5 / tf.square(deviation)

    return tf.exp(gamma * tf.square(input_tensor - blur_tensor))


if __name__ == "__main__":
    v = tf.Variable([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=tf.float16)
    v1 = tf.Variable([0, 1, 2], dtype=tf.float16)
    print(gaussian_blur(v, v1))
