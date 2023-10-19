# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/project_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3aruna/api/storage/services/v2/project_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xe6\x02\n\x14\x43reateProjectRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x44\n\nkey_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\tkeyValues\x12\\\n\x12\x65xternal_relations\x18\x04 \x03(\x0b\x32-.aruna.api.storage.models.v2.ExternalRelationR\x11\x65xternalRelations\x12\x45\n\ndata_class\x18\x05 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\x12-\n\x12preferred_endpoint\x18\x06 \x01(\tR\x11preferredEndpoint\"W\n\x15\x43reateProjectResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project\"2\n\x11GetProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"T\n\x12GetProjectResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project\"5\n\x12GetProjectsRequest\x12\x1f\n\x0bproject_ids\x18\x01 \x03(\tR\nprojectIds\"W\n\x13GetProjectsResponse\x12@\n\x08projects\x18\x01 \x03(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x08projects\"5\n\x14\x44\x65leteProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x17\n\x15\x44\x65leteProjectResponse\"M\n\x18UpdateProjectNameRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"[\n\x19UpdateProjectNameResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project\"b\n\x1fUpdateProjectDescriptionRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"b\n UpdateProjectDescriptionResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project\"\xde\x01\n\x1dUpdateProjectKeyValuesRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12K\n\x0e\x61\x64\x64_key_values\x18\x02 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0c\x61\x64\x64KeyValues\x12Q\n\x11remove_key_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0fremoveKeyValues\"`\n\x1eUpdateProjectKeyValuesResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project\"\x85\x01\n\x1dUpdateProjectDataClassRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x45\n\ndata_class\x18\x02 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\"`\n\x1eUpdateProjectDataClassResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project\"6\n\x15\x41rchiveProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"X\n\x16\x41rchiveProjectResponse\x12>\n\x07project\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.ProjectR\x07project2\xa6\x0c\n\x0eProjectService\x12\x92\x01\n\rCreateProject\x12\x33.aruna.api.storage.services.v2.CreateProjectRequest\x1a\x34.aruna.api.storage.services.v2.CreateProjectResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/v2/project:\x01*\x12\x93\x01\n\nGetProject\x12\x30.aruna.api.storage.services.v2.GetProjectRequest\x1a\x31.aruna.api.storage.services.v2.GetProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v2/project/{project_id}\x12\x8a\x01\n\x0bGetProjects\x12\x31.aruna.api.storage.services.v2.GetProjectsRequest\x1a\x32.aruna.api.storage.services.v2.GetProjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v2/projects\x12\x9c\x01\n\rDeleteProject\x12\x33.aruna.api.storage.services.v2.DeleteProjectRequest\x1a\x34.aruna.api.storage.services.v2.DeleteProjectResponse\" \x82\xd3\xe4\x93\x02\x1a*\x18/v2/project/{project_id}\x12\xb0\x01\n\x11UpdateProjectName\x12\x37.aruna.api.storage.services.v2.UpdateProjectNameRequest\x1a\x38.aruna.api.storage.services.v2.UpdateProjectNameResponse\"(\x82\xd3\xe4\x93\x02\"2\x1d/v2/project/{project_id}/name:\x01*\x12\xcc\x01\n\x18UpdateProjectDescription\x12>.aruna.api.storage.services.v2.UpdateProjectDescriptionRequest\x1a?.aruna.api.storage.services.v2.UpdateProjectDescriptionResponse\"/\x82\xd3\xe4\x93\x02)2$/v2/project/{project_id}/description:\x01*\x12\xc5\x01\n\x16UpdateProjectKeyValues\x12<.aruna.api.storage.services.v2.UpdateProjectKeyValuesRequest\x1a=.aruna.api.storage.services.v2.UpdateProjectKeyValuesResponse\".\x82\xd3\xe4\x93\x02(2#/v2/project/{project_id}/key_values:\x01*\x12\xc5\x01\n\x16UpdateProjectDataClass\x12<.aruna.api.storage.services.v2.UpdateProjectDataClassRequest\x1a=.aruna.api.storage.services.v2.UpdateProjectDataClassResponse\".\x82\xd3\xe4\x93\x02(2#/v2/project/{project_id}/data_class:\x01*\x12\xaa\x01\n\x0e\x41rchiveProject\x12\x34.aruna.api.storage.services.v2.ArchiveProjectRequest\x1a\x35.aruna.api.storage.services.v2.ArchiveProjectResponse\"+\x82\xd3\xe4\x93\x02%\" /v2/project/{project_id}/archive:\x01*B\xe7\x02\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x0eProjectServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v2\x92\x41\xd3\x01\x12\x33\n#Aruna Object Storage (AOS) REST API2\x0c\x32.0.0-beta.5*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZ`\n^\n\rAccessKeyAuth\x12M\x08\x02\x12\x38\x41uthentication token, prefixed by Bearer: Bearer <token>\x1a\rAuthorization \x02\x62\x13\n\x11\n\rAccessKeyAuth\x12\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.project_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\016ProjectServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v2\222A\323\001\0223\n#Aruna Object Storage (AOS) REST API2\0142.0.0-beta.5*\001\0022\020application/json:\020application/jsonZ`\n^\n\rAccessKeyAuth\022M\010\002\0228Authentication token, prefixed by Bearer: Bearer <token>\032\rAuthorization \002b\023\n\021\n\rAccessKeyAuth\022\000'
  _globals['_PROJECTSERVICE'].methods_by_name['CreateProject']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002\020\"\013/v2/project:\001*'
  _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\032\022\030/v2/project/{project_id}'
  _globals['_PROJECTSERVICE'].methods_by_name['GetProjects']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['GetProjects']._serialized_options = b'\202\323\344\223\002\016\022\014/v2/projects'
  _globals['_PROJECTSERVICE'].methods_by_name['DeleteProject']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['DeleteProject']._serialized_options = b'\202\323\344\223\002\032*\030/v2/project/{project_id}'
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectName']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectName']._serialized_options = b'\202\323\344\223\002\"2\035/v2/project/{project_id}/name:\001*'
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectDescription']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectDescription']._serialized_options = b'\202\323\344\223\002)2$/v2/project/{project_id}/description:\001*'
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectKeyValues']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectKeyValues']._serialized_options = b'\202\323\344\223\002(2#/v2/project/{project_id}/key_values:\001*'
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectDataClass']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['UpdateProjectDataClass']._serialized_options = b'\202\323\344\223\002(2#/v2/project/{project_id}/data_class:\001*'
  _globals['_PROJECTSERVICE'].methods_by_name['ArchiveProject']._options = None
  _globals['_PROJECTSERVICE'].methods_by_name['ArchiveProject']._serialized_options = b'\202\323\344\223\002%\" /v2/project/{project_id}/archive:\001*'
  _globals['_CREATEPROJECTREQUEST']._serialized_start=207
  _globals['_CREATEPROJECTREQUEST']._serialized_end=565
  _globals['_CREATEPROJECTRESPONSE']._serialized_start=567
  _globals['_CREATEPROJECTRESPONSE']._serialized_end=654
  _globals['_GETPROJECTREQUEST']._serialized_start=656
  _globals['_GETPROJECTREQUEST']._serialized_end=706
  _globals['_GETPROJECTRESPONSE']._serialized_start=708
  _globals['_GETPROJECTRESPONSE']._serialized_end=792
  _globals['_GETPROJECTSREQUEST']._serialized_start=794
  _globals['_GETPROJECTSREQUEST']._serialized_end=847
  _globals['_GETPROJECTSRESPONSE']._serialized_start=849
  _globals['_GETPROJECTSRESPONSE']._serialized_end=936
  _globals['_DELETEPROJECTREQUEST']._serialized_start=938
  _globals['_DELETEPROJECTREQUEST']._serialized_end=991
  _globals['_DELETEPROJECTRESPONSE']._serialized_start=993
  _globals['_DELETEPROJECTRESPONSE']._serialized_end=1016
  _globals['_UPDATEPROJECTNAMEREQUEST']._serialized_start=1018
  _globals['_UPDATEPROJECTNAMEREQUEST']._serialized_end=1095
  _globals['_UPDATEPROJECTNAMERESPONSE']._serialized_start=1097
  _globals['_UPDATEPROJECTNAMERESPONSE']._serialized_end=1188
  _globals['_UPDATEPROJECTDESCRIPTIONREQUEST']._serialized_start=1190
  _globals['_UPDATEPROJECTDESCRIPTIONREQUEST']._serialized_end=1288
  _globals['_UPDATEPROJECTDESCRIPTIONRESPONSE']._serialized_start=1290
  _globals['_UPDATEPROJECTDESCRIPTIONRESPONSE']._serialized_end=1388
  _globals['_UPDATEPROJECTKEYVALUESREQUEST']._serialized_start=1391
  _globals['_UPDATEPROJECTKEYVALUESREQUEST']._serialized_end=1613
  _globals['_UPDATEPROJECTKEYVALUESRESPONSE']._serialized_start=1615
  _globals['_UPDATEPROJECTKEYVALUESRESPONSE']._serialized_end=1711
  _globals['_UPDATEPROJECTDATACLASSREQUEST']._serialized_start=1714
  _globals['_UPDATEPROJECTDATACLASSREQUEST']._serialized_end=1847
  _globals['_UPDATEPROJECTDATACLASSRESPONSE']._serialized_start=1849
  _globals['_UPDATEPROJECTDATACLASSRESPONSE']._serialized_end=1945
  _globals['_ARCHIVEPROJECTREQUEST']._serialized_start=1947
  _globals['_ARCHIVEPROJECTREQUEST']._serialized_end=2001
  _globals['_ARCHIVEPROJECTRESPONSE']._serialized_start=2003
  _globals['_ARCHIVEPROJECTRESPONSE']._serialized_end=2091
  _globals['_PROJECTSERVICE']._serialized_start=2094
  _globals['_PROJECTSERVICE']._serialized_end=3668
# @@protoc_insertion_point(module_scope)