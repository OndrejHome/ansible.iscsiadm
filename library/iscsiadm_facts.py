#!/usr/bin/python

DOCUMENTATION = '''
---
module: iscsiadm_facts
short_description: iscsiadm facts module
description:
     - Module for gathering configuration facts of iscsiadm for ansible.
version_added: "2.4"
options:
notes:
   - Tested on CentOS 7.2, 7.4
requirements: [ ]
author: "Ondrej Famera <ondrej-xa2iel8u@famera.cz>"
'''

EXAMPLES = '''
- iscsiadm_facts

'''


def main():
        module = AnsibleModule(
                argument_spec=dict(),
                supports_check_mode=True
        )

        result = {}

        try:
            file = open('/etc/iscsi/initiatorname.iscsi', 'r')
            for line in file:
                if line.startswith('#'):
                    continue
                text = line.rstrip()
            result['ansible_facts'] = {}
            result['ansible_facts']['iscsi_initiator_name'] = text.split('=')[1]
        except IOError as e:
            result['ansible_facts'] = {}
        except OSError as e:
            module.fail_json(msg="Failed to open /etc/iscsi/initiatorname.iscsi file - %s" % (e))
        module.exit_json(**result)

# import module snippets
from ansible.module_utils.basic import *
main()
