# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/workspace_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5aruna/api/storage/services/v2/workspace_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/api/visibility.proto\"\xc7\x01\n\x1e\x43reateWorkspaceTemplateRequest\x12\x19\n\x08owner_id\x18\x01 \x01(\tR\x07ownerId\x12\x16\n\x06prefix\x18\x02 \x01(\tR\x06prefix\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x19\n\x08hook_ids\x18\x05 \x03(\tR\x07hookIds\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12!\n\x0c\x65ndpoint_ids\x18\x07 \x03(\tR\x0b\x65ndpointIds\"B\n\x1f\x43reateWorkspaceTemplateResponse\x12\x1f\n\x0btemplate_id\x18\x01 \x01(\tR\ntemplateId\">\n\x1bGetWorkspaceTemplateRequest\x12\x1f\n\x0btemplate_id\x18\x01 \x01(\tR\ntemplateId\"j\n\x1cGetWorkspaceTemplateResponse\x12J\n\tworkspace\x18\x01 \x01(\x0b\x32,.aruna.api.storage.services.v2.WorkspaceInfoR\tworkspace\"A\n\x1e\x44\x65leteWorkspaceTemplateRequest\x12\x1f\n\x0btemplate_id\x18\x01 \x01(\tR\ntemplateId\"!\n\x1f\x44\x65leteWorkspaceTemplateResponse\"$\n\"ListOwnedWorkspaceTemplatesRequest\"s\n#ListOwnedWorkspaceTemplatesResponse\x12L\n\nworkspaces\x18\x01 \x03(\x0b\x32,.aruna.api.storage.services.v2.WorkspaceInfoR\nworkspaces\"\xd4\x01\n\rWorkspaceInfo\x12!\n\x0cworkspace_id\x18\x01 \x01(\tR\x0bworkspaceId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05owner\x18\x04 \x01(\tR\x05owner\x12\x16\n\x06prefix\x18\x05 \x01(\tR\x06prefix\x12\x19\n\x08hook_ids\x18\x06 \x01(\tR\x07hookIds\x12!\n\x0c\x65ndpoint_ids\x18\x07 \x01(\tR\x0b\x65ndpointIds\"i\n\x16\x43reateWorkspaceRequest\x12-\n\x12workspace_template\x18\x01 \x01(\tR\x11workspaceTemplate\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"\x90\x01\n\x17\x43reateWorkspaceResponse\x12!\n\x0cworkspace_id\x18\x01 \x01(\tR\x0bworkspaceId\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\x12\x1d\n\naccess_key\x18\x03 \x01(\tR\taccessKey\x12\x1d\n\nsecret_key\x18\x04 \x01(\tR\tsecretKey\";\n\x16\x44\x65leteWorkspaceRequest\x12!\n\x0cworkspace_id\x18\x01 \x01(\tR\x0bworkspaceId\"\x19\n\x17\x44\x65leteWorkspaceResponse\"P\n\x15\x43laimWorkspaceRequest\x12!\n\x0cworkspace_id\x18\x01 \x01(\tR\x0bworkspaceId\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\x18\n\x16\x43laimWorkspaceResponse2\xb6\n\n\x10WorkspaceService\x12\xbd\x01\n\x17\x43reateWorkspaceTemplate\x12=.aruna.api.storage.services.v2.CreateWorkspaceTemplateRequest\x1a>.aruna.api.storage.services.v2.CreateWorkspaceTemplateResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v2/workspaces/templates:\x01*\x12\xbf\x01\n\x14GetWorkspaceTemplate\x12:.aruna.api.storage.services.v2.GetWorkspaceTemplateRequest\x1a;.aruna.api.storage.services.v2.GetWorkspaceTemplateResponse\".\x82\xd3\xe4\x93\x02(\x12&/v2/workspaces/templates/{template_id}\x12\xc6\x01\n\x1bListOwnedWorkspaceTemplates\x12\x41.aruna.api.storage.services.v2.ListOwnedWorkspaceTemplatesRequest\x1a\x42.aruna.api.storage.services.v2.ListOwnedWorkspaceTemplatesResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v2/workspaces/templates\x12\xcb\x01\n\x17\x44\x65leteWorkspaceTemplate\x12=.aruna.api.storage.services.v2.DeleteWorkspaceTemplateRequest\x1a>.aruna.api.storage.services.v2.DeleteWorkspaceTemplateResponse\"1\x82\xd3\xe4\x93\x02+*&/v2/workspaces/templates/{template_id}:\x01*\x12\x9b\x01\n\x0f\x43reateWorkspace\x12\x35.aruna.api.storage.services.v2.CreateWorkspaceRequest\x1a\x36.aruna.api.storage.services.v2.CreateWorkspaceResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v2/workspaces:\x01*\x12\xaa\x01\n\x0f\x44\x65leteWorkspace\x12\x35.aruna.api.storage.services.v2.DeleteWorkspaceRequest\x1a\x36.aruna.api.storage.services.v2.DeleteWorkspaceResponse\"(\x82\xd3\xe4\x93\x02\"*\x1d/v2/workspaces/{workspace_id}:\x01*\x12\xad\x01\n\x0e\x43laimWorkspace\x12\x34.aruna.api.storage.services.v2.ClaimWorkspaceRequest\x1a\x35.aruna.api.storage.services.v2.ClaimWorkspaceResponse\".\x82\xd3\xe4\x93\x02(\"#/v2/workspaces/{workspace_id}/claim:\x01*\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\x95\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x10WorkspaceServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.workspace_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\020WorkspaceServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_WORKSPACESERVICE']._options = None
  _globals['_WORKSPACESERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_WORKSPACESERVICE'].methods_by_name['CreateWorkspaceTemplate']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['CreateWorkspaceTemplate']._serialized_options = b'\202\323\344\223\002\035\"\030/v2/workspaces/templates:\001*'
  _globals['_WORKSPACESERVICE'].methods_by_name['GetWorkspaceTemplate']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['GetWorkspaceTemplate']._serialized_options = b'\202\323\344\223\002(\022&/v2/workspaces/templates/{template_id}'
  _globals['_WORKSPACESERVICE'].methods_by_name['ListOwnedWorkspaceTemplates']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['ListOwnedWorkspaceTemplates']._serialized_options = b'\202\323\344\223\002\032\022\030/v2/workspaces/templates'
  _globals['_WORKSPACESERVICE'].methods_by_name['DeleteWorkspaceTemplate']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['DeleteWorkspaceTemplate']._serialized_options = b'\202\323\344\223\002+*&/v2/workspaces/templates/{template_id}:\001*'
  _globals['_WORKSPACESERVICE'].methods_by_name['CreateWorkspace']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['CreateWorkspace']._serialized_options = b'\202\323\344\223\002\023\"\016/v2/workspaces:\001*'
  _globals['_WORKSPACESERVICE'].methods_by_name['DeleteWorkspace']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['DeleteWorkspace']._serialized_options = b'\202\323\344\223\002\"*\035/v2/workspaces/{workspace_id}:\001*'
  _globals['_WORKSPACESERVICE'].methods_by_name['ClaimWorkspace']._options = None
  _globals['_WORKSPACESERVICE'].methods_by_name['ClaimWorkspace']._serialized_options = b'\202\323\344\223\002(\"#/v2/workspaces/{workspace_id}/claim:\001*'
  _globals['_CREATEWORKSPACETEMPLATEREQUEST']._serialized_start=148
  _globals['_CREATEWORKSPACETEMPLATEREQUEST']._serialized_end=347
  _globals['_CREATEWORKSPACETEMPLATERESPONSE']._serialized_start=349
  _globals['_CREATEWORKSPACETEMPLATERESPONSE']._serialized_end=415
  _globals['_GETWORKSPACETEMPLATEREQUEST']._serialized_start=417
  _globals['_GETWORKSPACETEMPLATEREQUEST']._serialized_end=479
  _globals['_GETWORKSPACETEMPLATERESPONSE']._serialized_start=481
  _globals['_GETWORKSPACETEMPLATERESPONSE']._serialized_end=587
  _globals['_DELETEWORKSPACETEMPLATEREQUEST']._serialized_start=589
  _globals['_DELETEWORKSPACETEMPLATEREQUEST']._serialized_end=654
  _globals['_DELETEWORKSPACETEMPLATERESPONSE']._serialized_start=656
  _globals['_DELETEWORKSPACETEMPLATERESPONSE']._serialized_end=689
  _globals['_LISTOWNEDWORKSPACETEMPLATESREQUEST']._serialized_start=691
  _globals['_LISTOWNEDWORKSPACETEMPLATESREQUEST']._serialized_end=727
  _globals['_LISTOWNEDWORKSPACETEMPLATESRESPONSE']._serialized_start=729
  _globals['_LISTOWNEDWORKSPACETEMPLATESRESPONSE']._serialized_end=844
  _globals['_WORKSPACEINFO']._serialized_start=847
  _globals['_WORKSPACEINFO']._serialized_end=1059
  _globals['_CREATEWORKSPACEREQUEST']._serialized_start=1061
  _globals['_CREATEWORKSPACEREQUEST']._serialized_end=1166
  _globals['_CREATEWORKSPACERESPONSE']._serialized_start=1169
  _globals['_CREATEWORKSPACERESPONSE']._serialized_end=1313
  _globals['_DELETEWORKSPACEREQUEST']._serialized_start=1315
  _globals['_DELETEWORKSPACEREQUEST']._serialized_end=1374
  _globals['_DELETEWORKSPACERESPONSE']._serialized_start=1376
  _globals['_DELETEWORKSPACERESPONSE']._serialized_end=1401
  _globals['_CLAIMWORKSPACEREQUEST']._serialized_start=1403
  _globals['_CLAIMWORKSPACEREQUEST']._serialized_end=1483
  _globals['_CLAIMWORKSPACERESPONSE']._serialized_start=1485
  _globals['_CLAIMWORKSPACERESPONSE']._serialized_end=1509
  _globals['_WORKSPACESERVICE']._serialized_start=1512
  _globals['_WORKSPACESERVICE']._serialized_end=2846
# @@protoc_insertion_point(module_scope)
