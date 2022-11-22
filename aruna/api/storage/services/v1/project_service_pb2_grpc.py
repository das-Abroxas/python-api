# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v1 import project_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2


class ProjectServiceStub(object):
    """ProjectService

    Contains all methods that get/create or update Projects and associated resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/CreateProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.CreateProjectResponse.FromString,
                )
        self.AddUserToProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/AddUserToProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.AddUserToProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.AddUserToProjectResponse.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/GetProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectResponse.FromString,
                )
        self.GetProjects = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/GetProjects',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectsResponse.FromString,
                )
        self.DestroyProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/DestroyProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.DestroyProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.DestroyProjectResponse.FromString,
                )
        self.UpdateProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/UpdateProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.UpdateProjectResponse.FromString,
                )
        self.RemoveUserFromProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/RemoveUserFromProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.RemoveUserFromProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.RemoveUserFromProjectResponse.FromString,
                )
        self.GetUserPermissionsForProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/GetUserPermissionsForProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetUserPermissionsForProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetUserPermissionsForProjectResponse.FromString,
                )
        self.EditUserPermissionsForProject = channel.unary_unary(
                '/aruna.api.storage.services.v1.ProjectService/EditUserPermissionsForProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.EditUserPermissionsForProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.EditUserPermissionsForProjectResponse.FromString,
                )


class ProjectServiceServicer(object):
    """ProjectService

    Contains all methods that get/create or update Projects and associated resources
    """

    def CreateProject(self, request, context):
        """CreateProject

        Status: STABLE

        Creates a new project all users and collections are bundled in a project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserToProject(self, request, context):
        """AddUserToProject

        Status: STABLE

        Adds a new user to a given project by its id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """GetProject

        Status: STABLE

        Requests a project by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjects(self, request, context):
        """GetProjects

        Status: STABLE

        Admin request to get all projects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyProject(self, request, context):
        """DestroyProject

        Status: STABLE

        Destroys the project and all its associated data. Must be empty
        (cannot contain any collections).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProject(self, request, context):
        """UpdateProject

        Status: STABLE

        Updates the project. All (meta) data will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUserFromProject(self, request, context):
        """RemoveUserFromProject

        Status: STABLE

        Removes a specified user from the project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserPermissionsForProject(self, request, context):
        """GetUserPermissionsForProject

        Status: STABLE

        Get the user_permission of a specific user for the project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditUserPermissionsForProject(self, request, context):
        """EditUserPermissionsForProject

        Status: STABLE

        Modifies the user_permission of a specific user for the project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.CreateProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.CreateProjectResponse.SerializeToString,
            ),
            'AddUserToProject': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUserToProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.AddUserToProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.AddUserToProjectResponse.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectResponse.SerializeToString,
            ),
            'GetProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjects,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectsResponse.SerializeToString,
            ),
            'DestroyProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.DestroyProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.DestroyProjectResponse.SerializeToString,
            ),
            'UpdateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.UpdateProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.UpdateProjectResponse.SerializeToString,
            ),
            'RemoveUserFromProject': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUserFromProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.RemoveUserFromProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.RemoveUserFromProjectResponse.SerializeToString,
            ),
            'GetUserPermissionsForProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserPermissionsForProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetUserPermissionsForProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetUserPermissionsForProjectResponse.SerializeToString,
            ),
            'EditUserPermissionsForProject': grpc.unary_unary_rpc_method_handler(
                    servicer.EditUserPermissionsForProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.EditUserPermissionsForProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.EditUserPermissionsForProjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v1.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
    """ProjectService

    Contains all methods that get/create or update Projects and associated resources
    """

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/CreateProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.CreateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUserToProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/AddUserToProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.AddUserToProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.AddUserToProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/GetProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/GetProjects',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/DestroyProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.DestroyProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.DestroyProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/UpdateProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.UpdateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveUserFromProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/RemoveUserFromProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.RemoveUserFromProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.RemoveUserFromProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserPermissionsForProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/GetUserPermissionsForProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetUserPermissionsForProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.GetUserPermissionsForProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditUserPermissionsForProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v1.ProjectService/EditUserPermissionsForProject',
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.EditUserPermissionsForProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v1_dot_project__service__pb2.EditUserPermissionsForProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
