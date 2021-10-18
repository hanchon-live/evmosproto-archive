# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/evm/v1/evm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethermint/evm/v1/evm.proto',
  package='ethermint.evm.v1',
  syntax='proto3',
  serialized_options=b'Z(github.com/tharsis/ethermint/x/evm/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x65thermint/evm/v1/evm.proto\x12\x10\x65thermint.evm.v1\x1a\x14gogoproto/gogo.proto\"\x99\x02\n\x06Params\x12\'\n\tevm_denom\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"evm_denom\"\x12/\n\renable_create\x18\x02 \x01(\x08\x42\x18\xf2\xde\x1f\x14yaml:\"enable_create\"\x12+\n\x0b\x65nable_call\x18\x03 \x01(\x08\x42\x16\xf2\xde\x1f\x12yaml:\"enable_call\"\x12\x36\n\nextra_eips\x18\x04 \x03(\x03\x42\"\xe2\xde\x1f\tExtraEIPs\xf2\xde\x1f\x11yaml:\"extra_eips\"\x12P\n\x0c\x63hain_config\x18\x05 \x01(\x0b\x32\x1d.ethermint.evm.v1.ChainConfigB\x1b\xf2\xde\x1f\x13yaml:\"chain_config\"\xc8\xde\x1f\x00\"\xbb\x0b\n\x0b\x43hainConfig\x12]\n\x0fhomestead_block\x18\x01 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:\"homestead_block\"\x12k\n\x0e\x64\x61o_fork_block\x18\x02 \x01(\tBS\xe2\xde\x1f\x0c\x44\x41OForkBlock\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"dao_fork_block\"\x12G\n\x10\x64\x61o_fork_support\x18\x03 \x01(\x08\x42-\xe2\xde\x1f\x0e\x44\x41OForkSupport\xf2\xde\x1f\x17yaml:\"dao_fork_support\"\x12\x66\n\x0c\x65ip150_block\x18\x04 \x01(\tBP\xe2\xde\x1f\x0b\x45IP150Block\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"eip150_block\"\x12=\n\x0b\x65ip150_hash\x18\x05 \x01(\tB(\xe2\xde\x1f\nEIP150Hash\xf2\xde\x1f\x16yaml:\"byzantium_block\"\x12\x66\n\x0c\x65ip155_block\x18\x06 \x01(\tBP\xe2\xde\x1f\x0b\x45IP155Block\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"eip155_block\"\x12\x66\n\x0c\x65ip158_block\x18\x07 \x01(\tBP\xe2\xde\x1f\x0b\x45IP158Block\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"eip158_block\"\x12]\n\x0f\x62yzantium_block\x18\x08 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:\"byzantium_block\"\x12g\n\x14\x63onstantinople_block\x18\t \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:\"constantinople_block\"\x12_\n\x10petersburg_block\x18\n \x01(\tBE\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:\"petersburg_block\"\x12[\n\x0eistanbul_block\x18\x0b \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"istanbul_block\"\x12\x63\n\x12muir_glacier_block\x18\x0c \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x19yaml:\"muir_glacier_block\"\x12W\n\x0c\x62\x65rlin_block\x18\r \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"berlin_block\"\x12[\n\x0e\x63\x61talyst_block\x18\x10 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"catalyst_block\"\x12W\n\x0clondon_block\x18\x11 \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"london_block\"J\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10R\ryolo_v3_blockR\x0b\x65wasm_block\"#\n\x05State\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"D\n\x0fTransactionLogs\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12#\n\x04logs\x18\x02 \x03(\x0b\x32\x15.ethermint.evm.v1.Log\"\xfa\x01\n\x03Log\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06topics\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12%\n\x0c\x62lock_number\x18\x04 \x01(\x04\x42\x0f\xea\xde\x1f\x0b\x62lockNumber\x12$\n\x07tx_hash\x18\x05 \x01(\tB\x13\xea\xde\x1f\x0ftransactionHash\x12&\n\x08tx_index\x18\x06 \x01(\x04\x42\x14\xea\xde\x1f\x10transactionIndex\x12!\n\nblock_hash\x18\x07 \x01(\tB\r\xea\xde\x1f\tblockHash\x12\x1b\n\x05index\x18\x08 \x01(\x04\x42\x0c\xea\xde\x1f\x08logIndex\x12\x0f\n\x07removed\x18\t \x01(\x08\"\xd3\x01\n\x08TxResult\x12\x35\n\x10\x63ontract_address\x18\x01 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"contract_address\"\x12\r\n\x05\x62loom\x18\x02 \x01(\x0c\x12J\n\x07tx_logs\x18\x03 \x01(\x0b\x32!.ethermint.evm.v1.TransactionLogsB\x16\xf2\xde\x1f\x0eyaml:\"tx_logs\"\xc8\xde\x1f\x00\x12\x0b\n\x03ret\x18\x04 \x01(\x0c\x12\x10\n\x08reverted\x18\x05 \x01(\x08\x12\x10\n\x08gas_used\x18\x06 \x01(\x04:\x04\x88\xa0\x1f\x00\"K\n\x0b\x41\x63\x63\x65ssTuple\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12%\n\x0cstorage_keys\x18\x02 \x03(\tB\x0f\xea\xde\x1f\x0bstorageKeys:\x04\x88\xa0\x1f\x00\"\xf0\x02\n\x0bTraceConfig\x12\x0e\n\x06tracer\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\t\x12\x0e\n\x06reexec\x18\x03 \x01(\x04\x12\'\n\rdisable_stack\x18\x05 \x01(\x08\x42\x10\xea\xde\x1f\x0c\x64isableStack\x12+\n\x0f\x64isable_storage\x18\x06 \x01(\x08\x42\x12\xea\xde\x1f\x0e\x64isableStorage\x12\r\n\x05\x64\x65\x62ug\x18\x08 \x01(\x08\x12\r\n\x05limit\x18\t \x01(\x05\x12\x30\n\toverrides\x18\n \x01(\x0b\x32\x1d.ethermint.evm.v1.ChainConfig\x12\'\n\renable_memory\x18\x0b \x01(\x08\x42\x10\xea\xde\x1f\x0c\x65nableMemory\x12\x30\n\x12\x65nable_return_data\x18\x0c \x01(\x08\x42\x14\xea\xde\x1f\x10\x65nableReturnDataJ\x04\x08\x04\x10\x05J\x04\x08\x07\x10\x08R\x0e\x64isable_memoryR\x13\x64isable_return_dataB*Z(github.com/tharsis/ethermint/x/evm/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='ethermint.evm.v1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='evm_denom', full_name='ethermint.evm.v1.Params.evm_denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"evm_denom\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_create', full_name='ethermint.evm.v1.Params.enable_create', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\024yaml:\"enable_create\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_call', full_name='ethermint.evm.v1.Params.enable_call', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\022yaml:\"enable_call\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_eips', full_name='ethermint.evm.v1.Params.extra_eips', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\tExtraEIPs\362\336\037\021yaml:\"extra_eips\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chain_config', full_name='ethermint.evm.v1.Params.chain_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"chain_config\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=71,
  serialized_end=352,
)


