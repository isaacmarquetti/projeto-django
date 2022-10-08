from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501

        # Se a página for 1
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Se a página for 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Se a página for 3
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        # Se a página for 4
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_sure_middle_ranges_are_correct(self):  # noqa: E501

        # Se a página for 10
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # Se a página for 12
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # Se a página for 18
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Se a página for 19
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Se a página for 20
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Se a página for 21
        # Aqui vai rotacionar
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
