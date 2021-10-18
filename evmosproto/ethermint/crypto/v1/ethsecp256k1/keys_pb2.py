# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/crypto/v1/ethsecp256k1/keys.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethermint/crypto/v1/ethsecp256k1/keys.proto',
  package='ethermint.crypto.v1.ethsecp256k1',
  syntax='proto3',
  serialized_options=b'Z0github.com/tharsis/ethermint/crypto/ethsecp256k1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+ethermint/crypto/v1/ethsecp256k1/keys.proto\x12 ethermint.crypto.v1.ethsecp256k1\x1a\x14gogoproto/gogo.proto\"\x1b\n\x06PubKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c:\x04\x98\xa0\x1f\x00\"\x16\n\x07PrivKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x42\x32Z0github.com/tharsis/ethermint/crypto/ethsecp256k1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PUBKEY = _descriptor.Descriptor(
  name='PubKey',
  full_name='ethermint.crypto.v1.ethsecp256k1.PubKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ethermint.crypto.v1.ethsecp256k1.PubKey.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=130,
)


_PRIVKEY = _descriptor.Descriptor(
  name='PrivKey',
  full_name='ethermint.crypto.v1.ethsecp256k1.PrivKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ethermint.crypto.v1.ethsecp256k1.PrivKey.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=154,
)

DESCRIPTOR.message_types_by_name['PubKey'] = _PUBKEY
DESCRIPTOR.message_types_by_name['PrivKey'] = _PRIVKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PubKey = _reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), {
  'DESCRIPTOR' : _PUBKEY,
  '__module__' : 'ethermint.crypto.v1.ethsecp256k1.keys_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.crypto.v1.ethsecp256k1.PubKey)
  })
_sym_db.RegisterMessage(PubKey)

PrivKey = _reflection.GeneratedProtocolMessageType('PrivKey', (_message.Message,), {
  'DESCRIPTOR' : _PRIVKEY,
  '__module__' : 'ethermint.crypto.v1.ethsecp256k1.keys_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.crypto.v1.ethsecp256k1.PrivKey)
  })
_sym_db.RegisterMessage(PrivKey)


DESCRIPTOR._options = None
_PUBKEY._options = None
# @@protoc_insertion_point(module_scope)
