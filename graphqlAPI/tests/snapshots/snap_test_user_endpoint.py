# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['UserEndpointTest::test_create_user 1'] = {
    'data': {
        'createUser': {
            'user': {
                'email': 'test@test.test',
                'username': 'test'
            }
        }
    }
}
