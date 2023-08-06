"""
    ---Task 2---
    2.Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
"""
import os
import pickle
import json
import csv


class Serializer:
    def __init__(self, directory):
        self.directory = directory

    def __get_file_path(self, filename):
        return os.path.join(self.directory, filename)

    def read_pickle(self, filename):
        pickle_path = self.__get_file_path(filename)
        try:
            with open(pickle_path, 'rb') as file:
                data = pickle.load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' was not found.")
        except pickle.UnpicklingError:
            raise ValueError(f"The file '{filename}' is not a valid pickle file.")

    def read_json(self, filename):
        json_path = self.__get_file_path(filename)
        try:
            with open(json_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file '{filename}' is not a valid JSON file.")

    def read_csv(self, filename):
        csv_path = self.__get_file_path(filename)
        try:
            with open(csv_path, 'r', newline='') as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' was not found.")
        except csv.Error:
            raise ValueError(f"The file '{filename}' is not a valid CSV file.")

    def convert_pickle2csv(self, pickle_file):
        pickle_filepath = self.__get_file_path(pickle_file)
        csv_filepath = os.path.splitext(pickle_file)[0] + '.csv'
        with open(pickle_filepath, 'rb') as pickle_file:
            try:
                data = pickle.load(pickle_file)
                if not isinstance(data, list):
                    raise TypeError("Invalid data format in pickle file. Expected a list of dictionaries.")

                # Получаем заголовки столбцов из ключей словаря
                fieldnames = list(data[0].keys())

                csv_filepath_full = os.path.join(self.directory, csv_filepath)
                with open(csv_filepath_full, 'w', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    # Записываем заголовки в CSV файл
                    writer.writeheader()

                    # Записываем данные из списка словарей в CSV файл
                    writer.writerows(data)

                print(f"Converting {pickle_filepath} to {csv_filepath} is complete.")
            except pickle.UnpicklingError as e:
                print(f"Error unpickling {pickle_filepath}: {e}")
            except Exception as e:
                print(f"Error converting {pickle_filepath} to CSV: {e}")

    def convert_json2pickle(self):
        for filename in os.listdir(self.directory):
            filepath = self.__get_file_path(filename)
            if filepath.lower().endswith('.json') and os.path.isfile(filepath):
                name_without_extension = os.path.splitext(filename)[0]
                pickle_file = name_without_extension + '.pickle'
                pickle_filepath = self.__get_file_path(pickle_file)

                with open(filepath, 'r', encoding='utf-8') as json_file:
                    try:
                        json_data = json.load(json_file)
                        with open(pickle_filepath, 'wb') as pickle_out:
                            pickle.dump(json_data, pickle_out)

                        print(f'Converting "{filename}" to "{pickle_file}" is complete.')
                    except json.JSONDecodeError as e:
                        print(f'Error decoding JSON file "{filename}": {e}')
                    except Exception as e:
                        print(f'Error converting "{filename}" to pickle: {e}')
