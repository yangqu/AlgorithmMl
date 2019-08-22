import os
import pickle

from ratelimit import limits, sleep_and_retry
from tqdm import tqdm


if __name__ == "__main__":
    assert (True),print("daye")
    #print(os.listdir())
    #print(os.path.join("D:\\tmp","code"))
    subjects = [d for d in os.listdir('D:\\tmp\\data') if os.path.isdir(os.path.join('D:\\tmp\\data', d))]
    print(subjects)

    file_names = []
    for i in range(len(subjects)):
        sub = subjects[i]
        folder = os.path.join('D:\\tmp\\data', sub)
        files = [f for f in os.listdir(folder) if
                 os.path.isfile(os.path.join(folder, f)) and f.lower().endswith('.jpg')]
        for file in files:
            filename = os.path.join(folder, file)
            file_names.append({'filename': filename, 'class_id': i, 'subject': sub})

    print(file_names)
    from tqdm import tqdm

    for i in tqdm(range(10000000)):
        pass
    """
    samples = []
    for item in tqdm(file_names):
        filename = item['filename']
        attr = get_attr(filename)

        if len(attr) > 0:
            class_id = item['class_id']
            sub = item['subject']

            samples.append(
                {'class_id': class_id, 'subject': sub, 'full_path': filename, 'attr': attr})

    print('num_samples: ' + str(len(samples)))
    """
