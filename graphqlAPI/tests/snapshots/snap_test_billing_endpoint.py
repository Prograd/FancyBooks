# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['UserEndpointTest::test_create_billing 1'] = {
    'data': {
        'createBilling': {
            'billing': {
                'id': '2',
                'order': {
                    'books': [
                        {
                            'id': '1'
                        },
                        {
                            'id': '2'
                        },
                        {
                            'id': '3'
                        }
                    ],
                    'id': '2'
                },
                'status': 'created'
            }
        }
    }
}