_CHAINCONFIG = _descriptor.Descriptor(
  name='ChainConfig',
  full_name='ethermint.evm.v1.ChainConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='homestead_block', full_name='ethermint.evm.v1.ChainConfig.homestead_block', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\026yaml:\"homestead_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dao_fork_block', full_name='ethermint.evm.v1.ChainConfig.dao_fork_block', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\014DAOForkBlock\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"dao_fork_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dao_fork_support', full_name='ethermint.evm.v1.ChainConfig.dao_fork_support', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\016DAOForkSupport\362\336\037\027yaml:\"dao_fork_support\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eip150_block', full_name='ethermint.evm.v1.ChainConfig.eip150_block', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\013EIP150Block\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"eip150_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eip150_hash', full_name='ethermint.evm.v1.ChainConfig.eip150_hash', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\nEIP150Hash\362\336\037\026yaml:\"byzantium_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eip155_block', full_name='ethermint.evm.v1.ChainConfig.eip155_block', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\013EIP155Block\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"eip155_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eip158_block', full_name='ethermint.evm.v1.ChainConfig.eip158_block', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\013EIP158Block\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"eip158_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='byzantium_block', full_name='ethermint.evm.v1.ChainConfig.byzantium_block', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\026yaml:\"byzantium_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constantinople_block', full_name='ethermint.evm.v1.ChainConfig.constantinople_block', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\033yaml:\"constantinople_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='petersburg_block', full_name='ethermint.evm.v1.ChainConfig.petersburg_block', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\027yaml:\"petersburg_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='istanbul_block', full_name='ethermint.evm.v1.ChainConfig.istanbul_block', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"istanbul_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='muir_glacier_block', full_name='ethermint.evm.v1.ChainConfig.muir_glacier_block', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\031yaml:\"muir_glacier_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='berlin_block', full_name='ethermint.evm.v1.ChainConfig.berlin_block', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"berlin_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='catalyst_block', full_name='ethermint.evm.v1.ChainConfig.catalyst_block', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"catalyst_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='london_block', full_name='ethermint.evm.v1.ChainConfig.london_block', index=14,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"london_block\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=355,
  serialized_end=1822,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='ethermint.evm.v1.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ethermint.evm.v1.State.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ethermint.evm.v1.State.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1824,
  serialized_end=1859,
)


