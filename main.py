# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:40 AM", "0:25"))
# Returns: "2:45 AM (next day)"


# Run unit tests automatically
main(module='test_module', exit=False)