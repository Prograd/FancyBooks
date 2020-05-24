# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BookEndpointTest::test_get_all_books 1'] = {
    'data': {
        'books': [
            {
                'amount': 0,
                'authors': 'test test',
                'categories': [
                    {
                        'id': '1'
                    }
                ],
                'description': 'test description',
                'id': '1',
                'language': 'en-gb',
                'pageCount': 0,
                'price': 0.0,
                'publishedDate': '2019-12-12',
                'publisher': 'test',
                'subtitle': 'test sub',
                'thumbnailUrl': 'https://test.test',
                'title': 'test book'
            },
            {
                'amount': 0,
                'authors': 'test test',
                'categories': [
                    {
                        'id': '1'
                    }
                ],
                'description': 'test description',
                'id': '2',
                'language': 'en-gb',
                'pageCount': 67,
                'price': 79.23,
                'publishedDate': '2019-12-12',
                'publisher': 'test',
                'subtitle': 'test sub',
                'thumbnailUrl': 'https://test.test',
                'title': 'test book'
            },
            {
                'amount': 0,
                'authors': 'test test',
                'categories': [
                    {
                        'id': '1'
                    }
                ],
                'description': 'test description',
                'id': '3',
                'language': 'en-gb',
                'pageCount': 134,
                'price': 158.46,
                'publishedDate': '2019-12-12',
                'publisher': 'test',
                'subtitle': 'test sub',
                'thumbnailUrl': 'https://test.test',
                'title': 'test book'
            }
        ]
    }
}
