import os

class LinkLibrary():
    def __init__(self):
        self.__mail_directory = str(os.getcwd()) + "\links.txt"  # gets the directory of the links txt
        print(self.__mail_directory)
        self.read_counter = 0
        self.__links = []  # initializes the array of links
        self.__read_links()  # runs the read links function

    def __read_links(self):
        with open(self.__mail_directory, 'r') as links_list:  # creates a stream reader
            print("Opened the text file successfully")
            temp = links_list.readline()
            self.read_counter = 0
            while temp != "":
                temp = self.__format_link(str(temp))
                # print("Formatted link: " + temp)
                self.__links.append(temp)
                temp = links_list.readline()
                self.read_counter = self.read_counter + 1
            print("Read " + str(self.read_counter) + " links into the system")

    def __format_link(self, temp) -> str:
        temp = self.__check_https(temp)
        temp = self.__check_domain(temp)
        temp = self.__check_for_space(temp)
        return temp

    def __check_https(self, temp) -> str:  # adds https to the link given
        if "https://" in temp:
            return temp  # contains the correct https formatting
        else:
            if "http://" in temp:
                return temp.replace("http", "https")  # stops links from using http
            else:
                return "https://www." + temp  # adds https to start of link

    def __check_domain(self, temp) -> str:
        if temp.find('.') != -1:  # if temp contains a .
            return temp
        else:
            temp = temp.replace("\n", ".com\n")
            return temp

    def __check_for_space(self, temp):
        if ' ' in temp:
            return temp.replace(' ','')
        else:
            return temp

    def get_link(self, target) -> str:
        return self.__links[target]

    def get_count(self) -> int:
        return self.read_counter



