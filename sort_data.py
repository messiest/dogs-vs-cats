import os
import shutil
import argparse

from tqdm import tqdm


def main(data_source='train/', data_dir='data/', train=True):
    split = 'train' if train else 'test'

    if split not in os.listdir(data_dir):
        os.mkdir(os.path.join(data_dir, split))

    pbar = tqdm(os.listdir(data_source))
    for i, file in enumerate(pbar):
        image_class = file.split('.')[0]

        pbar.set_description(file)
        if image_class not in os.listdir(os.path.join(data_dir, split)):
            os.mkdir(os.path.join(data_dir, split, image_class))

        os.rename(
            os.path.join(data_source, file),
            os.path.join(data_dir, split, image_class, file),
        )

    # os.rmdir(data_source)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-source', type=str, default='train/')

    args = parser.parse_args()

    main(data_source=args.source)
