# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/services/v1/dataset_service_models.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sciobjsdb.api.storage.models.v1 import dataset_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_dataset__pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_common__models__pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_object__models__pb2
from sciobjsdb.api.storage.services.v1 import dataset_object_service_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>sciobjsdb/api/storage/services/v1/dataset_service_models.proto\x12!sciobjsdb.api.storage.services.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-sciobjsdb/api/storage/models/v1/dataset.proto\x1a\x33sciobjsdb/api/storage/models/v1/common_models.proto\x1a\x33sciobjsdb/api/storage/models/v1/object_models.proto\x1a\x45sciobjsdb/api/storage/services/v1/dataset_object_service_models.proto\"\xdd\x02\n\x14\x43reateDatasetRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\nproject_id\x18\x03 \x01(\tR\tprojectId\x12>\n\x06labels\x18\x04 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12M\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32+.sciobjsdb.api.storage.models.v1.AnnotationR\x0b\x61nnotations\x12\x61\n\x10metadata_objects\x18\x06 \x03(\x0b\x32\x36.sciobjsdb.api.storage.services.v1.CreateObjectRequestR\x0fmetadataObjects\"\'\n\x15\x43reateDatasetResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"#\n\x11GetDatasetRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"X\n\x12GetDatasetResponse\x12\x42\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32(.sciobjsdb.api.storage.models.v1.DatasetR\x07\x64\x61taset\"\xcc\x01\n\x18GetDatasetObjectsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12O\n\x0cpage_request\x18\x02 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.PageRequestR\x0bpageRequest\x12O\n\x0clabel_filter\x18\x03 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.LabelFilterR\x0blabelFilter\"^\n\x19GetDatasetObjectsResponse\x12\x41\n\x07objects\x18\x01 \x03(\x0b\x32\'.sciobjsdb.api.storage.models.v1.ObjectR\x07objects\"+\n\x19GetDatasetVersionsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"x\n\x1aGetDatasetVersionsResponse\x12Z\n\x10\x64\x61taset_versions\x18\x01 \x03(\x0b\x32/.sciobjsdb.api.storage.models.v1.DatasetVersionR\x0f\x64\x61tasetVersions\"\xcb\x01\n\x1dGetDatasetObjectGroupsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12O\n\x0cpage_request\x18\x02 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.PageRequestR\x0bpageRequest\x12I\n\x0clabel_filter\x18\x03 \x01(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x0blabelFilter\"s\n\x1eGetDatasetObjectGroupsResponse\x12Q\n\robject_groups\x18\x01 \x03(\x0b\x32,.sciobjsdb.api.storage.models.v1.ObjectGroupR\x0cobjectGroups\"\x9b\x01\n)GetObjectGroupRevisionsInDateRangeRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x30\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\"\x98\x01\n*GetObjectGroupRevisionsInDateRangeResponse\x12j\n\x16object_group_revisions\x18\x01 \x03(\x0b\x32\x34.sciobjsdb.api.storage.models.v1.ObjectGroupRevisionR\x14objectGroupRevisions\"\x9a\t\n GetObjectGroupsStreamLinkRequest\x12o\n\x0bstream_type\x18\x03 \x01(\x0e\x32N.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.StreamTypeR\nstreamType\x12p\n\tgroup_ids\x18\x04 \x01(\x0b\x32Q.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.GroupIDsQueryH\x00R\x08groupIds\x12s\n\ndate_range\x18\x05 \x01(\x0b\x32R.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DateRangeQueryH\x00R\tdateRange\x12l\n\x07\x64\x61taset\x18\x06 \x01(\x0b\x32P.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DatasetQueryH\x00R\x07\x64\x61taset\x12\x82\x01\n\x0f\x64\x61taset_version\x18\x07 \x01(\x0b\x32W.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DatasetVersionQueryH\x00R\x0e\x64\x61tasetVersion\x12\x32\n\x06\x65xpiry\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x06\x65xpiry\x1a\x8f\x01\n\x0e\x44\x61teRangeQuery\x12\x1d\n\ndataset_id\x18\x03 \x01(\tR\tdatasetId\x12\x30\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\x1aS\n\rGroupIDsQuery\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12#\n\robject_groups\x18\x01 \x03(\tR\x0cobjectGroups\x1a-\n\x0c\x44\x61tasetQuery\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x1a\x62\n\x13\x44\x61tasetVersionQuery\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12,\n\x12\x64\x61taset_version_id\x18\x02 \x01(\tR\x10\x64\x61tasetVersionId\"t\n\nStreamType\x12\x1b\n\x17STREAM_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19STREAM_TYPE_BASE64NEWLINE\x10\x01\x12\x13\n\x0fSTREAM_TYPE_ZIP\x10\x02\x12\x15\n\x11STREAM_TYPE_TARGZ\x10\x03\x42\x07\n\x05query\"5\n!GetObjectGroupsStreamLinkResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"x\n\x19UpdateDatasetFieldRequest\x12[\n\x0eupdate_request\x18\x01 \x01(\x0b\x32\x34.sciobjsdb.api.storage.models.v1.UpdateFieldsRequestR\rupdateRequest\"\x1c\n\x1aUpdateDatasetFieldResponse\"&\n\x14\x44\x65leteDatasetRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x17\n\x15\x44\x65leteDatasetResponse\"\x81\x03\n\x1cReleaseDatasetVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12\x42\n\x07version\x18\x03 \x01(\x0b\x32(.sciobjsdb.api.storage.models.v1.VersionR\x07version\x12>\n\x06labels\x18\x04 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12M\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32+.sciobjsdb.api.storage.models.v1.AnnotationR\x0b\x61nnotations\x12\x39\n\x19object_group_revision_ids\x18\x07 \x03(\tR\x16objectGroupRevisionIds\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\"/\n\x1dReleaseDatasetVersionResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"*\n\x18GetDatasetVersionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"u\n\x19GetDatasetVersionResponse\x12X\n\x0f\x64\x61taset_version\x18\x01 \x01(\x0b\x32/.sciobjsdb.api.storage.models.v1.DatasetVersionR\x0e\x64\x61tasetVersion\"\x87\x01\n$GetDatasetVersionObjectGroupsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12O\n\x0cpage_request\x18\x02 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.PageRequestR\x0bpageRequest\"\x93\x01\n%GetDatasetVersionObjectGroupsResponse\x12j\n\x16object_group_revisions\x18\x01 \x03(\x0b\x32\x34.sciobjsdb.api.storage.models.v1.ObjectGroupRevisionR\x14objectGroupRevisions\"-\n\x1b\x44\x65leteDatasetVersionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x1e\n\x1c\x44\x65leteDatasetVersionResponseB\xa6\x01\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\x14\x44\x61tasetServiceModelsP\x01ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\024DatasetServiceModelsP\001ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1'
  _CREATEDATASETREQUEST._serialized_start=359
  _CREATEDATASETREQUEST._serialized_end=708
  _CREATEDATASETRESPONSE._serialized_start=710
  _CREATEDATASETRESPONSE._serialized_end=749
  _GETDATASETREQUEST._serialized_start=751
  _GETDATASETREQUEST._serialized_end=786
  _GETDATASETRESPONSE._serialized_start=788
  _GETDATASETRESPONSE._serialized_end=876
  _GETDATASETOBJECTSREQUEST._serialized_start=879
  _GETDATASETOBJECTSREQUEST._serialized_end=1083
  _GETDATASETOBJECTSRESPONSE._serialized_start=1085
  _GETDATASETOBJECTSRESPONSE._serialized_end=1179
  _GETDATASETVERSIONSREQUEST._serialized_start=1181
  _GETDATASETVERSIONSREQUEST._serialized_end=1224
  _GETDATASETVERSIONSRESPONSE._serialized_start=1226
  _GETDATASETVERSIONSRESPONSE._serialized_end=1346
  _GETDATASETOBJECTGROUPSREQUEST._serialized_start=1349
  _GETDATASETOBJECTGROUPSREQUEST._serialized_end=1552
  _GETDATASETOBJECTGROUPSRESPONSE._serialized_start=1554
  _GETDATASETOBJECTGROUPSRESPONSE._serialized_end=1669
  _GETOBJECTGROUPREVISIONSINDATERANGEREQUEST._serialized_start=1672
  _GETOBJECTGROUPREVISIONSINDATERANGEREQUEST._serialized_end=1827
  _GETOBJECTGROUPREVISIONSINDATERANGERESPONSE._serialized_start=1830
  _GETOBJECTGROUPREVISIONSINDATERANGERESPONSE._serialized_end=1982
  _GETOBJECTGROUPSSTREAMLINKREQUEST._serialized_start=1985
  _GETOBJECTGROUPSSTREAMLINKREQUEST._serialized_end=3163
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATERANGEQUERY._serialized_start=2661
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATERANGEQUERY._serialized_end=2804
  _GETOBJECTGROUPSSTREAMLINKREQUEST_GROUPIDSQUERY._serialized_start=2806
  _GETOBJECTGROUPSSTREAMLINKREQUEST_GROUPIDSQUERY._serialized_end=2889
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETQUERY._serialized_start=2891
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETQUERY._serialized_end=2936
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETVERSIONQUERY._serialized_start=2938
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETVERSIONQUERY._serialized_end=3036
  _GETOBJECTGROUPSSTREAMLINKREQUEST_STREAMTYPE._serialized_start=3038
  _GETOBJECTGROUPSSTREAMLINKREQUEST_STREAMTYPE._serialized_end=3154
  _GETOBJECTGROUPSSTREAMLINKRESPONSE._serialized_start=3165
  _GETOBJECTGROUPSSTREAMLINKRESPONSE._serialized_end=3218
  _UPDATEDATASETFIELDREQUEST._serialized_start=3220
  _UPDATEDATASETFIELDREQUEST._serialized_end=3340
  _UPDATEDATASETFIELDRESPONSE._serialized_start=3342
  _UPDATEDATASETFIELDRESPONSE._serialized_end=3370
  _DELETEDATASETREQUEST._serialized_start=3372
  _DELETEDATASETREQUEST._serialized_end=3410
  _DELETEDATASETRESPONSE._serialized_start=3412
  _DELETEDATASETRESPONSE._serialized_end=3435
  _RELEASEDATASETVERSIONREQUEST._serialized_start=3438
  _RELEASEDATASETVERSIONREQUEST._serialized_end=3823
  _RELEASEDATASETVERSIONRESPONSE._serialized_start=3825
  _RELEASEDATASETVERSIONRESPONSE._serialized_end=3872
  _GETDATASETVERSIONREQUEST._serialized_start=3874
  _GETDATASETVERSIONREQUEST._serialized_end=3916
  _GETDATASETVERSIONRESPONSE._serialized_start=3918
  _GETDATASETVERSIONRESPONSE._serialized_end=4035
  _GETDATASETVERSIONOBJECTGROUPSREQUEST._serialized_start=4038
  _GETDATASETVERSIONOBJECTGROUPSREQUEST._serialized_end=4173
  _GETDATASETVERSIONOBJECTGROUPSRESPONSE._serialized_start=4176
  _GETDATASETVERSIONOBJECTGROUPSRESPONSE._serialized_end=4323
  _DELETEDATASETVERSIONREQUEST._serialized_start=4325
  _DELETEDATASETVERSIONREQUEST._serialized_end=4370
  _DELETEDATASETVERSIONRESPONSE._serialized_start=4372
  _DELETEDATASETVERSIONRESPONSE._serialized_end=4402
# @@protoc_insertion_point(module_scope)
