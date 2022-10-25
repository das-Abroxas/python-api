# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/notification/services/v1/notification_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from aruna.api.storage.models.v1 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=aruna/api/notification/services/v1/notification_service.proto\x12\"aruna.api.notification.services.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a(aruna/api/storage/models/v1/models.proto\"\x8e\x04\n CreateEventStreamingGroupRequest\x12\x45\n\x08resource\x18\x01 \x01(\x0e\x32).aruna.api.storage.models.v1.ResourceTypeR\x08resource\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12/\n\x13include_subresource\x18\x03 \x01(\x08R\x12includeSubresource\x12N\n\nstream_all\x18\x04 \x01(\x0b\x32-.aruna.api.notification.services.v1.StreamAllH\x00R\tstreamAll\x12^\n\x10stream_from_date\x18\x05 \x01(\x0b\x32\x32.aruna.api.notification.services.v1.StreamFromDateH\x00R\x0estreamFromDate\x12j\n\x14stream_from_sequence\x18\x06 \x01(\x0b\x32\x36.aruna.api.notification.services.v1.StreamFromSequenceH\x00R\x12streamFromSequence\x12&\n\x0fstream_group_id\x18\x07 \x01(\tR\rstreamGroupIdB\r\n\x0bstream_type\"K\n!CreateEventStreamingGroupResponse\x12&\n\x0fstream_group_id\x18\x01 \x01(\tR\rstreamGroupId\"\xe7\x01\n\x1eReadStreamGroupMessagesRequest\x12P\n\x04init\x18\x01 \x01(\x0b\x32:.aruna.api.notification.services.v1.NotificationStreamInitH\x00R\x04init\x12L\n\x03\x61\x63k\x18\x02 \x01(\x0b\x32\x38.aruna.api.notification.services.v1.NotficationStreamAckH\x00R\x03\x61\x63k\x12\x14\n\x05\x63lose\x18\x03 \x01(\x08R\x05\x63loseB\x0f\n\rstream_action\"J\n DeleteEventStreamingGroupRequest\x12&\n\x0fstream_group_id\x18\x01 \x01(\tR\rstreamGroupId\"#\n!DeleteEventStreamingGroupResponse\"@\n\x16NotificationStreamInit\x12&\n\x0fstream_group_id\x18\x01 \x01(\tR\rstreamGroupId\"8\n\x14NotficationStreamAck\x12 \n\x0c\x61\x63k_chunk_id\x18\x01 \x03(\tR\nackChunkId\"\xa7\x01\n\x1fReadStreamGroupMessagesResponse\x12\x62\n\x0cnotification\x18\x01 \x03(\x0b\x32>.aruna.api.notification.services.v1.NotificationStreamResponseR\x0cnotification\x12 \n\x0c\x61\x63k_chunk_id\x18\x02 \x01(\tR\nackChunkId\"0\n\x12StreamFromSequence\x12\x1a\n\x08sequence\x18\x01 \x01(\x04R\x08sequence\"J\n\x0eStreamFromDate\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\x0b\n\tStreamAll\"\xca\x01\n\x1aNotificationStreamResponse\x12V\n\x07message\x18\x01 \x01(\x0b\x32<.aruna.api.notification.services.v1.EventNotificationMessageR\x07message\x12\x1a\n\x08sequence\x18\x02 \x01(\x04R\x08sequence\x12\x38\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\xd4\x01\n\x18\x45ventNotificationMessage\x12\x45\n\x08resource\x18\x01 \x01(\x0e\x32).aruna.api.storage.models.v1.ResourceTypeR\x08resource\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12P\n\x0cupdated_type\x18\x03 \x01(\x0e\x32-.aruna.api.notification.services.v1.EventTypeR\x0bupdatedType*\xbe\x01\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x45VENT_TYPE_CREATED\x10\x01\x12\x18\n\x14\x45VENT_TYPE_AVAILABLE\x10\x02\x12\x16\n\x12\x45VENT_TYPE_UPDATED\x10\x03\x12\x1f\n\x1b\x45VENT_TYPE_METADATA_UPDATED\x10\x04\x12\x16\n\x12\x45VENT_TYPE_DELETED\x10\x05\x12\x12\n\x0e\x45VENT_TYPE_ALL\x10\x06\x32\xa0\x04\n\x19UpdateNotificationService\x12\xaa\x01\n\x19\x43reateEventStreamingGroup\x12\x44.aruna.api.notification.services.v1.CreateEventStreamingGroupRequest\x1a\x45.aruna.api.notification.services.v1.CreateEventStreamingGroupResponse\"\x00\x12\xaa\x01\n\x19\x44\x65leteEventStreamingGroup\x12\x44.aruna.api.notification.services.v1.DeleteEventStreamingGroupRequest\x1a\x45.aruna.api.notification.services.v1.DeleteEventStreamingGroupResponse\"\x00\x12\xa8\x01\n\x17ReadStreamGroupMessages\x12\x42.aruna.api.notification.services.v1.ReadStreamGroupMessagesRequest\x1a\x43.aruna.api.notification.services.v1.ReadStreamGroupMessagesResponse\"\x00(\x01\x30\x01\x42\x9c\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x1aUpdateNotificationServicesP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.notification.services.v1.notification_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\032UpdateNotificationServicesP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1'
  _EVENTTYPE._serialized_start=1983
  _EVENTTYPE._serialized_end=2173
  _CREATEEVENTSTREAMINGGROUPREQUEST._serialized_start=177
  _CREATEEVENTSTREAMINGGROUPREQUEST._serialized_end=703
  _CREATEEVENTSTREAMINGGROUPRESPONSE._serialized_start=705
  _CREATEEVENTSTREAMINGGROUPRESPONSE._serialized_end=780
  _READSTREAMGROUPMESSAGESREQUEST._serialized_start=783
  _READSTREAMGROUPMESSAGESREQUEST._serialized_end=1014
  _DELETEEVENTSTREAMINGGROUPREQUEST._serialized_start=1016
  _DELETEEVENTSTREAMINGGROUPREQUEST._serialized_end=1090
  _DELETEEVENTSTREAMINGGROUPRESPONSE._serialized_start=1092
  _DELETEEVENTSTREAMINGGROUPRESPONSE._serialized_end=1127
  _NOTIFICATIONSTREAMINIT._serialized_start=1129
  _NOTIFICATIONSTREAMINIT._serialized_end=1193
  _NOTFICATIONSTREAMACK._serialized_start=1195
  _NOTFICATIONSTREAMACK._serialized_end=1251
  _READSTREAMGROUPMESSAGESRESPONSE._serialized_start=1254
  _READSTREAMGROUPMESSAGESRESPONSE._serialized_end=1421
  _STREAMFROMSEQUENCE._serialized_start=1423
  _STREAMFROMSEQUENCE._serialized_end=1471
  _STREAMFROMDATE._serialized_start=1473
  _STREAMFROMDATE._serialized_end=1547
  _STREAMALL._serialized_start=1549
  _STREAMALL._serialized_end=1560
  _NOTIFICATIONSTREAMRESPONSE._serialized_start=1563
  _NOTIFICATIONSTREAMRESPONSE._serialized_end=1765
  _EVENTNOTIFICATIONMESSAGE._serialized_start=1768
  _EVENTNOTIFICATIONMESSAGE._serialized_end=1980
  _UPDATENOTIFICATIONSERVICE._serialized_start=2176
  _UPDATENOTIFICATIONSERVICE._serialized_end=2720
# @@protoc_insertion_point(module_scope)
