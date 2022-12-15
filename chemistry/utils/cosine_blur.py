import tensorflow as tf


def cosine_blur(input_tensor, blur_tensor, cutoff_tensor):
    """
    blur input_tensor by cosine function: cos(blur*input)*e^(-cutoff*input)
    """
    print(input_tensor)
    input_tensor = tf.expand_dims(input_tensor, axis=-1)
    print(input_tensor)
    blur_tensor = tf.expand_dims(blur_tensor, axis=0)
    temp = tf.cos(blur_tensor * input_tensor)
    print(blur_tensor * input_tensor)
    print(temp)
    return tf.exp(-cutoff_tensor * input_tensor) * temp


if __name__ == "__main__":
    v1 = tf.Variable([1], [1], [1], dtype=tf.float32)
    v2 = tf.Variable([1, 1.5, 2.2], dtype=tf.float32)
    v3 = tf.Variable([1, 4, 6], dtype=tf.float32)
    print(cosine_blur(v1, v2, v3))
