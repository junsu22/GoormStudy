import tensorflow as tf
from tensorflow.keras.layers import Layer

class AttentionLayer(Layer):

    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)

    def call(self, inputs):
        encoder_out_seq, decoder_out_seq = inputs
        score = tf.matmul(decoder_out_seq, encoder_out_seq, transpose_b=True)
        attention_weights = tf.nn.softmax(score, axis=-1)
        context = tf.matmul(attention_weights, encoder_out_seq)
        return context, attention_weights