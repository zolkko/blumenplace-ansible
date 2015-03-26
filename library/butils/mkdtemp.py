#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import mkdtemp
from ansible.module_utils.basic import *


def main():
    module = AnsibleModule(
        argument_spec = {
            'suffix': {'default': ''},
            'prefix': {'default': 'tmp'},
            'dir': {'default': None},
        }
    )

    try:
        dir_name = mkdtemp(
            module.params.get('suffix'),
            module.params.get('prefix'),
            module.params.get('dir')
        )
        module.exit_json(changed=True, path=dir_name)
    except Exception as err:
        module.fail_json(msg='Failed to create temporary directory. Reason: %s' % err)


main()

