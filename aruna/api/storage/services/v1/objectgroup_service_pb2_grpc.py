# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v1 import objectgroup_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2


class ObjectGroupServiceStub(object):
    """ObjectService

    Contains all methods that get/create or update Objects and associated resource
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateObjectGroup = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/CreateObjectGroup',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.CreateObjectGroupRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.CreateObjectGroupResponse.FromString,
                )
        self.UpdateObjectGroup = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/UpdateObjectGroup',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.UpdateObjectGroupRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.UpdateObjectGroupResponse.FromString,
                )
        self.GetObjectGroupById = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupById',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupByIdRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupByIdResponse.FromString,
                )
        self.GetObjectGroupsFromObject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupsFromObject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsFromObjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsFromObjectResponse.FromString,
                )
        self.GetObjectGroups = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroups',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsResponse.FromString,
                )
        self.GetObjectGroupHistory = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupHistory',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupHistoryRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupHistoryResponse.FromString,
                )
        self.GetObjectGroupObjects = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupObjects',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupObjectsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupObjectsResponse.FromString,
                )
        self.DeleteObjectGroup = channel.unary_unary(
                '/aruna.api.storage.services.v1.ObjectGroupService/DeleteObjectGroup',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.DeleteObjectGroupRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.DeleteObjectGroupResponse.FromString,
                )


class ObjectGroupServiceServicer(object):
    """ObjectService

    Contains all methods that get/create or update Objects and associated resource
    """

    def CreateObjectGroup(self, request, context):
        """CreateObjectGroup

        This creates a new ObjectGroup in the collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateObjectGroup(self, request, context):
        """UpdateObjectGroup

        This creates an updated ObjectGroup
        ObjectGroups are immutable
        Updating an ObjectGroup will create a new Revision of the ObjectGroup
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroupById(self, request, context):
        """GetObjectGroupById

        This gets a specific ObjectGroup by ID
        By default the latest revision is always returned, older revisions need to
        be specified separately
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroupsFromObject(self, request, context):
        """GetObjectGroupsFromObject

        This gets all ObjectGroups associated to a specific
        Object Objects can be part of multiple ObjectGroups at once
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroups(self, request, context):
        """GetObjectGroups

        This is a request that returns a (paginated) list of
        ObjectGroups that contain a specific set of labels.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroupHistory(self, request, context):
        """GetObjectGroupHistory

        This requests a full history with all objectgroups
        that are part of this objectgroups history
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroupObjects(self, request, context):
        """GetObjectGroupObjects

        Requests a list of paginated objects associated with this
        specific objectgroup
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteObjectGroup(self, request, context):
        """DeleteObjectGroup

        This is a request that deletes a specified ObjectGroup
        This does not delete the associated Objects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateObjectGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateObjectGroup,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.CreateObjectGroupRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.CreateObjectGroupResponse.SerializeToString,
            ),
            'UpdateObjectGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateObjectGroup,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.UpdateObjectGroupRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.UpdateObjectGroupResponse.SerializeToString,
            ),
            'GetObjectGroupById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroupById,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupByIdRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupByIdResponse.SerializeToString,
            ),
            'GetObjectGroupsFromObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroupsFromObject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsFromObjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsFromObjectResponse.SerializeToString,
            ),
            'GetObjectGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroups,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsResponse.SerializeToString,
            ),
            'GetObjectGroupHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroupHistory,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupHistoryRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupHistoryResponse.SerializeToString,
            ),
            'GetObjectGroupObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroupObjects,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupObjectsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupObjectsResponse.SerializeToString,
            ),
            'DeleteObjectGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteObjectGroup,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.DeleteObjectGroupRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.DeleteObjectGroupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v1.ObjectGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObjectGroupService(object):
    """ObjectService

    Contains all methods that get/create or update Objects and associated resource
    """

    @staticmethod
    def CreateObjectGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/CreateObjectGroup',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.CreateObjectGroupRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.CreateObjectGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateObjectGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/UpdateObjectGroup',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.UpdateObjectGroupRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.UpdateObjectGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroupById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupById',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupByIdRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroupsFromObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupsFromObject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsFromObjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsFromObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroups',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroupHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupHistory',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupHistoryRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupHistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroupObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/GetObjectGroupObjects',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupObjectsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.GetObjectGroupObjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteObjectGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ObjectGroupService/DeleteObjectGroup',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.DeleteObjectGroupRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_objectgroup__service__pb2.DeleteObjectGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)