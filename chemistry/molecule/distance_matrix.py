import tensorflow as tf


def get_distance_matrix(coordinate_list: tf.Tensor, system_name: str = 'cartesian') -> tf.Tensor:
    """
    return distance matrix from input coordinations
    default return -1
    """
    tf.debugging.assert_rank_at_least(coordinate_list,2, message="coordinate tensor at least at rank 2")

    tf.debugging.assert_integer(coordinate_list, message="coordinate tensor must be float")

    if system_name == 'cartesian':
        return _cartensian_distance_matrix(coordinate_list)
    else:
        raise NotImplementedError("Unrecognized coordinate system")


def _cartensian_distance_matrix(coordinate_list):
    """
    calculate
    """
    vertex_1 = tf.expand_dims(coordinate_list, -2)
    vertex_2 = tf.expand_dims(coordinate_list, -3)
    matrix = tf.sqrt(tf.reduce_sum(tf.square(vertex_1 - vertex_2), axis=-1))
    return matrix




if __name__ == "__main__":
    v = tf.Variable([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(get_distance_matrix(v))
