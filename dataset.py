import json

import torch
from torch.utils.data import Dataset, DataLoader

class ClassifierDataset(Dataset):
    def __init__(self, json_path):
        self.json_path = json_path
        with open(json_path, 'r', encoding = 'UTF-8-sig') as j:
            self.mwp_cpae = json.load(j)
        
    def read_cpae(self, idx):
        c = self.mwp_cpae[str(idx)]['class']
        p = self.mwp_cpae[str(idx)]['question']
        a = self.mwp_cpae[str(idx)]['answer']
        e = self.mwp_cpae[str(idx)]['equation'] if c == '산술연산' else 'none'
        return c, p, a, e

    def __len__(self):
        return len(self.mwp_cpae.keys())

    def __getitem__(self, idx):
        return self.read_cpae(idx)

if __name__ == '__main__':
    json_path = './public_mwp_data.json'
    dataset = ClassifierDataset(json_path = json_path)
    for i in range(1, dataset.__len__() + 1):
        c, p, a, e = dataset.__getitem__(i)
        print(c)
        print(p)
        print(a)
        print(e)