from factory import Factory
from serializer import Serializer

if __name__ == '__main__':
    factory = Factory()

    bird_params = {"name": "Eagle", "wingspan": 2.5}
    bird = factory.create_animal("Bird", **bird_params)
    print(f'{bird.name}, {bird.wingspan}')

    fish_params = {"name": "Salmon", "max_depth": 20}
    fish = factory.create_animal("Fish", **fish_params)
    print(f'{fish.name}, {fish.depth()}')

    mammal_params = {"name": "Elephant", "weight": 5000}
    mammal = factory.create_animal("Mammal", **mammal_params)
    print(f'{mammal.name}, {mammal.weight}')

    # Task 2
    data_dir = 'data'
    data_reader = Serializer(data_dir)

    data_file = 'new_json.json'
    print(data_reader.read_json(data_file))

    data_reader.convert_json2pickle()

    data_file = 'new_json.pickle'
    data_reader.convert_pickle2csv(data_file)
