from datasets import tqdm


class DataMerge:
    def __init__(self):
        self.trains = [
            'dataset/train_komoran.txt',
            'dataset/data/eng_google_civil_train.txt'
        ]

        self.validations = [
            'dataset/validation_komoran.txt',
            'dataset/data/eng_google_civil_validation.txt'
        ]

        self.train_path = 'dataset/train.txt'
        self.validation_path = 'dataset/validation.txt'

    def get_all_data(self, path):
        train_data = []

        for train_path in path:
            with open(train_path, 'rt') as f:
                for line in tqdm(f):
                    train_data.append(line.rstrip())

        return train_data

    def merge(self):
        train_data = self.get_all_data(self.trains)
        validation_data = self.get_all_data(self.validations)

        print('all data loaded')

        with open(self.train_path, 'wt') as f:
            for line in tqdm(train_data):
                f.write(line + '\n')

        with open(self.validation_path, 'wt') as f:
            for line in tqdm(validation_data):
                f.write(line + '\n')


if __name__ == '__main__':
    dm = DataMerge()
    dm.merge()