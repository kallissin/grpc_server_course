from concurrent import futures
import logging

import grpc

from course.service.category import CategoryService
from course.pb import course_category_pb2_grpc

from dotenv import load_dotenv

load_dotenv()

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_category_pb2_grpc.add_CategoryServiceServicer_to_server(CategoryService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
    print("Server started, listening on " + port)


if __name__ == "__main__":
    logging.basicConfig()
    serve()