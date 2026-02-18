from rest_framework.pagination import PageNumberPagination

class ProjectPagination(PageNumberPagination):
    page_size = 3   # number of projects per page (homepage)
    page_size_query_param = 'limit'
    max_page_size = 20