_TRANSACTIONLOGS = _descriptor.Descriptor(
  name='TransactionLogs',
  full_name='ethermint.evm.v1.TransactionLogs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ethermint.evm.v1.TransactionLogs.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='ethermint.evm.v1.TransactionLogs.logs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1861,
  serialized_end=1929,
)


_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='ethermint.evm.v1.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='ethermint.evm.v1.Log.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topics', full_name='ethermint.evm.v1.Log.topics', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethermint.evm.v1.Log.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_number', full_name='ethermint.evm.v1.Log.block_number', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\013blockNumber', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='ethermint.evm.v1.Log.tx_hash', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\017transactionHash', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_index', full_name='ethermint.evm.v1.Log.tx_index', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\020transactionIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='ethermint.evm.v1.Log.block_hash', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\tblockHash', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='ethermint.evm.v1.Log.index', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\010logIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removed', full_name='ethermint.evm.v1.Log.removed', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1932,
  serialized_end=2182,
)


_TXRESULT = _descriptor.Descriptor(
  name='TxResult',
  full_name='ethermint.evm.v1.TxResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_address', full_name='ethermint.evm.v1.TxResult.contract_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\027yaml:\"contract_address\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bloom', full_name='ethermint.evm.v1.TxResult.bloom', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_logs', full_name='ethermint.evm.v1.TxResult.tx_logs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"tx_logs\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ret', full_name='ethermint.evm.v1.TxResult.ret', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reverted', full_name='ethermint.evm.v1.TxResult.reverted', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='ethermint.evm.v1.TxResult.gas_used', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2185,
  serialized_end=2396,
)


_ACCESSTUPLE = _descriptor.Descriptor(
  name='AccessTuple',
  full_name='ethermint.evm.v1.AccessTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='ethermint.evm.v1.AccessTuple.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_keys', full_name='ethermint.evm.v1.AccessTuple.storage_keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\013storageKeys', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2398,
  serialized_end=2473,
)


_TRACECONFIG = _descriptor.Descriptor(
  name='TraceConfig',
  full_name='ethermint.evm.v1.TraceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracer', full_name='ethermint.evm.v1.TraceConfig.tracer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='ethermint.evm.v1.TraceConfig.timeout', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reexec', full_name='ethermint.evm.v1.TraceConfig.reexec', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disable_stack', full_name='ethermint.evm.v1.TraceConfig.disable_stack', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\014disableStack', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disable_storage', full_name='ethermint.evm.v1.TraceConfig.disable_storage', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\016disableStorage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug', full_name='ethermint.evm.v1.TraceConfig.debug', index=5,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ethermint.evm.v1.TraceConfig.limit', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overrides', full_name='ethermint.evm.v1.TraceConfig.overrides', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_memory', full_name='ethermint.evm.v1.TraceConfig.enable_memory', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\014enableMemory', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_return_data', full_name='ethermint.evm.v1.TraceConfig.enable_return_data', index=9,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\020enableReturnData', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2476,
  serialized_end=2844,
)

