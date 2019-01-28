# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\x12\x07message\"\x1c\n\x06\x43onfig\x12\x12\n\nisTraining\x18\x01 \x01(\x08\"\xd4\x02\n\x05State\x12\x15\n\rangleBallGoal\x18\x01 \x01(\x01\x12\x19\n\x11\x61ngleAttackerBall\x18\x02 \x01(\x01\x12\x19\n\x11\x61ngleDefenderBall\x18\x03 \x01(\x01\x12\x15\n\rangleAttacker\x18\x04 \x01(\x01\x12\x15\n\rangleDefender\x18\x05 \x01(\x01\x12\x18\n\x10\x64istanceBallGoal\x18\x06 \x01(\x01\x12\x1c\n\x14\x64istanceAttackerBall\x18\x07 \x01(\x01\x12\x1c\n\x14\x64istanceDefenderBall\x18\x08 \x01(\x01\x12\x14\n\x0cvelAttackerX\x18\t \x01(\x01\x12\x14\n\x0cvelAttackerY\x18\n \x01(\x01\x12\x14\n\x0cvelDefenderX\x18\x0b \x01(\x01\x12\x14\n\x0cvelDefenderY\x18\x0c \x01(\x01\x12\x10\n\x08velBallX\x18\r \x01(\x01\x12\x10\n\x08velBallY\x18\x0e \x01(\x01\";\n\nExperience\x12\x1d\n\x05state\x18\x01 \x01(\x0b\x32\x0e.message.State\x12\x0e\n\x06target\x18\x02 \x01(\x01\"T\n\x07Request\x12(\n\x0b\x65xperiences\x18\x01 \x03(\x0b\x32\x13.message.Experience\x12\x1f\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x0f.message.Config\"\x1a\n\x08Response\x12\x0e\n\x06values\x18\x01 \x03(\x01\"\x8c\x01\n\x07Message\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.message.MessageType\x12!\n\x07request\x18\x02 \x01(\x0b\x32\x10.message.Request\x12#\n\x08response\x18\x03 \x01(\x0b\x32\x11.message.Response\x12\x15\n\rendConnection\x18\x04 \x01(\x08*@\n\x0bMessageType\x12\x0c\n\x08GETVALUE\x10\x00\x12\t\n\x05LEARN\x10\x01\x12\n\n\x06\x43ONFIG\x10\x02\x12\x0c\n\x08RESPONSE\x10\x03\x62\x06proto3')
)

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='message.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GETVALUE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEARN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=717,
  serialized_end=781,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
GETVALUE = 0
LEARN = 1
CONFIG = 2
RESPONSE = 3



_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='message.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isTraining', full_name='message.Config.isTraining', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=26,
  serialized_end=54,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='message.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='angleBallGoal', full_name='message.State.angleBallGoal', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angleAttackerBall', full_name='message.State.angleAttackerBall', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angleDefenderBall', full_name='message.State.angleDefenderBall', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angleAttacker', full_name='message.State.angleAttacker', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angleDefender', full_name='message.State.angleDefender', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distanceBallGoal', full_name='message.State.distanceBallGoal', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distanceAttackerBall', full_name='message.State.distanceAttackerBall', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distanceDefenderBall', full_name='message.State.distanceDefenderBall', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velAttackerX', full_name='message.State.velAttackerX', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velAttackerY', full_name='message.State.velAttackerY', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velDefenderX', full_name='message.State.velDefenderX', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velDefenderY', full_name='message.State.velDefenderY', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velBallX', full_name='message.State.velBallX', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velBallY', full_name='message.State.velBallY', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=57,
  serialized_end=397,
)


_EXPERIENCE = _descriptor.Descriptor(
  name='Experience',
  full_name='message.Experience',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='message.Experience.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='message.Experience.target', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=399,
  serialized_end=458,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='message.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiences', full_name='message.Request.experiences', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='message.Request.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=460,
  serialized_end=544,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='message.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='message.Response.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=546,
  serialized_end=572,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='message.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='message.Message.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='message.Message.request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='message.Message.response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endConnection', full_name='message.Message.endConnection', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=575,
  serialized_end=715,
)

_EXPERIENCE.fields_by_name['state'].message_type = _STATE
_REQUEST.fields_by_name['experiences'].message_type = _EXPERIENCE
_REQUEST.fields_by_name['config'].message_type = _CONFIG
_MESSAGE.fields_by_name['type'].enum_type = _MESSAGETYPE
_MESSAGE.fields_by_name['request'].message_type = _REQUEST
_MESSAGE.fields_by_name['response'].message_type = _RESPONSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['Experience'] = _EXPERIENCE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Config)
  ))
_sym_db.RegisterMessage(Config)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.State)
  ))
_sym_db.RegisterMessage(State)

Experience = _reflection.GeneratedProtocolMessageType('Experience', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIENCE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Experience)
  ))
_sym_db.RegisterMessage(Experience)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Response)
  ))
_sym_db.RegisterMessage(Response)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
