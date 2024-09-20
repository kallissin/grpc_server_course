import logging

import grpc
from course.pb import course_category_pb2, course_category_pb2_grpc
from dotenv import load_dotenv


load_dotenv()

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = course_category_pb2_grpc.CategoryServiceStub(channel)
        response = stub.CreateCategory(course_category_pb2.CreateCategoryRequest(
                name="Kelvin", 
                description="Esta é uma descrição"
            )
        )

        print("Category id: " + response.id)
        print("Category description: " + response.description)
        print("Category name: " + response.name)

if __name__ == "__main__":
    logging.basicConfig()
    run()
