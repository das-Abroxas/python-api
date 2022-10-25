# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v1/objectgroup_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v1 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_models__pb2
from aruna.api.storage.models.v1 import query_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_query__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7aruna/api/storage/services/v1/objectgroup_service.proto\x12\x1d\x61runa.api.storage.services.v1\x1a(aruna/api/storage/models/v1/models.proto\x1a\'aruna/api/storage/models/v1/query.proto\x1a\x1cgoogle/api/annotations.proto\"\xb8\x02\n\x18\x43reateObjectGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12#\n\rcollection_id\x18\x03 \x01(\tR\x0c\x63ollectionId\x12\x1d\n\nobject_ids\x18\x04 \x03(\tR\tobjectIds\x12&\n\x0fmeta_object_ids\x18\x05 \x03(\tR\rmetaObjectIds\x12=\n\x06labels\x18\x06 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x07 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\"p\n\x19\x43reateObjectGroupResponse\x12S\n\x0cobject_group\x18\x01 \x01(\x0b\x32\x30.aruna.api.storage.models.v1.ObjectGroupOverviewR\x0bobjectGroup\"\xd3\x02\n\x18UpdateObjectGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12#\n\rcollection_id\x18\x04 \x01(\tR\x0c\x63ollectionId\x12\x1d\n\nobject_ids\x18\x05 \x03(\tR\tobjectIds\x12&\n\x0fmeta_object_ids\x18\x06 \x03(\tR\rmetaObjectIds\x12=\n\x06labels\x18\x07 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x08 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\"p\n\x19UpdateObjectGroupResponse\x12S\n\x0cobject_group\x18\x01 \x01(\x0b\x32\x30.aruna.api.storage.models.v1.ObjectGroupOverviewR\x0bobjectGroup\"[\n\x19GetObjectGroupByIdRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\"q\n\x1aGetObjectGroupByIdResponse\x12S\n\x0cobject_group\x18\x01 \x01(\x0b\x32\x30.aruna.api.storage.models.v1.ObjectGroupOverviewR\x0bobjectGroup\"\xb1\x01\n GetObjectGroupsFromObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\x12K\n\x0cpage_request\x18\x03 \x01(\x0b\x32(.aruna.api.storage.models.v1.PageRequestR\x0bpageRequest\"{\n!GetObjectGroupsFromObjectResponse\x12V\n\robject_groups\x18\x01 \x01(\x0b\x32\x31.aruna.api.storage.models.v1.ObjectGroupOverviewsR\x0cobjectGroups\"Z\n\x18\x44\x65leteObjectGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\"\x1b\n\x19\x44\x65leteObjectGroupResponse\"\xdf\x01\n\x16GetObjectGroupsRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12K\n\x0cpage_request\x18\x02 \x01(\x0b\x32(.aruna.api.storage.models.v1.PageRequestR\x0bpageRequest\x12S\n\x0flabel_id_filter\x18\x03 \x01(\x0b\x32+.aruna.api.storage.models.v1.LabelOrIDQueryR\rlabelIdFilter\"q\n\x17GetObjectGroupsResponse\x12V\n\robject_groups\x18\x01 \x01(\x0b\x32\x31.aruna.api.storage.models.v1.ObjectGroupOverviewsR\x0cobjectGroups\"\xab\x01\n\x1cGetObjectGroupHistoryRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x19\n\x08group_id\x18\x02 \x01(\tR\x07groupId\x12K\n\x0cpage_request\x18\x03 \x01(\x0b\x32(.aruna.api.storage.models.v1.PageRequestR\x0bpageRequest\"w\n\x1dGetObjectGroupHistoryResponse\x12V\n\robject_groups\x18\x01 \x01(\x0b\x32\x31.aruna.api.storage.models.v1.ObjectGroupOverviewsR\x0cobjectGroups\"\xc8\x01\n\x1cGetObjectGroupObjectsRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x19\n\x08group_id\x18\x02 \x01(\tR\x07groupId\x12K\n\x0cpage_request\x18\x03 \x01(\x0b\x32(.aruna.api.storage.models.v1.PageRequestR\x0bpageRequest\x12\x1b\n\tmeta_only\x18\x04 \x01(\x08R\x08metaOnly\"q\n\x11ObjectGroupObject\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x06object\x12\x1f\n\x0bis_metadata\x18\x02 \x01(\x08R\nisMetadata\"\x83\x01\n\x1dGetObjectGroupObjectsResponse\x12\x62\n\x14object_group_objects\x18\x01 \x03(\x0b\x32\x30.aruna.api.storage.services.v1.ObjectGroupObjectR\x12objectGroupObjects2\xda\x0c\n\x12ObjectGroupService\x12\xb7\x01\n\x11\x43reateObjectGroup\x12\x37.aruna.api.storage.services.v1.CreateObjectGroupRequest\x1a\x38.aruna.api.storage.services.v1.CreateObjectGroupResponse\"/\x82\xd3\xe4\x93\x02):\x01*\"$/v1/collection/{collection_id}/group\x12\xc2\x01\n\x11UpdateObjectGroup\x12\x37.aruna.api.storage.services.v1.UpdateObjectGroupRequest\x1a\x38.aruna.api.storage.services.v1.UpdateObjectGroupResponse\":\x82\xd3\xe4\x93\x02\x34:\x01*\"//v1/collection/{collection_id}/group/{group_id}\x12\xc2\x01\n\x12GetObjectGroupById\x12\x38.aruna.api.storage.services.v1.GetObjectGroupByIdRequest\x1a\x39.aruna.api.storage.services.v1.GetObjectGroupByIdResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//v1/collection/{collection_id}/group/{group_id}\x12\xe0\x01\n\x19GetObjectGroupsFromObject\x12?.aruna.api.storage.services.v1.GetObjectGroupsFromObjectRequest\x1a@.aruna.api.storage.services.v1.GetObjectGroupsFromObjectResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/v1/collection/{collection_id}/object/{object_id}/groups\x12\xae\x01\n\x0fGetObjectGroups\x12\x35.aruna.api.storage.services.v1.GetObjectGroupsRequest\x1a\x36.aruna.api.storage.services.v1.GetObjectGroupsResponse\",\x82\xd3\xe4\x93\x02&\x12$/v1/collection/{collection_id}/group\x12\xd3\x01\n\x15GetObjectGroupHistory\x12;.aruna.api.storage.services.v1.GetObjectGroupHistoryRequest\x1a<.aruna.api.storage.services.v1.GetObjectGroupHistoryResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/collection/{collection_id}/group/{group_id}/history\x12\xd3\x01\n\x15GetObjectGroupObjects\x12;.aruna.api.storage.services.v1.GetObjectGroupObjectsRequest\x1a<.aruna.api.storage.services.v1.GetObjectGroupObjectsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/collection/{collection_id}/group/{group_id}/objects\x12\xbf\x01\n\x11\x44\x65leteObjectGroup\x12\x37.aruna.api.storage.services.v1.DeleteObjectGroupRequest\x1a\x38.aruna.api.storage.services.v1.DeleteObjectGroupResponse\"7\x82\xd3\xe4\x93\x02\x31*//v1/collection/{collection_id}/group/{group_id}B\x94\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x12ObjectGroupServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v1.objectgroup_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\022ObjectGroupServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1'
  _OBJECTGROUPSERVICE.methods_by_name['CreateObjectGroup']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['CreateObjectGroup']._serialized_options = b'\202\323\344\223\002):\001*\"$/v1/collection/{collection_id}/group'
  _OBJECTGROUPSERVICE.methods_by_name['UpdateObjectGroup']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['UpdateObjectGroup']._serialized_options = b'\202\323\344\223\0024:\001*\"//v1/collection/{collection_id}/group/{group_id}'
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupById']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupById']._serialized_options = b'\202\323\344\223\0021\022//v1/collection/{collection_id}/group/{group_id}'
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupsFromObject']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupsFromObject']._serialized_options = b'\202\323\344\223\002:\0228/v1/collection/{collection_id}/object/{object_id}/groups'
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroups']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroups']._serialized_options = b'\202\323\344\223\002&\022$/v1/collection/{collection_id}/group'
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupHistory']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupHistory']._serialized_options = b'\202\323\344\223\0029\0227/v1/collection/{collection_id}/group/{group_id}/history'
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupObjects']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['GetObjectGroupObjects']._serialized_options = b'\202\323\344\223\0029\0227/v1/collection/{collection_id}/group/{group_id}/objects'
  _OBJECTGROUPSERVICE.methods_by_name['DeleteObjectGroup']._options = None
  _OBJECTGROUPSERVICE.methods_by_name['DeleteObjectGroup']._serialized_options = b'\202\323\344\223\0021*//v1/collection/{collection_id}/group/{group_id}'
  _CREATEOBJECTGROUPREQUEST._serialized_start=204
  _CREATEOBJECTGROUPREQUEST._serialized_end=516
  _CREATEOBJECTGROUPRESPONSE._serialized_start=518
  _CREATEOBJECTGROUPRESPONSE._serialized_end=630
  _UPDATEOBJECTGROUPREQUEST._serialized_start=633
  _UPDATEOBJECTGROUPREQUEST._serialized_end=972
  _UPDATEOBJECTGROUPRESPONSE._serialized_start=974
  _UPDATEOBJECTGROUPRESPONSE._serialized_end=1086
  _GETOBJECTGROUPBYIDREQUEST._serialized_start=1088
  _GETOBJECTGROUPBYIDREQUEST._serialized_end=1179
  _GETOBJECTGROUPBYIDRESPONSE._serialized_start=1181
  _GETOBJECTGROUPBYIDRESPONSE._serialized_end=1294
  _GETOBJECTGROUPSFROMOBJECTREQUEST._serialized_start=1297
  _GETOBJECTGROUPSFROMOBJECTREQUEST._serialized_end=1474
  _GETOBJECTGROUPSFROMOBJECTRESPONSE._serialized_start=1476
  _GETOBJECTGROUPSFROMOBJECTRESPONSE._serialized_end=1599
  _DELETEOBJECTGROUPREQUEST._serialized_start=1601
  _DELETEOBJECTGROUPREQUEST._serialized_end=1691
  _DELETEOBJECTGROUPRESPONSE._serialized_start=1693
  _DELETEOBJECTGROUPRESPONSE._serialized_end=1720
  _GETOBJECTGROUPSREQUEST._serialized_start=1723
  _GETOBJECTGROUPSREQUEST._serialized_end=1946
  _GETOBJECTGROUPSRESPONSE._serialized_start=1948
  _GETOBJECTGROUPSRESPONSE._serialized_end=2061
  _GETOBJECTGROUPHISTORYREQUEST._serialized_start=2064
  _GETOBJECTGROUPHISTORYREQUEST._serialized_end=2235
  _GETOBJECTGROUPHISTORYRESPONSE._serialized_start=2237
  _GETOBJECTGROUPHISTORYRESPONSE._serialized_end=2356
  _GETOBJECTGROUPOBJECTSREQUEST._serialized_start=2359
  _GETOBJECTGROUPOBJECTSREQUEST._serialized_end=2559
  _OBJECTGROUPOBJECT._serialized_start=2561
  _OBJECTGROUPOBJECT._serialized_end=2674
  _GETOBJECTGROUPOBJECTSRESPONSE._serialized_start=2677
  _GETOBJECTGROUPOBJECTSRESPONSE._serialized_end=2808
  _OBJECTGROUPSERVICE._serialized_start=2811
  _OBJECTGROUPSERVICE._serialized_end=4437
# @@protoc_insertion_point(module_scope)
