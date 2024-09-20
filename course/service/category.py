from course.pb import course_category_pb2, course_category_pb2_grpc
from uuid import uuid4


class CategoryService(course_category_pb2_grpc.CategoryServiceServicer):
    def CreateCategory(self, request, context):
        return course_category_pb2.Category(
            id=str(uuid4()),
            name=request.name,
            description=request.description
        )
