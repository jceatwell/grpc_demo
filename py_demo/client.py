from __future__ import print_function
import logging
import sys
import queue
import grpc
import todo_pb2
import todo_pb2_grpc


def send_item(todo_details):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:40000') as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        response = stub.createTodo(todo_pb2.TodoItem(id=-1,details=todo_details,done=False))

    print("Received from Server ...")
    print(response)

def stream_response():
    with grpc.insecure_channel('localhost:40000') as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        responses = stub.readTodosStream(todo_pb2.voidNoParam())
        for response in responses:
            print(response)

if __name__ == '__main__':
    logging.basicConfig()
    todo_details = sys.argv[1]
    send_item(todo_details)

    stream_response()