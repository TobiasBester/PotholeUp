from shutil import copy

import pandas as pd

train_ids_labels = './data/train_ids_labels.csv'
all_data = './data/all_data'


def move_image(sample_id, target):
    src = '{}/{}.JPG'.format(all_data, sample_id)
    dest = './data/train/{}/'.format(target)
    copy(src, dest)


if __name__ == '__main__':

    train_labels = pd.read_csv(train_ids_labels)
    print(train_labels)

    for row in train_labels.itertuples():
        move_image(row[1], row[2])