_PARAMS.fields_by_name['chain_config'].message_type = _CHAINCONFIG
_TRANSACTIONLOGS.fields_by_name['logs'].message_type = _LOG
_TXRESULT.fields_by_name['tx_logs'].message_type = _TRANSACTIONLOGS
_TRACECONFIG.fields_by_name['overrides'].message_type = _CHAINCONFIG
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['ChainConfig'] = _CHAINCONFIG
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['TransactionLogs'] = _TRANSACTIONLOGS
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['TxResult'] = _TXRESULT
DESCRIPTOR.message_types_by_name['AccessTuple'] = _ACCESSTUPLE
DESCRIPTOR.message_types_by_name['TraceConfig'] = _TRACECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.Params)
  })
_sym_db.RegisterMessage(Params)

ChainConfig = _reflection.GeneratedProtocolMessageType('ChainConfig', (_message.Message,), {
  'DESCRIPTOR' : _CHAINCONFIG,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.ChainConfig)
  })
_sym_db.RegisterMessage(ChainConfig)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.State)
  })
_sym_db.RegisterMessage(State)

TransactionLogs = _reflection.GeneratedProtocolMessageType('TransactionLogs', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONLOGS,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.TransactionLogs)
  })
_sym_db.RegisterMessage(TransactionLogs)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), {
  'DESCRIPTOR' : _LOG,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.Log)
  })
_sym_db.RegisterMessage(Log)

TxResult = _reflection.GeneratedProtocolMessageType('TxResult', (_message.Message,), {
  'DESCRIPTOR' : _TXRESULT,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.TxResult)
  })
_sym_db.RegisterMessage(TxResult)

AccessTuple = _reflection.GeneratedProtocolMessageType('AccessTuple', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSTUPLE,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.AccessTuple)
  })
_sym_db.RegisterMessage(AccessTuple)

TraceConfig = _reflection.GeneratedProtocolMessageType('TraceConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRACECONFIG,
  '__module__' : 'ethermint.evm.v1.evm_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.evm.v1.TraceConfig)
  })
_sym_db.RegisterMessage(TraceConfig)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['evm_denom']._options = None
_PARAMS.fields_by_name['enable_create']._options = None
_PARAMS.fields_by_name['enable_call']._options = None
_PARAMS.fields_by_name['extra_eips']._options = None
_PARAMS.fields_by_name['chain_config']._options = None
_CHAINCONFIG.fields_by_name['homestead_block']._options = None
_CHAINCONFIG.fields_by_name['dao_fork_block']._options = None
_CHAINCONFIG.fields_by_name['dao_fork_support']._options = None
_CHAINCONFIG.fields_by_name['eip150_block']._options = None
_CHAINCONFIG.fields_by_name['eip150_hash']._options = None
_CHAINCONFIG.fields_by_name['eip155_block']._options = None
_CHAINCONFIG.fields_by_name['eip158_block']._options = None
_CHAINCONFIG.fields_by_name['byzantium_block']._options = None
_CHAINCONFIG.fields_by_name['constantinople_block']._options = None
_CHAINCONFIG.fields_by_name['petersburg_block']._options = None
_CHAINCONFIG.fields_by_name['istanbul_block']._options = None
_CHAINCONFIG.fields_by_name['muir_glacier_block']._options = None
_CHAINCONFIG.fields_by_name['berlin_block']._options = None
_CHAINCONFIG.fields_by_name['catalyst_block']._options = None
_CHAINCONFIG.fields_by_name['london_block']._options = None
_LOG.fields_by_name['block_number']._options = None
_LOG.fields_by_name['tx_hash']._options = None
_LOG.fields_by_name['tx_index']._options = None
_LOG.fields_by_name['block_hash']._options = None
_LOG.fields_by_name['index']._options = None
_TXRESULT.fields_by_name['contract_address']._options = None
_TXRESULT.fields_by_name['tx_logs']._options = None
_TXRESULT._options = None
_ACCESSTUPLE.fields_by_name['storage_keys']._options = None
_ACCESSTUPLE._options = None
_TRACECONFIG.fields_by_name['disable_stack']._options = None
_TRACECONFIG.fields_by_name['disable_storage']._options = None
_TRACECONFIG.fields_by_name['enable_memory']._options = None
_TRACECONFIG.fields_by_name['enable_return_data']._options = None
# @@protoc_insertion_point(module_scope)