import argparse

from cv2 import cv2
from segmentation import Segmentation
from inference import Inference


def main():
    img, mask, maskDetails = Segmentation(
        modelWeights=args.model_segmentation, cfgPath=args.cfg_path
    ).start_segmentation(img=cv2.imread(args.img_path + args.image))
    Inference(img, mask, maskDetails, inpaintModel=args.model_inpainting).inference()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image File Name")
    parser.add_argument(
        "--image",
        type=str,
        default="img.png",
        help="Enter the image file name located at ./img_input/",
    )
    parser.add_argument(
        "--model_segmentation",
        type=str,
        default="http://dl.fbaipublicfiles.com/detectron2/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x/139514569/model_final_c10459.pkl",
        help="Pre-trained Weights for Segmentation",
    )
    parser.add_argument(
        "--cfg_path",
        type=str,
        default="COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml",
        help="Path to model cfg file relative to './detectron2/model_zoo/configs' ",
    )
    parser.add_argument(
        "--model_inpainting",
        type=str,
        default="./models/1000000.pth",
        help="Weights for Inpainting relative to ./inpainting/",
    )
    parser.add_argument(
        "--img_path",
        type=str,
        default="./img_input/",
        help="Specify custom path for image",
    )
    args = parser.parse_args()

    main()
