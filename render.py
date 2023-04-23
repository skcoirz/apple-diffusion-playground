from python_coreml_stable_diffusion import pipeline

# Example command from repo readme. Core function is in pipeline.py main function.
# python -m python_coreml_stable_diffusion.pipeline
# 	--prompt "a photo of an astronaut riding a horse on mars"
# 	-i coreml-stable-diffusion-2-1-base/original/packages
#   -o output
# 	--compute-unit ALL
# 	--seed 93

# shell command.
# python -m python_coreml_stable_diffusion.pipeline --prompt "a photo of an astronaut riding a horse on mars" -i coreml-stable-diffusion-2-1-base/original/packages --model-version stabilityai/stable-diffusion-2-1-base -o output --compute-unit ALL --seed 93

# python -m python_coreml_stable_diffusion.pipeline
# 	--prompt "a photo of an astronaut riding a horse on mars"
# 	--compute-unit ALL
# 	-o output
# 	--seed 93
# 	-i models/coreml-stable-diffusion-v1-5_original_packages
# 	--model-version runwayml/stable-diffusion-v1-5


# Apple Converted Stable Diffusion Model - stability.ai Stable Diffusion
# https://huggingface.co/apple/coreml-stable-diffusion-2-base
# https://huggingface.co/docs/diffusers/optimization/mps // huggingface pipeline


import argparse
def get_args_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--prompt",
        required=True,
        help="The text prompt to be used for text-to-image generation.")
    parser.add_argument(
        "-i",
        required=True,
        help=("Path to input directory with the .mlpackage files generated by "
              "python_coreml_stable_diffusion.torch2coreml"))
    parser.add_argument("-o", required=True)
    parser.add_argument("--seed",
                        "-s",
                        default=93,
                        type=int,
                        help="Random seed to be able to reproduce results")
    parser.add_argument(
        "--model-version",
        default="CompVis/stable-diffusion-v1-4",
        help=
        ("The pre-trained model checkpoint and configuration to restore. "
         "For available versions: https://huggingface.co/models?search=stable-diffusion"
         ))
    parser.add_argument(
        "--compute-unit",
        choices="'ALL', 'CPU_AND_GPU', 'CPU_ONLY', 'CPU_AND_NE'",
        default="ALL",
        help=("The compute units to be used when executing Core ML models. "
              f"Options: 'ALL', 'CPU_AND_GPU', 'CPU_ONLY', 'CPU_AND_NE'"))
    parser.add_argument(
        "--scheduler",
        choices="...ignored...",
        default=None,
        help=("The scheduler to use for running the reverse diffusion process. "
             "If not specified, the default scheduler from the diffusers pipeline is utilized"))
    parser.add_argument(
        "--num-inference-steps",
        default=50,
        type=int,
        help="The number of iterations the unet model will be executed throughout the reverse diffusion process")
    parser.add_argument(
        "--guidance-scale",
        default=7.5,
        type=float,
        help="Controls the influence of the text prompt on sampling process (0=random images)")
    parser.add_argument(
        "--controlnet",
        nargs="*", 
        type=str,
        help=("Enables ControlNet and use control-unet instead of unet for additional inputs. "
            "For Multi-Controlnet, provide the model names separated by spaces."))
    parser.add_argument(
        "--controlnet-inputs",
        nargs="*", 
        type=str,
        help=("Image paths for ControlNet inputs. "
            "Please enter images corresponding to each controlnet provided at --controlnet option in same order."))
    return parser

def render(prompt):
	args = get_args_parser().parse_args([
		"--prompt", prompt,
		"-i", "coreml-stable-diffusion-2-1-base/original/packages",
		"-o", "output",
		"--compute-unit", "ALL",
		"--model-version", "stabilityai/stable-diffusion-2-1-base",
		"--seed", "93"])
	pipeline.main(args)

render("a photo of an astronaut riding a horse on mars")