iscsiadm
=========

Role for installing and setting up iscsiadm iSCSI initiator.

Requirements
------------

Working iSCSI target (server). This role is only configuring the initiator (client).

Role Variables
--------------

  - iSCSI target tcp port (defaults to 3260)
    ```
    iscsi_target_port: 3260
    ```

  - (optional) iSCSI initiator WWN
    ```
    iscsi_initiator_wwn: iqn.1994-05.com.redhat:client1
    ```

  - (optional) iSCSI target IP and target WWN (when supplied the role will try to discover target and login into it)
    ```
    iscsi_target_wwn: iqn.1994-05.com.redhat:target
    iscsi_target_ip: 192.168.0.1
    ```

Example Playbook
----------------

Without any variables passed this role just installs and enables iscsiadm tools on system

    - hosts: servers
      roles:
         - { role: OndrejHome.iscsiadm }

Below example will install iscsiadm, set initiator WWN and instruct systems to discover and login into iSCSI target.

    - hosts: servers
      roles:
         - { role: OndrejHome.iscsiadm, iscsi_target_ip: "192.168.0.1", iscsi_target_wwn: "iqn.1994-05.com.redhat:target", iscsi_initiator_wwn: "iqn.1994-05.com.redhat:client1" }
License
-------

GPLv3

Author Information
------------------

To get in touch with author you can use email ondrej-xa2iel8u@famera.cz or create a issue on github when requesting some feature.
