from tests_by_bug_id import all_tests
from util.logs import Log

url = "http://klahnakoski-es.corp.tor1.mozilla.com:9292"

try:
    all_tests(url)
finally:
    Log.stop()