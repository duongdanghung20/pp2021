import pickle
import threading


class BackgroundThread(threading.Thread):
    def __init__(self, mode, pickled_file, dumped_obj=None, loaded_obj=None, loaded_array=None):
        threading.Thread.__init__(self)
        self.__loaded_array = loaded_array
        self.__mode = mode
        self.__dumped_obj = dumped_obj
        self.__pickled_file = pickled_file
        self.__loaded_obj = loaded_obj

    def run(self):
        if self.__mode == "dump":
            pickle.dump(self.__dumped_obj, self.__pickled_file)
        elif self.__mode == "load":
            if self.__loaded_array is not None:
                self.__loaded_array.append(pickle.load(self.__pickled_file))
            if self.__loaded_obj is not None:
                self.__loaded_obj = pickle.load(self.__pickled_file)

    def get_loaded_obj(self):
        return self.__loaded_obj
