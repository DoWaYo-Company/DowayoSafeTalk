from datasets import load_dataset, tqdm


class DataConverterEngGoogleCivil:
    def __init__(self):
        self.dataset = load_dataset("google/civil_comments")
        self.result_path = 'dataset/data/eng_google_civil'


    def convert(self, type):
        maxlen = 250
        THRESHOLD = 0.2

        results = []

        count_1 = 0
        count_0 = 0

        for train in tqdm(self.dataset[type]):
            text = train['text']
            bad_score = train['toxicity'] + train['severe_toxicity'] + train['obscene'] + train['threat'] + train['insult'] + train['identity_attack'] + train['sexual_explicit']

            text = text.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('|', ' ')

            if len(text) > maxlen:
                continue
            # print(bad_score)

            if bad_score > THRESHOLD:  # 일정 범위를 넘어서면 욕설로 간주
                results.append(f'{text}|1')
                count_1 += 1
            else:
                results.append(f'{text}|0')
                count_0 += 1

        print(f'{count_0} {count_1}')

        with open(f'{self.result_path}_{type}.txt', 'wt') as f:
            for result in tqdm(results):
                f.write(result + '\n')


if __name__ == "__main__":
    converter = DataConverterEngGoogleCivil()
    converter.convert('train')
    converter.convert('validation')
