import os


class File:
    COUNTER = 0

    def __init__(self, file_name, method):
        self.name = file_name
        self.method = method

    def __enter__(self):
        if self.method in ("w", "a") or (
            os.path.isfile(self.name) and self.method in "r"
        ):
            File.COUNTER += 1
            log_file = open(
                "D:/Beetroot Academy II/lms_homework/No21/log_info/log.txt", "a"
            )
            log_file.write(f"> Create file No{File.COUNTER}\n")
            log_file.close()
            self.file = open(self.name, self.method)
            return self.file
        raise TypeError("Wrong params")

    def __exit__(self, types, value, traceback):
        self.no_error_file = File.COUNTER + 1
        log_file = open(
            "D:/Beetroot Academy II/lms_homework/No21/log_info/log.txt", "a"
        )
        log_file.write(f"> Error of create file No {self.no_error_file}")
        log_file.write(f" '{self.name}'\n")
        log_file.write(f"   Type error: {types},  Value: {value}\n")
        self.file.close()


if __name__ == "__main__":
    with File("test1.txt", "w") as file:
        file.write("testing 1....")

    with File("test2.txt", "w") as file:
        file.write("testing 2....")

    with File("test_positive2.txt", "w") as file:
        file.write("testing done")

    with open("test_positive2.txt") as temp_test_file:
        print(temp_test_file.readline())

    with File("df.txt", "r") as file:
        file.write("testing 2....")
