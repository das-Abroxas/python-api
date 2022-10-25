#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Aruna-Python-API',
    version='v0.5.0-beta.3',
    description='Aruna Object Storage Python API builds',
    url='https://github.com/ArunaStorage/python-api'
    author='Marius Dieckmann, Jannis Hochmuth',
    author_email='marius.dieckmann@computational.bio.uni-giessen.de, jannis.hochmuth@computational.bio.uni-giessen.de, '
    #packages=find_packages('aruna')
    packages=['aruna',
              'aruna.api',
              'aruna.api.internal', 'aruna.api.internal.v1',
              'aruna.api.notification', 'aruna.api.notification.services', 'aruna.api.notification.services.v1',
              'aruna.api.storage', 'aruna.api.storage.models', 'aruna.api.storage.models.v1', 'aruna.api.storage.services', 'aruna.api.storage.services.v1'],
    install_requires=[
        'protobuf>=3.20.0',
        'grpcio',
        'grpc-gateway-protoc-gen-openapiv2',
        'google-api-python-client'
    ],
)