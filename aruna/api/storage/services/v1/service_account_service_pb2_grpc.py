# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v1 import service_account_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2


class ServiceAccountServiceStub(object):
    """ServiceAccountService

    Service that contains all methods for service_accounts, these are Accounts that are
    project specific (or global) and can be used for automation. 
    Service account users will always contain (bot) behind their name
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateServiceAccount = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/CreateServiceAccount',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountResponse.FromString,
                )
        self.CreateServiceAccountToken = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/CreateServiceAccountToken',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountTokenRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountTokenResponse.FromString,
                )
        self.EditServiceAccountPermission = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/EditServiceAccountPermission',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.EditServiceAccountPermissionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.EditServiceAccountPermissionResponse.FromString,
                )
        self.GetServiceAccountToken = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/GetServiceAccountToken',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokenRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokenResponse.FromString,
                )
        self.GetServiceAccountTokens = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/GetServiceAccountTokens',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokensRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokensResponse.FromString,
                )
        self.GetServiceAccountsByProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/GetServiceAccountsByProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountsByProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountsByProjectResponse.FromString,
                )
        self.DeleteServiceAccountToken = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/DeleteServiceAccountToken',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokenRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokenResponse.FromString,
                )
        self.DeleteServiceAccountTokens = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/DeleteServiceAccountTokens',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokensRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokensResponse.FromString,
                )
        self.DeleteServiceAccount = channel.unary_unary(
                '/aruna.api.storage.services.v1.ServiceAccountService/DeleteServiceAccount',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountResponse.FromString,
                )


class ServiceAccountServiceServicer(object):
    """ServiceAccountService

    Service that contains all methods for service_accounts, these are Accounts that are
    project specific (or global) and can be used for automation. 
    Service account users will always contain (bot) behind their name
    """

    def CreateServiceAccount(self, request, context):
        """CreateServiceAccount

        Creates a service account for a given project
        If the service account has permissions for the global Admin project
        it will be a global service account that can interact with any resource
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateServiceAccountToken(self, request, context):
        """CreateServiceAccountToken

        Creates a token for a service account
        Each service account can only have one permission -> The token will have the same permission as the
        service account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditServiceAccountPermission(self, request, context):
        """EditServiceAccountPermission

        Overwrites the project specific permissions for a service account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceAccountToken(self, request, context):
        """GetServiceAccountToken

        This requests the overall information about a specifc service account token (by id)
        it will not contain the token itself.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceAccountTokens(self, request, context):
        """GetServiceAccountTokens

        This requests the overall information about all service account tokens
        it will not contain the token itself.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceAccountsByProject(self, request, context):
        """GetServiceAccountsByProject

        Will request all service_accounts for a given project
        each service account is bound to a specific project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteServiceAccountToken(self, request, context):
        """DeleteServiceAccountToken

        Deletes one service account token by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteServiceAccountTokens(self, request, context):
        """DeleteServiceAccountTokens

        Deletes all service account tokens
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteServiceAccount(self, request, context):
        """DeleteServiceAccount

        Deletes a service account (by id)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceAccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateServiceAccount,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountResponse.SerializeToString,
            ),
            'CreateServiceAccountToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateServiceAccountToken,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountTokenRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountTokenResponse.SerializeToString,
            ),
            'EditServiceAccountPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.EditServiceAccountPermission,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.EditServiceAccountPermissionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.EditServiceAccountPermissionResponse.SerializeToString,
            ),
            'GetServiceAccountToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAccountToken,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokenRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokenResponse.SerializeToString,
            ),
            'GetServiceAccountTokens': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAccountTokens,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokensRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokensResponse.SerializeToString,
            ),
            'GetServiceAccountsByProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAccountsByProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountsByProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountsByProjectResponse.SerializeToString,
            ),
            'DeleteServiceAccountToken': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteServiceAccountToken,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokenRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokenResponse.SerializeToString,
            ),
            'DeleteServiceAccountTokens': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteServiceAccountTokens,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokensRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokensResponse.SerializeToString,
            ),
            'DeleteServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteServiceAccount,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v1.ServiceAccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServiceAccountService(object):
    """ServiceAccountService

    Service that contains all methods for service_accounts, these are Accounts that are
    project specific (or global) and can be used for automation. 
    Service account users will always contain (bot) behind their name
    """

    @staticmethod
    def CreateServiceAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/CreateServiceAccount',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateServiceAccountToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/CreateServiceAccountToken',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountTokenRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.CreateServiceAccountTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditServiceAccountPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/EditServiceAccountPermission',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.EditServiceAccountPermissionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.EditServiceAccountPermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceAccountToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/GetServiceAccountToken',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokenRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceAccountTokens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/GetServiceAccountTokens',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokensRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountTokensResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceAccountsByProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/GetServiceAccountsByProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountsByProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.GetServiceAccountsByProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteServiceAccountToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/DeleteServiceAccountToken',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokenRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteServiceAccountTokens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/DeleteServiceAccountTokens',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokensRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountTokensResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteServiceAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ServiceAccountService/DeleteServiceAccount',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
