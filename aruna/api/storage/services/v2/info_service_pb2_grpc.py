# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v2 import info_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2


class StorageStatusServiceStub(object):
    """StorageStatusService

    This is a generic service that contains utility functions 
    these functions are used to query additional meta-information
    about the status of the overall storage architecture
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStorageVersion = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetStorageVersion',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionResponse.FromString,
                )
        self.GetStorageStatus = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetStorageStatus',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusResponse.FromString,
                )
        self.GetPubkeys = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetPubkeys',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysResponse.FromString,
                )
        self.GetAnouncements = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetAnouncements',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnouncementsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnouncementsResponse.FromString,
                )
        self.SetAnouncements = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/SetAnouncements',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnouncementsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnouncementsResponse.FromString,
                )


class StorageStatusServiceServicer(object):
    """StorageStatusService

    This is a generic service that contains utility functions 
    these functions are used to query additional meta-information
    about the status of the overall storage architecture
    """

    def GetStorageVersion(self, request, context):
        """GetStorageVersion

        Status: BETA

        A request to get the current version of the server application
        String representation and https://semver.org/
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStorageStatus(self, request, context):
        """GetStorageStatus

        Status: ALPHA

        A request to get the current status of the storage components by location(s)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPubkeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnouncements(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAnouncements(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageStatusServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStorageVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorageVersion,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionResponse.SerializeToString,
            ),
            'GetStorageStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorageStatus,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusResponse.SerializeToString,
            ),
            'GetPubkeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPubkeys,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysResponse.SerializeToString,
            ),
            'GetAnouncements': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnouncements,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnouncementsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnouncementsResponse.SerializeToString,
            ),
            'SetAnouncements': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAnouncements,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnouncementsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnouncementsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v2.StorageStatusService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StorageStatusService(object):
    """StorageStatusService

    This is a generic service that contains utility functions 
    these functions are used to query additional meta-information
    about the status of the overall storage architecture
    """

    @staticmethod
    def GetStorageVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetStorageVersion',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStorageStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetStorageStatus',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPubkeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetPubkeys',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnouncements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetAnouncements',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnouncementsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnouncementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAnouncements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/SetAnouncements',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnouncementsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnouncementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)