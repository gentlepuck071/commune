# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import server_pb2 as server__pb2


class ServerStub(object):
    """Service definition for tensor processing servers.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/Server/Forward',
                request_serializer=server__pb2.DataBlock.SerializeToString,
                response_deserializer=server__pb2.DataBlock.FromString,
                )


class ServerServicer(object):
    """Service definition for tensor processing servers.
    """

    def Forward(self, request, context):
        """Forward tensor request. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=server__pb2.DataBlock.FromString,
                    response_serializer=server__pb2.DataBlock.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """Service definition for tensor processing servers.
    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/Forward',
            server__pb2.DataBlock.SerializeToString,
            server__pb2.DataBlock.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)