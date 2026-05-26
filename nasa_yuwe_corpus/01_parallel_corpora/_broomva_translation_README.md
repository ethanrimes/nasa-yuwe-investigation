---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: translation
    struct:
    - name: pbb
      dtype: string
    - name: spa
      dtype: string
  splits:
  - name: train
    num_bytes: 109901
    num_examples: 2428
  - name: validation
    num_bytes: 31457
    num_examples: 607
  - name: test
    num_bytes: 33789
    num_examples: 759
  download_size: 137803
  dataset_size: 175147
---
# Dataset Card for "translation_pbb_spa"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)