import json

import torch
from torch.utils.data import Dataset, DataLoader

class ClassifierDataset(Dataset):
    def __init__(self, json_path):
        self.json_path = json_path

    def __len__(self):
        return 0

    def __getitem__(self, idx):
        return 0


if __name__ == '__main__':
    json_path = './public_mwp_data.json'

    dataset = ClassifierDataset(json_path = json_path)
    dataloader = DataLoader(dataset, batch_size = 4, shuffle = True, pin_memort = True)
    print(dataset.__len__())