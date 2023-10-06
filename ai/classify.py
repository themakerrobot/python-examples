import tensorflow as tf

batch_size = 128
img_height = 64
img_width = 64

data_dir = "/home/pi/fer"
#class_names = ['ang', 'dis', 'fea', 'hap', 'neu', 'sad', 'sur']
class_names = None
color_mode = 'grayscale' # rgb, rgba
# subset training / validation

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir, class_names=class_names,
    color_mode=color_mode, batch_size=batch_size, image_size=(img_height, img_width), shuffle=True, seed=123,
    validation_split=0.2, subset="training")

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir, class_names=class_names,
    color_mode=color_mode, batch_size=batch_size, image_size=(img_height, img_width), shuffle=True, seed=123,
    validation_split=0.2, subset="validation")

class_names = train_ds.class_names
num_classes = len(class_names)
print(f'num_classes: {num_classes}, class_names: {class_names}')

normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))

n, h, w, c = image_batch.shape
print(n,h,w,c)

model = tf.keras.Sequential([
  tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, c, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, c, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, c, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

#model.fit(ds, epochs=3)
model.fit(normalized_ds, validation_data=val_ds, epochs=3)
