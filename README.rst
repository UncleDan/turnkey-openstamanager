OpenSTAManager - Technical service managemente and billing system
===================================================

**APPLIANCE IN VERY ALPHA STAGE: DO NOT USE IN PRODUCTION!**

The OpenSTAManager management system is an open-source, web-based software developed by the IT company [DevCode](https://www.devcode.it/) in Este to manage and archive technical service and related billing.
The name of the project derives from the partial translation into English of its main elements: its open-source nature and its purpose as a Technical Support Service Manager.

A management software, identified in the set of applications that automate management processes within companies, usually belongs to a specific industry category, specializing in the areas of:

- Accounting management;
- Warehouse management;
- Production management and aid;
- Management and forecasting of corporate budgets;
- Financial management and analysis.

According to this definition, OpenSTAManager succeeds in generalizing within itself the characteristic functionalities of accounting and warehouse management, presenting in addition rather advanced modules intended to complement the business activity in relation to the assistance interventions of the working reality in question.

Official documentation is available at <https://docs.openstamanager.com/>.

*Translated with [DeepL.com (free version)](https://www.deepl.com/)*

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- OpenSTAManager configurations:
   
    - Installed from upstream source code to /var/www/openstamanager

      **Security note**: Updates to OpenSTAManager may require supervision so
      they **ARE NOT** configured to install automatically. See `OpenSTAManager
      documentation`_ for upgrading.

    - Websocket_ preconfigured and enabled.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Adminer: username **adminer**
-  OpenSTAManager: username **admin**


.. _OpenSTAManager: https://www.openstamanager.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _OpenSTAManager documentation: https://docs.openstamanager.com/
~~.. _Websocket: https://docs.openstamanager.com/administration/websocket/~~
.. _Adminer: https://www.adminer.org

