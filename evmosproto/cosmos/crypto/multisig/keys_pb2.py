# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/multisig/keys.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/crypto/multisig/keys.proto',
  package='cosmos.crypto.multisig',
  syntax='proto3',
  serialized_options=b'Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisig',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!cosmos/crypto/multisig/keys.proto\x12\x16\x63osmos.crypto.multisig\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"\x8c\x01\n\x11LegacyAminoPubKey\x12\'\n\tthreshold\x18\x01 \x01(\rB\x14\xf2\xde\x1f\x10yaml:\"threshold\"\x12H\n\x0bpublic_keys\x18\x02 \x03(\x0b\x32\x14.google.protobuf.AnyB\x1d\xe2\xde\x1f\x07PubKeys\xf2\xde\x1f\x0eyaml:\"pubkeys\":\x04\x88\xa0\x1f\x00\x42\x33Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisigb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_LEGACYAMINOPUBKEY = _descriptor.Descriptor(
  name='LegacyAminoPubKey',
  full_name='cosmos.crypto.multisig.LegacyAminoPubKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='threshold', full_name='cosmos.crypto.multisig.LegacyAminoPubKey.threshold', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"threshold\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_keys', full_name='cosmos.crypto.multisig.LegacyAminoPubKey.public_keys', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\007PubKeys\362\336\037\016yaml:\"pubkeys\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=251,
)

_LEGACYAMINOPUBKEY.fields_by_name['public_keys'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['LegacyAminoPubKey'] = _LEGACYAMINOPUBKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LegacyAminoPubKey = _reflection.GeneratedProtocolMessageType('LegacyAminoPubKey', (_message.Message,), {
  'DESCRIPTOR' : _LEGACYAMINOPUBKEY,
  '__module__' : 'cosmos.crypto.multisig.keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.multisig.LegacyAminoPubKey)
  })
_sym_db.RegisterMessage(LegacyAminoPubKey)


DESCRIPTOR._options = None
_LEGACYAMINOPUBKEY.fields_by_name['threshold']._options = None
_LEGACYAMINOPUBKEY.fields_by_name['public_keys']._options = None
_LEGACYAMINOPUBKEY._options = None
# @@protoc_insertion_point(module_scope)
