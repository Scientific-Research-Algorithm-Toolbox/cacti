_base_=[
        "../_base_/real_data.py",
        "../_base_/davis.py",
        "../_base_/default_runtime.py"
        ]

cr = 10
resize_h,resize_w = 512,512

train_pipeline = [
    dict(type='Flip', direction='horizontal',flip_ratio=0.5,),
    dict(type='Resize',resize_h=resize_h,resize_w=resize_w)
]

gene_meas = dict(type='GenerationGrayMeas')

train_data = dict(
    type="DavisData",
    data_root="/home/wanglishun/datasets/DAVIS/DAVIS-480/JPEGImages/480p",
    mask_path="test_datasets/mask/real_mask.mat",
    mask_shape=(resize_h,resize_w,cr),
    pipeline=train_pipeline,
    gene_meas = gene_meas,
)

real_data = dict(
    data_root="test_datasets/real_data/cr10",
    cr=cr
)

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=2,
)

model = dict(
    type='MetaSCI',
    in_ch=cr
)

eval=dict(
    flag=False,
    interval=1
)

checkpoints="checkpoints/metasci/metasci_real_cr10.pth"