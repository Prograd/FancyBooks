# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['OrderEndpointTest::test_get_all_order_when_admin 1'] = {
    'data': {
        'orders': [
            {
                'billing': {
                    'id': '1'
                },
                'id': '1',
                'orderPrice': 237.69
            }
        ]
    }
}

snapshots['OrderEndpointTest::test_get_all_order_when_anonymous 1'] = {
    'data': {
        'orders': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': 'Not logged in!',
            'path': [
                'orders'
            ]
        }
    ]
}
