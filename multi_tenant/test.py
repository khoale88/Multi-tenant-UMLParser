import controller
import pprint
import json
print json.dumps(controller.get_tenant_table_data("TA"), indent=4, sort_keys=False)


