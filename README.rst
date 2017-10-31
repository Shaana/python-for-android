python-for-android
==================

Twisted support in kivy on android for python3 (python3crystax).

Make sure to use the kivy master or a version higher then 1.10.0. Otherwise

.. code-block:: python

    from kivy.support import install_twisted_reactor
    install_twisted_reactor()

won't work properly.

The requirements could look like this: 
--requirements=python3crystax,kivy==master,twisted
