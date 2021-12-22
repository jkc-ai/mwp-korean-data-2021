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