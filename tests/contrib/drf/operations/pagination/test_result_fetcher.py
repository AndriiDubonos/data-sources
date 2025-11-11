# from django.db.models import QuerySet
# from django.test import RequestFactory, TestCase
#
# from courses.models import Course
# from data_sources.data_source import DataSource
# from data_sources.keys import DataSourceKeys
# from data_sources.meta import Meta
# from data_sources.contrib.django.operations.fetch_entities import FetchAllQuerySetOperation
# from data_sources.operations.store_in_meta import ImplicitStoreInMetaParamsOperation
# from data_sources.contrib.drf.operations.pagination.result_fetcher import PageNumberPaginateOperation
# from data_sources.contrib.django.operations.queryset import RootQuerySetOperation
# from utils.rest.pagination.descriptors import PaginationParams
# from utils.test_utils.mommy_recipes import (
#     course_recipe,
#     vendor_recipe,
# )
#
#
# class PageNumberPaginateOperationTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.vendor = vendor_recipe.make()
#
#     def test_links_without_host(self):
#         course_recipe.make(_quantity=5, vendor=self.vendor)
#
#         pagination_params = PaginationParams(page=2, page_size=2)
#
#         url = (
#             '/api/v1/vendor/4cda68da-68c4-4837-8719-a3a72af3ad3b/'
#             'courses/762100f0-f64f-4aae-965b-042d2cd75dc9/participants/'
#         )
#         request = RequestFactory().get(url)
#
#         data_source = DataSource(
#             operations=[
#                 ImplicitStoreInMetaParamsOperation(
#                     params=[(DataSourceKeys.PAGINATION_DATA, pagination_params), (DataSourceKeys.REQUEST, request)]
#                 ),
#                 AllCourseQuerySetOperation(),
#                 FetchAllQuerySetOperation(),
#                 PageNumberPaginateOperation(),
#             ]
#         )
#
#         res, meta = data_source.get_data(None)
#         self.assertEqual(res['previous'], f'{url}')
#         self.assertEqual(res['next'], f'{url}?page=3')
