import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
UNIT_TEST_DIR = "../tests/unit"
UNIT_TEST_FILES_PATH = os.path.join(CURRENT_DIR, UNIT_TEST_DIR)

relevant_path = UNIT_TEST_FILES_PATH
included_extensions = ['py']
unit_tests = [fn for fn in os.listdir(relevant_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]

if unit_tests:
    for x in unit_tests:
        script = os.path.join(UNIT_TEST_FILES_PATH, x)
        print(script)
        os.system("python " + script)

