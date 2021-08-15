# Initial

- download http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2017_11_17.tar.gz

# Raspberry 4 

```sh
sudo apt-get install libhdf5-dev  libhdf5-dev libatlas-base-dev libjasper-dev libqtgui4  libqt4-test
pip3 install -U numpy
pip3 install https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0-rc2/tensorflow-2.4.0rc2-cp37-none-linux_armv7l.whl
pip3 install tensorflow-object-detection-api
pip3 install --upgrade --force jupyter-console
pip3 install -U numpy
```

Reemplazar en el archivo: /home/pi/.local/lib/python3.7/site-packages/object_detection/utils/label_map_util.py<br />
Replace tf.gfile.GFile to tf.io.gfile.GFile
