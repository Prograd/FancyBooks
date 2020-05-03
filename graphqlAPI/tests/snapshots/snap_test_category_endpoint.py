# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['CategoryEndpointTest::test_get_all_categories 1'] = {
    'data': {
        'categories': [
            {
                'bookSet': [
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
                'id': '1',
                'name': 'test'
            }
        ]
    }
}
