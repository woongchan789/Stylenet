model_list='vit_base_resnet50_224_in21k'
# model_list='resnet152 inception_v3 vit_base_resnet50_224_in21k'

for model in $model_list
do
    echo "Encoder_model: $model"
    EXP_NAME="encoder_model_$model"    # 설정한 환경 이름
    
    if [ -d "$EXP_NAME" ]    # EXP_NAME이 디렉토리면 True
    then
        echo "$EXP_NAME is exist"
    else
        CUDA_VISIBLE_DEVICES=0,1 python train.py \
        --exp-name $EXP_NAME \
        --model_name $model
    fi

done