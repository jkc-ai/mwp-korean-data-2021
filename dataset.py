import json

import torch
from torch.utils.data import Dataset, DataLoader

class ClassifierDataset(Dataset):
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path


    def __len__(self):
        return 0

    def __getitem__(self, idx):
        return 0