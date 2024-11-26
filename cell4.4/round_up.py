#!/usr/bin/env python3

import math;

try:
    number = float(input("Give me a number: "));
    print(f"{math.ceil(number)}");
except ValueError:
    print("Please enter a valid number");
except KeyboardInterrupt:
    print("\nBye bye");
except EOFError:
    print("\nBye bye");
except Exception as e:
    print(f"An error occurred: {e}");

# try:
#     number = float(input("Give me a number: "));
#     print(f"{round(number)}");
# except ValueError:
#     print("Please enter a valid number");
# except KeyboardInterrupt:
#     print("\nBye bye");
# except EOFError:
#     print("\nBye bye");
# except Exception as e:
#     print(f"An error occurred: {e}");
# exit(0);