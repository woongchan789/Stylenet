# Stylenet
Stylenet experiments using various encoders (resnet152, inception_v3, vit_base_resnet50_224_in21k)

## 구현논문
- Stylenet: Generating Attractive Visual Captions with Styles (CVPR, 2017)
- Link: https://ieeexplore.ieee.org/document/8099591/similar#similar

## Overview
<p align="center"><img src="https://github.com/woongchan789/Stylenet/assets/75806377/02458e23-4c52-4c89-8020-f382a49aeec8"></p>

- 일반적으로 (image, caption) dataset은 a factual description에 집중되어있음
- 본 논문에서는 조금 더 attractive image caption을 생성하는 것을 목적으로 하였고, 이를 style로 표현하여 다양한 style의 caption을 생성해내고자 하였음
- 본 논문에서 구현하고자 하는 style은 크게 2가지
- Style: Romantic (간지폭발), Humorous (개꿀잼)

## Approach
<p align="center"><img src="https://github.com/woongchan789/Stylenet/assets/75806377/0f07b957-1b09-485f-aacf-8540aa83b89a"></p>

- 본 논문에서는 Romantic, Humorous한 단어들을 학습하기 위해 (image, romantic_caption), (image, humorous_caption) 이렇게 **image-stylized caption pair**로 학습하는 방식이 아닌 **monolingual stylized language corpus**로 학습을 진행
- 보다 자세히 본 논문에서는 ‘**monolingual stylized language corpus**’로 선택한 것은 ‘For the additional text corpus, **we used the 7K stylized captions without paired images** to train the stylized language model.’
- 즉, 7천 개의 humorous captions, romantic captions로부터 vocab을 구성하여 이미지없이 이로부터 captioning

## 코드진행

1. [preprocess.py] flickr30k에서 7k를 선택
    1. 단, random하게 선택하는 것이 아닌 사전에 7k로 구성해놓은 humorous, romantic caption에 맞는 image, caption을 선택)
2. [build_vocab.py] vocab을 만듦
    1. **factual** vocab을 만들 때는 **vocab from factual captions**
    2. **humorous** vocab을 만들 때는 **vocab from factual captions** + **vocab from humorous captions**
    3. **romantic** vocab을 만들 때는 **vocab from factual captions** + **vocab from romantic captions**
3. [train.py] 학습 진행
    1. 별도로 train.sh을 만들어서 encoder로 Resnet-152, Inception_v3, Vision transformer (based Resnet-50) 3개의 encoder를 비교 실험
4. [sample.py] inference를 잘 하는지 check!
    1. flickr30k에서 추출한 10개의 image(flickr7k에 속하지 않는 10개의 이미지) + 남웅찬의 이미지(5개)
  
## Dataset

- 데이터셋은 Flickr30k ([Link](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset))에서 7k만 추출하여 사용
- 7k = 정확하게 7000개의 (image, caption) pair

## 수정사항

- torch.nn.DataParallel을 사용하여 multi-gpu 사용
- Encoder를 조금 더 다양하게 사용해보고 비교 진행
    - 논문에서는 Resnet-152를 사용하였음
    - 실험으로 Resnet-152, Inception_v3, Vision transformer (based Resnet-50) 3개의 모델을 encoder로 써보고 성능 비교 실험 진행

## 실험결과

- 실험은 시간이 너무 오래 걸리는 관계로 factual, homorous만 진행
- 3개의 encoder에 따른 cross entropy loss 결과값 확인
- 3개의 encoder에 따른 sample 15개의 caption quality 확인




