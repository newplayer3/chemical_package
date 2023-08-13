import tensorflow as tf


def cosine_blur(input_tensor, blur_tensor, cutoff_tensor):
    """
    blur input_tensor by cosine function: cos(blur*input)*e^(-cutoff*input)
    """

    input_tensor = tf.expand_dims(input_tensor, axis=-1)
    blur_tensor = tf.expand_dims(blur_tensor, axis=0)
    temp = tf.cos(blur_tensor * input_tensor)

    return tf.exp(-cutoff_tensor * input_tensor) * temp


if __name__ == "__main__":
    v1 = tf.Variable([[1,2,3], [3,2,1], [7,8,9]], dtype=tf.float32)
    v2 = tf.Variable([1, 1.5, 2.2, 3.0], dtype=tf.float32)
    v3 = tf.Variable([1, 0.6, 0.2, 0.1], dtype=tf.float32)
    print(cosine_blur(v1, v2, v3))
