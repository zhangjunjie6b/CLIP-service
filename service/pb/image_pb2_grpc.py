# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.image_pb2 as image__pb2


class ImgHandleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImgToVector = channel.unary_unary(
                '/ImgHandle/ImgToVector',
                request_serializer=image__pb2.Request.SerializeToString,
                response_deserializer=image__pb2.Reply.FromString,
                )
        self.TextToVector = channel.unary_unary(
                '/ImgHandle/TextToVector',
                request_serializer=image__pb2.TextRequest.SerializeToString,
                response_deserializer=image__pb2.Reply.FromString,
                )


class ImgHandleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ImgToVector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TextToVector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImgHandleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ImgToVector': grpc.unary_unary_rpc_method_handler(
                    servicer.ImgToVector,
                    request_deserializer=image__pb2.Request.FromString,
                    response_serializer=image__pb2.Reply.SerializeToString,
            ),
            'TextToVector': grpc.unary_unary_rpc_method_handler(
                    servicer.TextToVector,
                    request_deserializer=image__pb2.TextRequest.FromString,
                    response_serializer=image__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImgHandle', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImgHandle(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ImgToVector(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImgHandle/ImgToVector',
            image__pb2.Request.SerializeToString,
            image__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TextToVector(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImgHandle/TextToVector',
            image__pb2.TextRequest.SerializeToString,
            image__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
