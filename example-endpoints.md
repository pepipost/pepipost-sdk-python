## Table of Content
* [fetch event logs](#example1)
* [fetch summary stats](#example2)
* [Domain Add](#example3)
* [Domain delete](#example4)
* [Suppression add](#example5)
* [Suppression delete](#example6)
* [create subaccount](#example7)
* [update subaccount](#example8)
* [enable/disable subaccount](#example9)
* [delete subaccount](#example10)
* [set recurring credit in subaccount](#example11)
* [add credit in subaccount](#example12)
* [get credit details of subaccount](#example13)

<a name="example1"></a>
## fetch event logs 

```python

from pepipost.pepipost_client import PepipostClient
from pepipost.models.events_enum import EventsEnum
from pepipost.models.sort_enum import SortEnum
from pepipost.exceptions.api_exception import APIException
import dateutil.parser

api_key = 'your api_key here'

client = PepipostClient(api_key)



events_controller = client.events
startdate = dateutil.parser.parse('2016-03-13').date()
events = EventsEnum.PROCESSED
sort = SortEnum.ASC
enddate = dateutil.parser.parse('2020-05-26').date()
subject = 'test'

try:
    result = events_controller.get_events_get(startdate, events, sort, enddate, None, None, subject)
except APIException as e: 
    print(e)

```

<a name="example2"></a>
## fetch summary stats  

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.aggregated_by_enum import AggregatedByEnum
from pepipost.exceptions.api_exception import APIException
import dateutil.parser

api_key = 'your api_key here'

client = PepipostClient(api_key)



stats_controller = client.stats
startdate = dateutil.parser.parse('2016-03-13').date()
enddate = dateutil.parser.parse('2020-05-26').date()
aggregated_by = AggregatedByEnum.WEEK

try:
    result = stats_controller.get_stats_get(startdate, enddate, aggregated_by)
except APIException as e: 
    print(e)
```
<a name="example3"></a>
## Domain Add  

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.domain_struct import DomainStruct
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



domain_controller = client.domain
body = DomainStruct()
body.domain = 'example.com'
body.envelope_name = 'test'

try:
    result = domain_controller.add_domain(body)
except APIException as e: 
    print(e)
```

<a name="example4"></a>
## Domain delete 

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.delete_domain import DeleteDomain
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



domain_delete_controller = client.domain_delete
body = DeleteDomain()
body.domain = 'adc.xyz'

try:
    result = domain_delete_controller.delete_domain(body)
except APIException as e: 
    print(e)
```

<a name="example5"></a>
## Suppression add  

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.add_email_or_domain_to_suppression_list import AddEmailOrDomainToSuppressionList
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



suppression_controller = client.suppression
body = AddEmailOrDomainToSuppressionList()
body.domain = 'domain.xyz'
body.email = 'email@gmail.com'

try:
    result = suppression_controller.add_domain_or_email_to_suppression_list(body)
except APIException as e: 
    print(e)
```

<a name="example6"></a>
## Suppression delete  

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.remove_email_or_domain_to_suppression_list import RemoveEmailOrDomainToSuppressionList
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



suppression_controller = client.suppression
body = RemoveEmailOrDomainToSuppressionList()
body.domain = 'domain.xyx'
body.email = 'email@gmail.com'

try:
    result = suppression_controller.remove_domain_or_email_to_suppression_list(body)
except APIException as e: 
    print(e)
```

<a name="example7"></a>
## create subaccount 

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.create_subaccount import CreateSubaccount
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



subaccounts_create_subaccount_controller = client.subaccounts_create_subaccount
body = CreateSubaccount()
body.username = 'name'
body.email = 'email1.gmail.com'
body.setpassword = 'setpassword8'
body.password = 'aa'

try:
    result = subaccounts_create_subaccount_controller.create_subaccounts_create_subaccount_post(body)
except APIException as e: 
    print(e)
```

<a name="example8"></a>
## update subaccount  

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.update_subaccount import UpdateSubaccount
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



subaccounts_update_subaccount_controller = client.subaccounts_update_subaccount
body = UpdateSubaccount()
body.username = 'username'
body.new_email = 'email@gmail.com'
body.new_password = 'pwd'
body.confirm_password = 'pwd'

try:
    result = subaccounts_update_subaccount_controller.create_subaccounts_update_subaccount_post(body)
except APIException as e: 
    print(e)
```

<a name="example9"></a>
## enable/disable subaccount 

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.enable_or_disable_subacoount import EnableOrDisableSubacoount
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



subaccounts_controller = client.subaccounts
body = EnableOrDisableSubacoount()
body.username = 'username'
body.disabled = False

try:
    result = subaccounts_controller.update_subaccounts_patch(body)
except APIException as e: 
    print(e)
```

<a name="example10"></a>
## delete subaccount 

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.delete_subacoount import DeleteSubacoount
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



subaccounts_delete_controller = client.subaccounts_delete
body = DeleteSubacoount()
body.username = 'username'

try:
    result = subaccounts_delete_controller.delete_subaccounts_delete_delete(body)
except APIException as e: 
    print(e)
```

<a name="example11"></a>
## set recurring credit in subaccount 

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.update_recurring_credis_of_subaccount import UpdateRecurringCredisOfSubaccount
from pepipost.models.timeperiod_enum import TimeperiodEnum
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



setrecurringcreditddetails_controller = client.setrecurringcreditddetails
body = UpdateRecurringCredisOfSubaccount()
body.username = 'usename'
body.recurring_credit = 1
body.timeperiod = TimeperiodEnum.WEEKLY

try:
    result = setrecurringcreditddetails_controller.create_setrecurringcreditddetails_post(body)
except APIException as e: 
    print(e)
```

<a name="example12"></a>
## add credit in subaccount 

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.update_credis_of_subaccount import UpdateCredisOfSubaccount
from pepipost.models.action_enum import ActionEnum
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



subaccounts_setsubaccountcredit_controller = client.subaccounts_setsubaccountcredit
body = UpdateCredisOfSubaccount()
body.username = 'username'
body.action = ActionEnum.INCREASE
body.amount = 2

try:
    result = subaccounts_setsubaccountcredit_controller.create_subaccounts_setsubaccountcredit_post(body)
except APIException as e: 
    print(e)
```

<a name="example13"></a>
## get credit details of subaccount  

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.exceptions.api_exception import APIException

api_key = 'your api_key here'

client = PepipostClient(api_key)



subaccounts_get_sub_accounts_controller = client.subaccounts_get_sub_accounts
limit = '4'
offset = '0'

try:
    result = subaccounts_get_sub_accounts_controller.get_subaccounts_get_sub_accounts_get(limit, offset)
except APIException as e: 
    print(e)
```