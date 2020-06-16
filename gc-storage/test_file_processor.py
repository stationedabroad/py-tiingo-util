from unittest.mock import Mock
import json

json = Mock()
json.dumps({'a': 1})
json.dumps({'a': 1})
print(json.dumps.assert_called())
print(json.dumps.call_count)