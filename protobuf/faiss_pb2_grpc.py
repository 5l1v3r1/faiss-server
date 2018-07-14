# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import faiss_pb2 as faiss__pb2


class FaissServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HealthCheck = channel.unary_unary(
        '/faiss.FaissService/HealthCheck',
        request_serializer=faiss__pb2.HealthCheckRequest.SerializeToString,
        response_deserializer=faiss__pb2.HealthCheckResponse.FromString,
        )


class FaissServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HealthCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FaissServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HealthCheck': grpc.unary_unary_rpc_method_handler(
          servicer.HealthCheck,
          request_deserializer=faiss__pb2.HealthCheckRequest.FromString,
          response_serializer=faiss__pb2.HealthCheckResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'faiss.FaissService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
