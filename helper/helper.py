
import model.client as client
import model.film as film


class Helper:

    @staticmethod
    def open_file(file_name):
        try:
            return open(file_name, "r")
        except:
            print("Error opening the file \"" + file_name + "\"")

        return None

    @staticmethod
    def fill_list(file, type):
        temp_list = []
        cont = 0
        for line in file:
            record = line.rstrip().split(',')
            # Getting fields
            if type == 'clients':
                temp_list.append(client.Client(name=record[0], code=int(record[1]), last_client=record[2], available=Helper.to_boolean(record[3])))

            elif type == 'film':
                temp_list.append(film.Film(name=record[0], code=int(record[1]), last_film=record[2], available=Helper.to_boolean(record[3])))

        return temp_list

    @staticmethod
    def to_boolean(string):
        """
        :rtype : bool
        """
        if string == "True":
            return True
        return False