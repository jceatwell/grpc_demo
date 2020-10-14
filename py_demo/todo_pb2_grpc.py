# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todo_pb2 as todo__pb2


class TodoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createTodo = channel.unary_unary(
                '/todoPackage.Todo/createTodo',
                request_serializer=todo__pb2.TodoItem.SerializeToString,
                response_deserializer=todo__pb2.TodoItem.FromString,
                )
        self.readTodos = channel.unary_unary(
                '/todoPackage.Todo/readTodos',
                request_serializer=todo__pb2.voidNoParam.SerializeToString,
                response_deserializer=todo__pb2.TodoItems.FromString,
                )
        self.readTodosStream = channel.unary_stream(
                '/todoPackage.Todo/readTodosStream',
                request_serializer=todo__pb2.voidNoParam.SerializeToString,
                response_deserializer=todo__pb2.TodoItem.FromString,
                )


class TodoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readTodosStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.createTodo,
                    request_deserializer=todo__pb2.TodoItem.FromString,
                    response_serializer=todo__pb2.TodoItem.SerializeToString,
            ),
            'readTodos': grpc.unary_unary_rpc_method_handler(
                    servicer.readTodos,
                    request_deserializer=todo__pb2.voidNoParam.FromString,
                    response_serializer=todo__pb2.TodoItems.SerializeToString,
            ),
            'readTodosStream': grpc.unary_stream_rpc_method_handler(
                    servicer.readTodosStream,
                    request_deserializer=todo__pb2.voidNoParam.FromString,
                    response_serializer=todo__pb2.TodoItem.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todoPackage.Todo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Todo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todoPackage.Todo/createTodo',
            todo__pb2.TodoItem.SerializeToString,
            todo__pb2.TodoItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readTodos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todoPackage.Todo/readTodos',
            todo__pb2.voidNoParam.SerializeToString,
            todo__pb2.TodoItems.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readTodosStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/todoPackage.Todo/readTodosStream',
            todo__pb2.voidNoParam.SerializeToString,
            todo__pb2.TodoItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
