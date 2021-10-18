# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/types/v1/web3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethermint/types/v1/web3.proto',
  package='ethermint.types.v1',
  syntax='proto3',
  serialized_options=b'Z\"github.com/tharsis/ethermint/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x65thermint/types/v1/web3.proto\x12\x12\x65thermint.types.v1\x1a\x14gogoproto/gogo.proto\"\xcc\x01\n\x16\x45xtensionOptionsWeb3Tx\x12O\n\x13typed_data_chain_id\x18\x01 \x01(\x04\x42\x32\xea\xde\x1f\x1atypedDataChainID,omitempty\xe2\xde\x1f\x10TypedDataChainID\x12)\n\tfee_payer\x18\x02 \x01(\tB\x16\xea\xde\x1f\x12\x66\x65\x65Payer,omitempty\x12\x30\n\rfee_payer_sig\x18\x03 \x01(\x0c\x42\x19\xea\xde\x1f\x15\x66\x65\x65PayerSig,omitempty:\x04\x88\xa0\x1f\x00\x42$Z\"github.com/tharsis/ethermint/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_EXTENSIONOPTIONSWEB3TX = _descriptor.Descriptor(
  name='ExtensionOptionsWeb3Tx',
  full_name='ethermint.types.v1.ExtensionOptionsWeb3Tx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='typed_data_chain_id', full_name='ethermint.types.v1.ExtensionOptionsWeb3Tx.typed_data_chain_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\032typedDataChainID,omitempty\342\336\037\020TypedDataChainID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fee_payer', full_name='ethermint.types.v1.ExtensionOptionsWeb3Tx.fee_payer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\022feePayer,omitempty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fee_payer_sig', full_name='ethermint.types.v1.ExtensionOptionsWeb3Tx.fee_payer_sig', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\025feePayerSig,omitempty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=76,
  serialized_end=280,
)

DESCRIPTOR.message_types_by_name['ExtensionOptionsWeb3Tx'] = _EXTENSIONOPTIONSWEB3TX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtensionOptionsWeb3Tx = _reflection.GeneratedProtocolMessageType('ExtensionOptionsWeb3Tx', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONOPTIONSWEB3TX,
  '__module__' : 'ethermint.types.v1.web3_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.types.v1.ExtensionOptionsWeb3Tx)
  })
_sym_db.RegisterMessage(ExtensionOptionsWeb3Tx)


DESCRIPTOR._options = None
_EXTENSIONOPTIONSWEB3TX.fields_by_name['typed_data_chain_id']._options = None
_EXTENSIONOPTIONSWEB3TX.fields_by_name['fee_payer']._options = None
_EXTENSIONOPTIONSWEB3TX.fields_by_name['fee_payer_sig']._options = None
_EXTENSIONOPTIONSWEB3TX._options = None
# @@protoc_insertion_point(module_scope)
