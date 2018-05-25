import pathlib

class Errlog(type):

    def __new__(self, log_file_name, log):
        file_name = pathlib.Path(log_file_name)
        if not file_name.parent.exists():
            raise FileExistsError("Нет такой директории")

        with open(log_file_name, 'a+') as file:
            file.write(log)


if __name__ == "__main__":
    count = 1
    while True:
        test = Errlog('/tmp/test.log', str(count) + ' test\n')
        count += 1
