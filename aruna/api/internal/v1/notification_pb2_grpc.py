# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.internal.v1 import notification_pb2 as aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2


class InternalEventServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterEvent = channel.unary_unary(
                '/aruna.api.internal.v1.InternalEventService/RegisterEvent',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2.RegisterEventRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2.RegisterEventResponse.FromString,
                )


class InternalEventServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InternalEventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterEvent,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2.RegisterEventRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2.RegisterEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.internal.v1.InternalEventService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InternalEventService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalEventService/RegisterEvent',
            aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2.RegisterEventRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_notification__pb2.RegisterEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)