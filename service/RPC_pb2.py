# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RPC.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PB_pb2 as PB__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tRPC.proto\x12\x02\x41\x33\x1a\x08PB.proto\"$\n\x14GetBookSearchRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"l\n\x15GetBookSearchResponse\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0c\n\x04year\x18\x04 \x01(\x05\x12\x18\n\x05genre\x18\x05 \x01(\x0e\x32\t.A3.Genre\"n\n\x17\x43reateBookCreateRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0c\n\x04year\x18\x04 \x01(\x05\x12\x18\n\x05genre\x18\x05 \x01(\x0e\x32\t.A3.Genre\"*\n\x18\x43reateBookCreateResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\x9f\x01\n\x10InventoryService\x12@\n\x07GetBook\x12\x18.A3.GetBookSearchRequest\x1a\x19.A3.GetBookSearchResponse\"\x00\x12I\n\nCreateBook\x12\x1b.A3.CreateBookCreateRequest\x1a\x1c.A3.CreateBookCreateResponse\"\x00')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RPC_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETBOOKSEARCHREQUEST._serialized_start=27
  _GETBOOKSEARCHREQUEST._serialized_end=63
  _GETBOOKSEARCHRESPONSE._serialized_start=65
  _GETBOOKSEARCHRESPONSE._serialized_end=173
  _CREATEBOOKCREATEREQUEST._serialized_start=175
  _CREATEBOOKCREATEREQUEST._serialized_end=285
  _CREATEBOOKCREATERESPONSE._serialized_start=287
  _CREATEBOOKCREATERESPONSE._serialized_end=329
  _INVENTORYSERVICE._serialized_start=332
  _INVENTORYSERVICE._serialized_end=491
# @@protoc_insertion_point(module_scope)
