# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from evmosproto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/bank/v1beta1/tx.proto',
  package='cosmos.bank.v1beta1',
  syntax='proto3',
  serialized_options=b'Z)github.com/cosmos/cosmos-sdk/x/bank/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x63osmos/bank/v1beta1/tx.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\"\xca\x01\n\x07MsgSend\x12-\n\x0c\x66rom_address\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:\"from_address\"\x12)\n\nto_address\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"to_address\"\x12[\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x11\n\x0fMsgSendResponse\"z\n\x0cMsgMultiSend\x12\x30\n\x06inputs\x18\x01 \x03(\x0b\x32\x1a.cosmos.bank.v1beta1.InputB\x04\xc8\xde\x1f\x00\x12\x32\n\x07outputs\x18\x02 \x03(\x0b\x32\x1b.cosmos.bank.v1beta1.OutputB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00\"\x16\n\x14MsgMultiSendResponse2\xac\x01\n\x03Msg\x12J\n\x04Send\x12\x1c.cosmos.bank.v1beta1.MsgSend\x1a$.cosmos.bank.v1beta1.MsgSendResponse\x12Y\n\tMultiSend\x12!.cosmos.bank.v1beta1.MsgMultiSend\x1a).cosmos.bank.v1beta1.MsgMultiSendResponseB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos_dot_bank_dot_v1beta1_dot_bank__pb2.DESCRIPTOR,])




_MSGSEND = _descriptor.Descriptor(
  name='MsgSend',
  full_name='cosmos.bank.v1beta1.MsgSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_address', full_name='cosmos.bank.v1beta1.MsgSend.from_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"from_address\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_address', full_name='cosmos.bank.v1beta1.MsgSend.to_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"to_address\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.bank.v1beta1.MsgSend.amount', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=342,
)


_MSGSENDRESPONSE = _descriptor.Descriptor(
  name='MsgSendResponse',
  full_name='cosmos.bank.v1beta1.MsgSendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=344,
  serialized_end=361,
)


_MSGMULTISEND = _descriptor.Descriptor(
  name='MsgMultiSend',
  full_name='cosmos.bank.v1beta1.MsgMultiSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='cosmos.bank.v1beta1.MsgMultiSend.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='cosmos.bank.v1beta1.MsgMultiSend.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=363,
  serialized_end=485,
)


_MSGMULTISENDRESPONSE = _descriptor.Descriptor(
  name='MsgMultiSendResponse',
  full_name='cosmos.bank.v1beta1.MsgMultiSendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=487,
  serialized_end=509,
)

_MSGSEND.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_MSGMULTISEND.fields_by_name['inputs'].message_type = cosmos_dot_bank_dot_v1beta1_dot_bank__pb2._INPUT
_MSGMULTISEND.fields_by_name['outputs'].message_type = cosmos_dot_bank_dot_v1beta1_dot_bank__pb2._OUTPUT
DESCRIPTOR.message_types_by_name['MsgSend'] = _MSGSEND
DESCRIPTOR.message_types_by_name['MsgSendResponse'] = _MSGSENDRESPONSE
DESCRIPTOR.message_types_by_name['MsgMultiSend'] = _MSGMULTISEND
DESCRIPTOR.message_types_by_name['MsgMultiSendResponse'] = _MSGMULTISENDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSend = _reflection.GeneratedProtocolMessageType('MsgSend', (_message.Message,), {
  'DESCRIPTOR' : _MSGSEND,
  '__module__' : 'cosmos.bank.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgSend)
  })
_sym_db.RegisterMessage(MsgSend)

MsgSendResponse = _reflection.GeneratedProtocolMessageType('MsgSendResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgSendResponse)
  })
_sym_db.RegisterMessage(MsgSendResponse)

MsgMultiSend = _reflection.GeneratedProtocolMessageType('MsgMultiSend', (_message.Message,), {
  'DESCRIPTOR' : _MSGMULTISEND,
  '__module__' : 'cosmos.bank.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgMultiSend)
  })
_sym_db.RegisterMessage(MsgMultiSend)

MsgMultiSendResponse = _reflection.GeneratedProtocolMessageType('MsgMultiSendResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGMULTISENDRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgMultiSendResponse)
  })
_sym_db.RegisterMessage(MsgMultiSendResponse)


DESCRIPTOR._options = None
_MSGSEND.fields_by_name['from_address']._options = None
_MSGSEND.fields_by_name['to_address']._options = None
_MSGSEND.fields_by_name['amount']._options = None
_MSGSEND._options = None
_MSGMULTISEND.fields_by_name['inputs']._options = None
_MSGMULTISEND.fields_by_name['outputs']._options = None
_MSGMULTISEND._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.bank.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=512,
  serialized_end=684,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='cosmos.bank.v1beta1.Msg.Send',
    index=0,
    containing_service=None,
    input_type=_MSGSEND,
    output_type=_MSGSENDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiSend',
    full_name='cosmos.bank.v1beta1.Msg.MultiSend',
    index=1,
    containing_service=None,
    input_type=_MSGMULTISEND,
    output_type=_MSGMULTISENDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)